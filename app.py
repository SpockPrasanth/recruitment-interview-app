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

.main {
    background-color: #F5F7FA;
}

.stButton button {
    width: 100%;
    border-radius: 10px;
    height: 45px;
    font-size: 16px;
    font-weight: bold;
}

.question-card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
}

.sidebar .sidebar-content {
    background-color: #FFFFFF;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER / BRANDING
# ---------------------------------------------------

st.markdown("""
<h1 style='text-align: center; color: #1F4E79;'>
🚀 Miracle Data Practices
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h3 style='text-align: center; color: gray;'>
Recruitment Interview Portal
</h3>
""", unsafe_allow_html=True)

st.markdown("""
<p style='text-align: center; font-size:18px;'>
Interview Question Assistant for Data Engineers & Power BI Developers
</p>
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
Incremental loading loads only new or modified records instead of loading full data.

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
- Logged operation

TRUNCATE:
- Removes all rows
- Faster
- Resets identity
"""
            }

        ],

        "Azure Data Factory": [

            {
                "question": "What is Integration Runtime?",
                "answer": """
Integration Runtime is the compute infrastructure used by ADF to move and transform data.
"""
            },

            {
                "question": "Explain Copy Activity.",
                "answer": """
Copy Activity is used to transfer data between source and destination systems.
"""
            },

            {
                "question": "What are Linked Services?",
                "answer": """
Linked Services are connection strings used to connect external systems in ADF.
"""
            }

        ],

        "Microsoft Fabric": [

            {
                "question": "Explain Medallion Architecture.",
                "answer": """
Medallion Architecture consists of:
- Bronze Layer → Raw Data
- Silver Layer → Cleansed Data
- Gold Layer → Business Ready Data
"""
            },

            {
                "question": "What is OneLake?",
                "answer": """
OneLake is Microsoft Fabric’s unified data lake storage.
"""
            },

            {
                "question": "What is a Lakehouse?",
                "answer": """
Lakehouse combines features of Data Lake and Data Warehouse.
"""
            }

        ],

        "PySpark": [

            {
                "question": "What is lazy evaluation in PySpark?",
                "answer": """
PySpark transformations are evaluated only when an action is triggered.
"""
            },

            {
                "question": "Difference between transformation and action?",
                "answer": """
Transformation:
Returns new dataframe.

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
Stored physically in model.
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
M Language is used in Power Query Editor for transformations.
"""
            }

        ],

        "Data Modeling": [

            {
                "question": "What is Star Schema?",
                "answer": """
Star Schema contains:
- Fact table
- Dimension tables
"""
            },

            {
                "question": "What is relationship cardinality?",
                "answer": """
Types:
- One to One
- One to Many
- Many to Many
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
- Use star schema
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
            <h4>Question {idx + 1}</h4>
            <p style='font-size:17px;'>
            {item['question']}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        f"Show Answer {idx + 1}",
        key=f"answer_{idx}"
    ):
        st.success(item['answer'])

    st.checkbox(
        "Question Asked",
        key=f"asked_{idx}"
    )

    st.divider()

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("""
<div style='text-align:center; color:gray; padding:20px;'>
Developed for Miracle Data Practices Recruitment Team
</div>
""", unsafe_allow_html=True)
