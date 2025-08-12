import streamlit as st
import pandas as pd
import uuid
import os
import datetime
import openai
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# ---------- Config / Theme ----------
st.set_page_config(page_title="Finley — Finance Memory", layout="wide")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_KEY:
    openai.api_key = OPENAI_KEY

CATEGORIES = ["Revenue", "Expenses", "Forecast", "General"]
DEFAULT_AUTHOR = "Anonymous"
DEFAULT_TEAM = "FP&A"

# ---------- Utilities ----------
def now_iso():
    return datetime.datetime.utcnow().isoformat() + "Z"

def make_id():
    return str(uuid.uuid4())

def compute_embedding(text):
    """Return embedding vector using OpenAI text-embedding-3-small if key available."""
    if not OPENAI_KEY:
        return None
    try:
        resp = openai.Embedding.create(model="text-embedding-3-small", input=text)
        return np.array(resp["data"][0]["embedding"], dtype=np.float32)
    except Exception as e:
        st.warning(f"Embedding error: {e}")
        return None

def embed_similarity_scores(query_emb, embeddings):
    if query_emb is None or len(embeddings) == 0:
        return []
    # embeddings is list of np arrays
    mats = np.vstack(embeddings)
    sims = cosine_similarity([query_emb], mats)[0]
    return sims

# ---------- Session State Setup ----------
if "notes" not in st.session_state:
    # Seed with sample notes for a realistic demo
    seeded = [
        {
            "id": make_id(),
            "category": "Revenue",
            "comment": "Q2 revenue beat target by 12% due to strong EMEA enterprise deals.",
            "tags": ["Q2", "EMEA", "enterprise"],
            "author": "Olivia (Sales Ops)",
            "team": "Sales",
            "date": (datetime.datetime.utcnow() - datetime.timedelta(days=45)).isoformat() + "Z",
            "related_to": None,
            "source": "sales_report_q2.pdf",
            "resolved": False,
            "embedding": None
        },
        {
            "id": make_id(),
            "category": "Expenses",
            "comment": "Marketing overspend in May driven by a last-minute campaign in North America.",
            "tags": ["May", "marketing", "NA"],
            "author": "Marco (Marketing)",
            "team": "Marketing",
            "date": (datetime.datetime.utcnow() - datetime.timedelta(days=30)).isoformat() + "Z",
            "related_to": None,
            "source": "jira-campaign-123",
            "resolved": True,
            "embedding": None
        },
        {
            "id": make_id(),
            "category": "Forecast",
            "comment": "Sales expects pipeline to soften next quarter due to seasonality; conservative forecast suggested.",
            "tags": ["pipeline", "forecast", "seasonality"],
            "author": "Priya (Head of Sales)",
            "team": "Sales",
            "date": (datetime.datetime.utcnow() - datetime.timedelta(days=10)).isoformat() + "Z",
            "related_to": None,
            "source": None,
            "resolved": False,
            "embedding": None
        }
    ]
    st.session_state.notes = seeded

    # compute embeddings if API key exists
    if OPENAI_KEY:
        for n in st.session_state.notes:
            emb = compute_embedding(n["comment"])
            n["embedding"] = emb.tolist() if emb is not None else None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # tuples: (role, text, sources)

# ---------- Helper functions to manage notes ----------
def add_note(category, comment, tags, author, team, related_to, source, resolved=False):
    note = {
        "id": make_id(),
        "category": category,
        "comment": comment,
        "tags": [t.strip() for t in tags.split(",")] if tags else [],
        "author": author or DEFAULT_AUTHOR,
        "team": team or DEFAULT_TEAM,
        "date": now_iso(),
        "related_to": related_to,
        "source": source,
        "resolved": resolved,
        "embedding": None
    }
    # compute embedding if possible (store as list for JSON-compat)
    emb = compute_embedding(comment) if OPENAI_KEY else None
    note["embedding"] = emb.tolist() if emb is not None else None
    st.session_state.notes.insert(0, note)  # newest first
    return note

def notes_to_df(notes):
    df = pd.DataFrame([{
        "id": n["id"],
        "date": n["date"],
        "category": n["category"],
        "author": n["author"],
        "team": n["team"],
        "tags": ", ".join(n["tags"]),
        "comment": n["comment"],
        "resolved": n["resolved"],
        "source": n["source"]
    } for n in notes])
    return df

def export_notes_csv():
    df = notes_to_df(st.session_state.notes)
    return df.to_csv(index=False).encode("utf-8")

# ---------- Retrieval / Recall ----------
def recall_with_embeddings(query, top_k=3):
    """Return top_k matching notes and a short summary (via OpenAI chat) if key available."""
    if not OPENAI_KEY:
        return [], None
    q_emb = compute_embedding(query)
    if q_emb is None:
        return [], None
    embeddings = []
    note_map = []
    for n in st.session_state.notes:
        if n.get("embedding"):
            embeddings.append(np.array(n["embedding"], dtype=np.float32))
            note_map.append(n)
    if len(embeddings) == 0:
        return [], None
    sims = embed_similarity_scores(q_emb, embeddings)
    top_idx = np.argsort(sims)[::-1][:top_k]
    matches = [note_map[i] for i in top_idx]
    # Build a context string with matched comments
    context_text = "\n\n".join([f"- ({m['category']}, {m['date'][:10]}) {m['comment']}" for m in matches])
    # Ask OpenAI to summarize role-based; we produce a short summary and a slightly longer deep-dive
    try:
        system = (
            "You are Finley, an AI memory & summarization assistant for FP&A teams. "
            "Given relevant notes, produce a short 2-sentence CFO summary and a 3-4 sentence operational deep-dive."
        )
        prompt = f"Context notes:\n{context_text}\n\nQuestion: {query}\n\nOutput: JSON with keys 'cfo_summary' and 'deep_dive'."
        resp = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # if unavailable, this will error; user can replace with 'gpt-4o' or 'gpt-4'
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.2
        )
        content = resp["choices"][0]["message"]["content"]
        # We expect JSON; try to parse, else return raw text as deep_dive
        try:
            import json
            parsed = json.loads(content)
            return matches, parsed
        except Exception:
            return matches, {"cfo_summary": content, "deep_dive": content}
    except Exception as e:
        st.warning(f"AI recall error: {e}")
        return matches, None

def recall_keyword(query, top_k=3):
    """Fallback keyword recall: simple substring matching + basic prioritization."""
    q = query.lower()
    scored = []
    for n in st.session_state.notes:
        score = 0
        if q in n["comment"].lower():
            score += 3
        if any(q in tag.lower() for tag in n["tags"]):
            score += 2
        if q in (n["category"] or "").lower():
            score += 1
        if q in (n["source"] or "").lower():
            score += 1
        if score > 0:
            scored.append((score, n))
    scored.sort(key=lambda x: x[0], reverse=True)
    matches = [s[1] for s in scored[:top_k]]
    # Create a naive summary by concatenating matching comments
    if matches:
        cfo_summary = " | ".join([m["comment"] for m in matches][:2])
        deep_dive = "\n\n".join([f"{m['date'][:10]} {m['author']}: {m['comment']}" for m in matches])
        return matches, {"cfo_summary": cfo_summary, "deep_dive": deep_dive}
    return [], None

# ---------- UI Layout ----------
st.sidebar.title("Add a note / question")
# Category as big buttons (columns)
cat_cols = st.sidebar.columns(len(CATEGORIES))
category_choice = None
for i, cat in enumerate(CATEGORIES):
    if cat_cols[i].button(cat):
        category_choice = cat
# fallback to selectbox if none clicked
if not category_choice:
    category_choice = st.sidebar.selectbox("Or choose category", [""] + CATEGORIES)

comment_input = st.sidebar.text_area("Comment / Question", height=120, placeholder="Type a memo or question here...")
tags_input = st.sidebar.text_input("Tags (comma-separated)", help="e.g. Q2, EMEA, product")
author_input = st.sidebar.text_input("Author", value=DEFAULT_AUTHOR)
team_input = st.sidebar.text_input("Team", value=DEFAULT_TEAM)
source_input = st.sidebar.text_input("Source (optional)", placeholder="e.g. report filename or ticket id")
related_input = st.sidebar.selectbox("Related to (thread)", options=["None"] + ["{}: {}".format(n["id"][:8], n["comment"][:30]) for n in st.session_state.notes], index=0)
resolved_input = st.sidebar.checkbox("Mark as resolved", value=False)
if st.sidebar.button("Submit note"):
    if not category_choice:
        st.sidebar.error("Please pick a category.")
    elif not comment_input.strip():
        st.sidebar.error("Please enter a comment.")
    else:
        # related id parsing
        related_to_id = None
        if related_input != "None":
            related_to_id = related_input.split(":")[0]
        n = add_note(category_choice, comment_input.strip(), tags_input, author_input, team_input, related_to_id, source_input, resolved_input)
        st.sidebar.success("Saved note.")
        st.experimental_rerun()

st.sidebar.markdown("---")
st.sidebar.download_button("Export notes as CSV", data=export_notes_csv(), file_name="finley_notes.csv", mime="text/csv")

# ---------- Main area ----------
left, right = st.columns([2, 3])

with left:
    st.header("Memory Feed — Recent Notes")
    # Filters
    with st.expander("Filters", expanded=False):
        f_category = st.selectbox("Category", options=["All"] + CATEGORIES, index=0)
        f_team = st.text_input("Team (filter)", value="")
        f_author = st.text_input("Author (filter)", value="")
        date_preset = st.selectbox("Date range", options=["All", "Last 7 days", "Last 30 days", "Last quarter", "Custom"])
        if date_preset == "Custom":
            col1, col2 = st.columns(2)
            start_date = col1.date_input("Start date", value=None)
            end_date = col2.date_input("End date", value=None)
        else:
            start_date = end_date = None

    # Build filtered notes list
    notes = st.session_state.notes
    def passes_filters(n):
        if f_category != "All" and n["category"] != f_category:
            return False
        if f_team and f_team.lower() not in (n["team"] or "").lower():
            return False
        if f_author and f_author.lower() not in (n["author"] or "").lower():
            return False
        if date_preset != "All":
            dt = datetime.datetime.fromisoformat(n["date"].replace("Z", ""))
            now = datetime.datetime.utcnow()
            if date_preset == "Last 7 days" and (now - dt).days > 7:
                return False
            if date_preset == "Last 30 days" and (now - dt).days > 30:
                return False
            if date_preset == "Last quarter" and (now - dt).days > 90:
                return False
            if date_preset == "Custom" and start_date and end_date:
                if not (start_date <= dt.date() <= end_date):
                    return False
        return True

    filtered = [n for n in notes if passes_filters(n)]
    if filtered:
        for n in filtered:
            cols = st.columns([1, 4, 1])
            with cols[0]:
                st.markdown(f"**{n['category']}**")
            with cols[1]:
                st.write(f"**{n['comment']}**")
                st.write(f"*{n['author']} — {n['team']} — {n['date'][:10]}*")
                if n["tags"]:
                    st.write("Tags:", ", ".join(n["tags"]))
                if n["source"]:
                    st.write("Source:", n["source"])
                if n["related_to"]:
                    st.write("Thread:", n["related_to"])
            with cols[2]:
                if not n["resolved"]:
                    if st.button(f"Mark resolved: {n['id'][:8]}", key="res_"+n["id"]):
                        n["resolved"] = True
                        st.experimental_rerun()
                else:
                    st.success("Resolved")
    else:
        st.info("No notes match the filters. Add a note on the left to get started.")

with right:
    st.header("Ask Finley — get context & a summary")
    q = st.text_input("Ask a question or paste a prompt", value="", key="query_input")
    role_for_summary = st.selectbox("Summary style", options=["CFO (short)", "Operational (deep dive)"], index=0)
    if st.button("Ask Finley"):
        if not q.strip():
            st.warning("Please type a question.")
        else:
            # Add user's question as a note (optional): keep we store as comment with category 'General - Question'
            st.session_state.chat_history.append(("user", q, None))
            # Recall
            if OPENAI_KEY:
                matches, summary_struct = recall_with_embeddings(q, top_k=4)
            else:
                matches, summary_struct = recall_keyword(q, top_k=4)
            # Build response text
            if summary_struct:
                if role_for_summary.startswith("CFO"):
                    reply = summary_struct.get("cfo_summary") or summary_struct.get("deep_dive") or "No summary available."
                else:
                    reply = summary_struct.get("deep_dive") or summary_struct.get("cfo_summary") or "No details available."
            else:
                if matches:
                    reply = "Found context from notes:\n" + "\n".join([f"- {m['comment']} ({m['category']})" for m in matches])
                else:
                    reply = "I don't have past context for that yet. I will remember future notes you add."

            # Save Finley reply in history with source references
            sources = [{"id": m["id"], "category": m["category"], "snippet": m["comment"][:140]} for m in matches] if matches else []
            st.session_state.chat_history.append(("finley", reply, sources))

    # Render chat history
    for idx, (role, text, sources) in enumerate(st.session_state.chat_history[::-1]):  # latest first visually
        if role == "user":
            st.markdown(f"**You:** {text}")
        else:
            st.markdown(f"**Finley:** {text}")
            if sources:
                chips = []
                for s in sources:
                    # Show tiny snippet with a clickable anchor that scrolls to the note in the left panel (can't auto-scroll easily)
                    chips.append(f"[{s['category']} · {s['snippet']}]({'#'})")
                st.markdown("**Sources:** " + " · ".join(chips))

    st.markdown("---")
    st.write("Debug / Notes count:", len(st.session_state.notes))
    if st.checkbox("Show raw notes data (debug)"):
        st.json(st.session_state.notes)
