       [data-testid="collapsedControl"] {
           display: none !important;
       }

        /* This hides the collapse/expand sidebar button */
        [data-testid="stSidebarNavCollapse"] {
            display: none !important;
        }

        /* This hides the small chevron button in some Streamlit versions */
        button[kind="header"] {
            display: none !important;
        }

   </style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)
