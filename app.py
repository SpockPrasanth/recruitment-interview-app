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

/* Main App */

.stApp {
    background-color: #F4F5F7;
    font-family: 'Segoe UI', sans-serif;
}

/* Header */

.main-header {
    background-color: #1F232A;
    padding: 20px 40px;
    border-radius: 5px;
    margin-bottom: 25px;
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

/* Welcome Banner */

.banner {
    background: linear-gradient(90deg, #0D5EA6, #1F6FB2);
    padding: 30px;
    border-radius: 8px;
    color: white;
    margin-bottom: 25px;
}

.banner-title {
    font-size: 32px;
    font-weight: bold;
}

.banner-text {
    font-size: 18px;
    margin-top: 10px;
}

/* Question Card */

.question-card {
    background-color: white;
    padding: 25px;
    border-radius: 8px;
    margin-bottom: 20px;
    border-left: 6px solid #0D5EA6;
    box-shadow: 0px 1px 4px rgba(0,0,0,0.08);
}

/* Buttons */

.stButton button {
    background-color: #0D5EA6;
    color: white;
    border: none;
    border-radius: 5px;
    height: 40px;
    font-size: 15px;
    font-weight: 600;
}

.stButton button:hover {
    background-color: #084B87;
    color: white;
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background-color: white;
}

/* Footer */

.footer {
    text-align: center;
    color: gray;
    padding: 20px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div class="main-header">

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

left, right = st.columns([3, 1])

with left:

    st.markdown("""
    <div class="banner">

        <div class="banner-title">
            Welcome to Miracle Recruitment Portal!
        </div>

        <div class="banner-text">
            Interview Question Assistant for Data Engineers,
            Power BI Developers, Fabric Engineers,
            and Azure Data Professionals.
        </div>

    </div>
    """, unsafe_allow_html=True)

with right:

    st.metric(
        label="Total Questions",
        value="120+"
    )

# =====================================================
# HARDCODED QUESTION BANK
# =====================================================

question_bank = {

    "Data Engineer": {

        "SQL": [

            {
                "question": "What is the difference between DELETE, TRUNCATE, and DROP?",
                "answer": """
DELETE removes rows and can be rolled back.

TRUNCATE removes all rows and resets identity.

DROP removes the entire table structure.
"""
            },

            {
                "question": "Explain window functions in SQL.",
                "answer": """
Window functions perform calculations across rows related to the current row.

Examples:
ROW_NUMBER()
RANK()
DENSE_RANK()
LEAD()
LAG()
"""
            },

            {
                "question": "What is incremental loading?",
                "answer": """
Incremental loading loads only new or changed records instead of full load.

Usually implemented using:
- Timestamp
- CDC
- Watermark columns
"""
            }

        ],

        "ADF": [

            {
                "question": "What is Integration Runtime in ADF?",
                "answer": """
Integration Runtime is the compute infrastructure used by Azure Data Factory
to move and transform data.
"""
            },

            {
                "question": "Explain Copy Activity.",
                "answer": """
Copy Activity is used to move data from source to destination.
"""
            }

        ],

        "Fabric": [

            {
                "question": "What is Medallion Architecture?",
                "answer": """
Medallion Architecture consists of:
- Bronze Layer
- Silver Layer
- Gold Layer
"""
            },

            {
                "question": "What is OneLake?",
                "answer": """
OneLake is Microsoft Fabric's unified data lake storage.
"""
            }

        ]
    },

    "Power BI Developer": {

        "DAX": [

            {
                "question": "What is CALCULATE function?",
                "answer": """
CALCULATE modifies filter context in DAX.
"""
            },

            {
                "question": "Difference between calculated column and measure?",
                "answer": """
Calculated Column:
Stored physically in model.

Measure:
Calculated dynamically during query execution.
"""
            }

        ],

        "Power Query": [

            {
                "question": "What is query folding?",
                "answer": """
Query folding pushes transformations back to source system.
"""
            }

        ],

        "Data Modeling": [

            {
                "question": "What is star schema?",
                "answer": """
Star schema contains:
- Fact table
- Dimension tables
"""
            }

        ]
    }
}

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.header("⚙ Interview Setup")

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
    ["Fresher", "2-4 Years", "5-8 Years", "10+ Years"]
)

# =====================================================
# SEARCH
# =====================================================

search = st.text_input(
    "Search Questions",
    placeholder="Search by keyword..."
)

# =====================================================
# MAIN SCREEN
# =====================================================

st.markdown(f"""
<h2 style='color:#0D5EA6; margin-top:20px;'>
📘 {role} → {technology} Interview Questions
</h2>
""", unsafe_allow_html=True)

questions = question_bank[role][technology]

for index, item in enumerate(questions):

    if search.lower() in item["question"].lower():

        with st.container():

            st.markdown(
                f"""
                <div class="question-card">

                    <h3 style="color:#0D5EA6;">
                        Question {index + 1}
                    </h3>

                    <p style="font-size:18px; color:#333333;">
                        {item['question']}
                    </p>

                </div>
                """,
                unsafe_allow_html=True
            )

            col1, col2 = st.columns([1, 4])

            with col1:

                if st.button(
                    f"Show Answer",
                    key=index
                ):
                    st.success(item['answer'])

            with col2:

                st.checkbox(
                    "Question Asked",
                    key=f"asked_{index}"
                )

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.markdown("""
<div class="footer">
Developed for Miracle Software Systems Recruitment Team
</div>
""", unsafe_allow_html=True)
