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
# CSS
# =====================================================

st.markdown("""
<style>

.stApp {
    background-color: #F4F5F7;
    font-family: 'Segoe UI';
}

/* HEADER */

.top-header {
    background-color: #1F232A;
    padding: 20px 40px;
    margin-bottom: 20px;
}

.logo-title {
    color: white;
    font-size: 42px;
    font-weight: 900;
    line-height: 40px;
}

.logo-subtitle {
    color: #00AEEF;
    font-size: 14px;
    font-weight: bold;
    letter-spacing: 1px;
}

/* BANNER */

.banner {
    background: linear-gradient(90deg, #0D5EA6, #1F6FB2);
    padding: 30px;
    border-radius: 6px;
    color: white;
    min-height: 180px;
}

.banner-title {
    font-size: 36px;
    font-weight: bold;
}

.banner-text {
    font-size: 18px;
    margin-top: 15px;
    line-height: 1.7;
}

/* STAT CARD */

.stat-card {
    background-color: white;
    padding: 30px;
    border-radius: 6px;
    text-align: center;
    min-height: 180px;
    box-shadow: 0px 1px 4px rgba(0,0,0,0.1);
}

.stat-title {
    font-size: 22px;
    font-weight: bold;
    color: #1F232A;
}

.stat-value {
    font-size: 42px;
    font-weight: bold;
    color: #0D5EA6;
    margin-top: 20px;
}

/* QUESTION CARD */

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
}

/* BUTTONS */

.stButton button {
    background-color: #0D5EA6;
    color: white;
    border: none;
    border-radius: 4px;
    height: 42px;
    font-size: 15px;
    font-weight: 600;
}

.stButton button:hover {
    background-color: #084B87;
    color: white;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background-color: white;
}

/* FOOTER */

.footer {
    text-align: center;
    color: gray;
    padding: 30px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div class="top-header">

    <div class="logo-title">
        MIRACLE
    </div>

    <div class="logo-subtitle">
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
- Watermark columns
"""
            },

            {
                "question": "Difference between DELETE and TRUNCATE?",
                "answer": """
DELETE:
Removes rows one by one.

TRUNCATE:
Removes all rows quickly and resets identity.
"""
            }

        ],

        "Microsoft Fabric": [

            {
                "question": "What is OneLake?",
                "answer": """
OneLake is unified storage in Microsoft Fabric.
"""
            }

        ]
    },

    "Power BI Developer": {

        "DAX": [

            {
                "question": "What is CALCULATE in DAX?",
                "answer": """
CALCULATE modifies filter context.
"""
            }

        ]
    }
}

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("⚙ Recruitment Setup")

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
# SEARCH
# =====================================================

search = st.text_input(
    "Search Questions",
    placeholder="Search by Question Keyword..."
)

# =====================================================
# TITLE
# =====================================================

st.markdown(f"""
<h2 style='color:#0D5EA6; margin-top:30px;'>
📘 {role} → {technology} Interview Questions
</h2>
""", unsafe_allow_html=True)

questions = question_bank[role][technology]

# =====================================================
# QUESTIONS
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

        col1, col2 = st.columns([1, 4])

        with col1:

            if st.button(
                f"Show Answer",
                key=f"btn_{idx}"
            ):
                st.success(item["answer"])

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
