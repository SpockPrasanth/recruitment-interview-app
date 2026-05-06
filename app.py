import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Miracle Recruitment Portal",
    page_icon="🚀",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

/* =====================================================
MAIN APP
===================================================== */

.stApp {
    background-color: #F4F5F7;
    font-family: 'Segoe UI', sans-serif;
}

/* =====================================================
TOP HEADER
===================================================== */

.top-header {
    background-color: #1F232A;
    padding: 15px 40px;
    border-radius: 0px;
    margin-bottom: 20px;
}

.logo-text {
    color: white;
    font-size: 42px;
    font-weight: 900;
    line-height: 40px;
}

.logo-subtext {
    color: #00AEEF;
    font-size: 14px;
    font-weight: bold;
    letter-spacing: 1px;
}

/* =====================================================
WELCOME BANNER
===================================================== */

.banner {
    background: linear-gradient(90deg, #0D5EA6, #1F6FB2);
    padding: 30px;
    border-radius: 6px;
    color: white;
}

.banner-title {
    font-size: 42px;
    font-weight: 700;
}

.banner-text {
    font-size: 18px;
    margin-top: 10px;
}

/* =====================================================
STAT CARDS
===================================================== */

.stat-card {
    background-color: white;
    padding: 25px;
    border-radius: 6px;
    text-align: center;
    box-shadow: 0px 1px 4px rgba(0,0,0,0.1);
}

.stat-title {
    font-size: 24px;
    font-weight: bold;
    color: #1F232A;
}

.stat-value {
    font-size: 38px;
    font-weight: bold;
    color: #0D5EA6;
}

/* =====================================================
SEARCH AREA
===================================================== */

.search-section {
    background-color: white;
    padding: 25px;
    border-radius: 6px;
    margin-top: 20px;
    margin-bottom: 20px;
}

/* =====================================================
QUESTION CARDS
===================================================== */

.question-card {
    background-color: white;
    padding: 25px;
    border-radius: 6px;
    margin-bottom: 20px;
    border-left: 6px solid #0D5EA6;
    box-shadow: 0px 1px 4px rgba(0,0,0,0.08);
}

.question-title {
    color: #0D5EA6;
    font-size: 24px;
    font-weight: bold;
}

.question-text {
    color: #333333;
    font-size: 18px;
    margin-top: 15px;
    line-height: 1.6;
}

/* =====================================================
BUTTONS
===================================================== */

.stButton button {
    background-color: #0D5EA6;
    color: white;
    border: none;
    border-radius: 4px;
    height: 45px;
    font-size: 16px;
    font-weight: 600;
    width: 100%;
}

.stButton button:hover {
    background-color: #084B87;
    color: white;
}

/* =====================================================
SIDEBAR
===================================================== */

section[data-testid="stSidebar"] {
    background-color: #FFFFFF;
    border-right: 1px solid #D9D9D9;
}

/* =====================================================
SIDEBAR TITLE
===================================================== */

.sidebar-title {
    color: #0D5EA6;
    font-size: 26px;
    font-weight: bold;
    margin-bottom: 20px;
}

/* =====================================================
FOOTER
===================================================== */

.footer {
    text-align: center;
    color: gray;
    padding: 30px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# TOP HEADER
# =====================================================

st.markdown("""
<div class="top-header">
    <div class="logo-text">
        MIRACLE
    </div>

    <div class="logo-subtext">
        SOFTWARE SYSTEMS
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================================
# TOP SECTION
# =====================================================

left, right = st.columns([3, 1.4])

with left:

    st.markdown("""
    <div class="banner">

        <div class="banner-title">
            Welcome to Miracle Recruitment Portal!
        </div>

        <div class="banner-text">
            Recruitment Interview Question Portal for Data Engineers,
            Power BI Developers, Microsoft Fabric Engineers,
            and Azure Data Professionals.
        </div>

    </div>
    """, unsafe_allow_html=True)

with right:

    st.markdown("""
    <div class="stat-card">
        <div class="stat-title">
            Total Questions
        </div>

        <div class="stat-value">
            120+
        </div>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# QUESTION BANK
# =====================================================

question_bank = {

    "Data Engineer": {

        "SQL": [

            {
                "question": "Explain Incremental Loading.",
                "answer": """
Incremental loading loads only changed or new records.

Methods:
- Timestamp
- CDC
- Watermark column
"""
            },

            {
                "question": "Difference between DELETE and TRUNCATE?",
                "answer": """
DELETE:
- Removes rows one by one
- Supports WHERE clause

TRUNCATE:
- Removes all rows quickly
- Resets identity
"""
            },

            {
                "question": "Explain Window Functions.",
                "answer": """
Window functions perform calculations across related rows.

Examples:
- ROW_NUMBER()
- RANK()
- LEAD()
- LAG()
"""
            }

        ],

        "Microsoft Fabric": [

            {
                "question": "What is Medallion Architecture?",
                "answer": """
Bronze → Raw Data

Silver → Cleansed Data

Gold → Business Ready Data
"""
            },

            {
                "question": "What is OneLake?",
                "answer": """
OneLake is unified storage in Microsoft Fabric.
"""
            }

        ],

        "Azure Data Factory": [

            {
                "question": "What is Integration Runtime?",
                "answer": """
Integration Runtime is compute infrastructure in ADF.
"""
            },

            {
                "question": "Explain Copy Activity.",
                "answer": """
Copy Activity transfers data between source and destination.
"""
            }

        ]
    },

    "Power BI Developer": {

        "DAX": [

            {
                "question": "What is CALCULATE in DAX?",
                "answer": """
CALCULATE modifies filter context in DAX.
"""
            },

            {
                "question": "Difference between Measure and Calculated Column?",
                "answer": """
Measure:
Calculated dynamically.

Calculated Column:
Stored physically in model.
"""
            }

        ],

        "Power Query": [

            {
                "question": "What is Query Folding?",
                "answer": """
Query Folding pushes transformations back to source system.
"""
            }

        ]
    }
}

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.markdown("""
<div class="sidebar-title">
⚙ Recruitment Setup
</div>
""", unsafe_allow_html=True)

role = st.sidebar.selectbox(
    "Select Role",
    list(question_bank.keys())
)

technology = st.sidebar.selectbox(
    "Select Technology",
    list(question_bank[role].keys())
)

experience = st.sidebar.selectbox(
    "Experience Level",
    [
        "Fresher",
        "2-4 Years",
        "5-8 Years",
        "10+ Years"
    ]
)

# =====================================================
# SEARCH SECTION
# =====================================================

st.markdown("""
<div class="search-section">
""", unsafe_allow_html=True)

search = st.text_input(
    "Search Questions",
    placeholder="Search by Question Keyword..."
)

st.markdown("""
</div>
""", unsafe_allow_html=True)

# =====================================================
# MAIN TITLE
# =====================================================

st.markdown(f"""
<h2 style='color:#0D5EA6; margin-bottom:30px;'>
📘 {role} → {technology} Interview Questions
</h2>
""", unsafe_allow_html=True)

questions = question_bank[role][technology]

# =====================================================
# QUESTION DISPLAY
# =====================================================

for idx, item in enumerate(questions):

    if search.lower() in item["question"].lower():

        st.markdown(
            f"""
            <div class="question-card">

                <div class="question-title">
                    Question {idx + 1}
                </div>

                <div class="question-text">
                    {item['question']}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        col1, col2 = st.columns([1, 5])

        with col1:

            if st.button(
                f"Show Answer",
                key=f"btn_{idx}"
            ):
                st.success(item['answer'])

        with col2:

            st.checkbox(
                "Question Asked",
                key=f"check_{idx}"
            )

# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<div class="footer">
Developed for Miracle Software Systems Recruitment Team
</div>
""", unsafe_allow_html=True)
