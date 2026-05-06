import streamlit as st

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Miracle Data Practices",
    page_icon="🚀",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

/* Main App */

.stApp {
    background-color: #0E1117;
    color: white;
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background-color: #1E1E2F;
}

/* Buttons */

.stButton button {
    width: 100%;
    border-radius: 10px;
    height: 45px;
    font-size: 16px;
    font-weight: bold;
    background-color: #1F4E79;
    color: white;
    border: none;
}

.stButton button:hover {
    background-color: #2E6EA6;
    color: white;
}

/* Question Cards */

.question-card {
    background-color: #1E1E2F;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
    border: 1px solid #2E2E3E;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.3);
}

/* Question Title */

.question-title {
    color: #4DA3FF;
    font-size: 22px;
    font-weight: bold;
}

/* Question Text */

.question-text {
    color: white;
    font-size: 18px;
    margin-top: 10px;
}

/* Header */

.main-title {
    text-align: center;
    color: #4DA3FF;
    font-size: 52px;
    font-weight: bold;
}

.sub-title {
    text-align: center;
    color: #CFCFCF;
    font-size: 32px;
    margin-top: 10px;
}

.caption-text {
    text-align: center;
    color: white;
    font-size: 18px;
    margin-top: 10px;
    margin-bottom: 30px;
}

/* Footer */

.footer {
    text-align: center;
    color: gray;
    padding: 20px;
    margin-top: 30px;
}

/* Success Message */

.stSuccess {
    border-radius: 10px;
}

/* Checkbox */

.stCheckbox label {
    color: white !important;
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.markdown("""
<div class="main-title">
🚀 Miracle Data Practices
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="sub-title">
Recruitment Interview Portal
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="caption-text">
Interview Question Assistant for Data Engineers & Power BI Developers
</div>
""", unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------
# QUESTION BANK
# ---------------------------------------------------

question_bank = {

    "Data Engineer": {

        "SQL": [

            {
                "question": "Explain Incremental Loading.",
                "answer": """
Incremental loading loads only new or modified records instead of full load.

Methods:
- Timestamp
- CDC
- Watermark column
"""
            },

            {
                "question": "What are Window Functions?",
                "answer": """
Window functions perform calculations across related rows.

Examples:
- ROW_NUMBER()
- RANK()
- LEAD()
- LAG()
"""
            },

            {
                "question": "Difference between DELETE and TRUNCATE?",
                "answer": """
DELETE:
- Removes rows one by one
- Can use WHERE clause

TRUNCATE:
- Removes all rows quickly
- Resets identity
"""
            }

        ],

        "Azure Data Factory": [

            {
                "question": "What is Integration Runtime?",
                "answer": """
Integration Runtime is the compute infrastructure used by Azure Data Factory.
"""
            },

            {
                "question": "Explain Copy Activity.",
                "answer": """
Copy Activity is used to transfer data from source to destination.
"""
            },

            {
                "question": "What are Linked Services?",
                "answer": """
Linked Services are connection configurations used to connect external systems.
"""
            }

        ],

        "Microsoft Fabric": [

            {
                "question": "Explain Medallion Architecture.",
                "answer": """
Bronze Layer:
Raw data

Silver Layer:
Cleaned and transformed data

Gold Layer:
Business-ready data
"""
            },

            {
                "question": "What is OneLake?",
                "answer": """
OneLake is Microsoft Fabric's unified data lake storage.
"""
            },

            {
                "question": "What is a Lakehouse?",
                "answer": """
Lakehouse combines Data Lake and Data Warehouse capabilities.
"""
            }

        ],

        "PySpark": [

            {
                "question": "What is Lazy Evaluation?",
                "answer": """
Transformations execute only when an action is triggered.
"""
            },

            {
                "question": "Difference between Transformation and Action?",
                "answer": """
Transformation:
Returns a new dataframe.

Action:
Executes computation and returns result.
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
Calculated dynamically during report execution.

Calculated Column:
Stored physically in the model.
"""
            },

            {
                "question": "What is FILTER function?",
                "answer": """
FILTER returns a filtered table based on conditions.
"""
            }

        ],

        "Power Query": [

            {
                "question": "What is Query Folding?",
                "answer": """
Query Folding pushes transformations back to source system for optimization.
"""
            },

            {
                "question": "What is M Language?",
                "answer": """
M Language is used in Power Query for data transformation.
"""
            }

        ],

        "Data Modeling": [

            {
                "question": "What is Star Schema?",
                "answer": """
Star Schema contains:
- Fact Table
- Dimension Tables
"""
            },

            {
                "question": "What is relationship cardinality?",
                "answer": """
Types:
- One-to-One
- One-to-Many
- Many-to-Many
"""
            }

        ],

        "Performance Tuning": [

            {
                "question": "How do you optimize Power BI reports?",
                "answer": """
Methods:
- Reduce visuals
- Optimize DAX
- Use Star Schema
- Remove unused columns
- Enable aggregations
"""
            }

        ]
    }
}

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.header("⚙️ Interview Setup")

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

st.sidebar.divider()

st.sidebar.info(f"""
Role: {role}

Technology: {technology}

Experience: {experience}
""")

# ---------------------------------------------------
# MAIN CONTENT
# ---------------------------------------------------

st.subheader(f"📘 {role} → {technology} Interview Questions")

questions = question_bank[role][technology]

for idx, item in enumerate(questions):

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

    if st.button(
        f"Show Answer {idx + 1}",
        key=f"btn_{idx}"
    ):
        st.success(item['answer'])

    st.checkbox(
        "Question Asked",
        key=f"check_{idx}"
    )

    st.divider()

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("""
<div class="footer">
Developed for Miracle Data Practices Recruitment Team
</div>
""", unsafe_allow_html=True)
