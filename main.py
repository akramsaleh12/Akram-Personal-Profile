import streamlit as st
import pandas as pd
from datetime import datetime

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Akram Elsayed Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.hero {
    background: linear-gradient(90deg,#0f172a,#1e40af);
    padding:5px;
    border-radius:1px;
    color:white;
}

.skill-card {
    background:#ffffff;
    padding:15px;
    border-radius:10px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.1);
    margin-bottom:10px;
}

.project-card {
    background:#ffffff;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.1);
    margin-bottom:20px;
}

.timeline {
    border-left:3px solid #2563eb;
    padding-left:20px;
    margin-left:10px;
}

.footer {
    text-align:center;
    color:gray;
    margin-top:50px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.title("📌 Navigation")

page = st.sidebar.radio(
    "",
    [
        "🏠 Home",
        "👤 About",
        "🛠 Skills",
        "💼 Experience",
        "🚀 Projects",
        "🏆 Certifications",
        "📧 Contact"
    ]
)

# ==========================================================
# HOME
# ==========================================================

if page == "🏠 Home":

    st.markdown("""
    <div class='hero'>
        <h3>Akram Elsayed</h1>
        <h5>Senior IT Consultant | AI Engineer | Data Scientist</h3>
        <p>35+ Years of Information Technology Experience</p>
        Current Location: Grover Beach, California, USA</p>
        Phone: 805-710-4068
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    col1, col2 = st.columns([1,3])

    with col1:
        st.image(
            # "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
            "ak11.png",
            width=200
        )

    with col2:

        st.markdown("## Welcome")

        st.write("""
        Experienced Information Technology professional with over
        35 years of expertise in:

        - Software Development
        - Python Programming
        - Data Analytics
        - Machine Learning
        - Deep Learning
        - Artificial Intelligence
        - Legacy Modernization
        - COBOL to Python Transformation
        - Streamlit Application Development
        - COBOL CICS App using Mainframe IBM
        - CoolGen App using Mainframe IBM
        - CSP App using Mainframe IBM
        - Databases: VSAM, DB2, MySQL, SQL Server
        """)

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Experience", "35+ Years")
    c2.metric("Projects", "100+")
    c3.metric("Technologies", "20+")
    c4.metric("AI Solutions", "50+")

# ==========================================================
# ABOUT
# ==========================================================

elif page == "👤 About":

    st.title("About Me")

    st.write("""
    I am a seasoned IT professional with more than 35 years of
    experience delivering enterprise-scale software solutions.

    My recent focus areas include:

    - Artificial Intelligence
    - Machine Learning
    - Data Science
    - Data Engineering
    - Python Development
    - Legacy Modernization
    - Streamlit Applications
    - Cloud Technologies
    """)

    st.subheader("Career Highlights")

    highlights = [
        "35+ Years of Professional Experience",
        "Expert in Legacy Modernization",
        "AI-Powered Software Development",
        "Data Science and Machine Learning Specialist",
        "Enterprise Application Architect"
    ]

    for item in highlights:
        st.success(item)

# ==========================================================
# SKILLS
# ==========================================================

elif page == "🛠 Skills":

    st.title("Technical Skills")

    skills = {
        "Python": 95,
        "Machine Learning": 90,
        "Deep Learning": 85,
        "Data Analytics": 95,
        "SQL": 90,
        "Streamlit": 95,
        "COBOL": 90,
        "Cloud Computing": 80,
        "AI Solutions": 90
    }

    for skill, value in skills.items():
        st.write(f"### {skill}")
        st.progress(value)

# ==========================================================
# EXPERIENCE
# ==========================================================

elif page == "💼 Experience":

    st.title("Professional Experience")

    experiences = [

        {
            "period":"2024 - Present",
            "title":"AI Consultant",
            "description":"Building AI-powered applications and modernization solutions."
        },

        {
            "period":"2018 - 2024",
            "title":"Data Science Consultant",
            "description":"Machine learning and analytics projects."
        },

        {
            "period":"2010 - 2018",
            "title":"Senior Software Engineer",
            "description":"Enterprise software development and architecture."
        },

        {
            "period":"1990 - 2010",
            "title":"Software Developer",
            "description":"Design and development of business applications."
        }
    ]

    for exp in experiences:

        st.markdown(
            f"""
            <div class='timeline'>
                <h4>{exp['period']}</h4>
                <b>{exp['title']}</b>
                <p>{exp['description']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# ==========================================================
# PROJECTS
# ==========================================================

elif page == "🚀 Projects":

    st.title("Featured Projects")

    projects = [

        {
            "title":"AI COBOL Modernization",
            "description":"Convert COBOL systems to Python using AI."
        },

        {
            "title":"Customer Segmentation",
            "description":"K-Means clustering dashboard with Streamlit."
        },

        {
            "title":"Diabetes Prediction System",
            "description":"Machine Learning healthcare application."
        },

        {
            "title":"Laptop Price Prediction",
            "description":"Stacking Ensemble with XGBoost, CatBoost and ExtraTrees."
        },

        {
            "title":"Data Analytics Dashboard",
            "description":"Interactive BI dashboards using Python and Streamlit."
        }
    ]

    for project in projects:

        st.markdown(
            f"""
            <div class='project-card'>
                <h3>{project['title']}</h3>
                <p>{project['description']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# ==========================================================
# CERTIFICATIONS
# ==========================================================

elif page == "🏆 Certifications":

    st.title("🏆 Certifications")

    certificates = {
        "Machine Learning with Python": {
            "image": "certificates/Machine_Learning_with_Python.jpeg",
            "verification_url": "https://www.coursera.org/account/accomplishments/verify/3PAVREYMRJF8"
        },

        "Data Analysis with Python": {
            "image": "certificates/Data_Analysis_with_Python.jpeg",
            "verification_url": "https://www.coursera.org/account/accomplishments/verify/ZFABX9X3JJ5N"
        },
        "Python for Data Science, AI & Development": {
            "image": "certificates/Python_for_Data Science_AI Development.jpeg",
            "verification_url": "https://www.coursera.org/account/accomplishments/verify/EZ9RXP4G9SCC"
        },
        "Using Databases with Python": {
            "image": "certificates/Using_Databases_with_Python.jpeg",
            "verification_url": "https://www.coursera.org/account/accomplishments/verify/CCBLNMXNN4YW"
        },
        "Using Python to Access Web Data": {
            "image": "certificates/Using_Python_to_Access_Web_Data.jpeg",
            "verification_url": "https://www.coursera.org/account/accomplishments/verify/EZ9RXP4G9SCC"
        },
        "Python Data Structures": {
            "image": "certificates/Python_Data_Structures.jpeg",
            "verification_url": "https://www.coursera.org/account/accomplishments/verify/WNT66NZQPLX3"
        },
        "Intro to Deep Learning": {
            "image": "certificates/intro_to_deep_learning.PNG",
            "verification_url": "https://www.kaggle.com/learn/certification/akelsayed/intro-to-deep-learning"
        },
        "Intermediate Machine Learning": {
            "image": "certificates/intermediate_machine_learning.PNG",
            "verification_url": "https://www.kaggle.com/learn/certification/akelsayed/intermediate-machine-learning"
        },
        "Intro to Machine Learning": {
            "image": "certificates/intro_to_machine_learning.PNG",
            "verification_url": "https://www.kaggle.com/learn/certification/akelsayed/intro-to-machine-learning"
        }
    }

    for cert_name, cert_data in certificates.items():

        with st.expander(f"📜 {cert_name}"):

            st.image(
                cert_data["image"],
                use_container_width=True
            )

            st.markdown(
                f"🔗 **Verification URL:** [Click to verify]({cert_data['verification_url']})"
            )

# ==========================================================
# CONTACT
# ==========================================================

elif page == "📧 Contact":

    st.title("Contact")

    st.write("### Akram Elsayed")

    st.write("📧 Email: akramelsayed11@gmail.com")
    st.write("🔗 Kaggle: https://www.kaggle.com/akelsayed")
    st.write("🔗 LinkedIn: https://www.linkedin.com/in/akram-elsayed/")
    st.write("💻 GitHub: https://github.com/akramsaleh12")
    st.write("🔗 YouTube: https://www.youtube.com/@learncodingwithak8520")

    st.divider()

    st.subheader("Send a Message")

    with st.form("contact_form"):

        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")

        submit = st.form_submit_button("Send Message")

        if submit:

            st.success(
                f"Thank you {name}. Your message has been received."
            )

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

current_year = datetime.now().year

st.markdown(
    f"""
    <div class='footer'>
        © {current_year} Akram Elsayed | AI Engineer | Data Scientist
    </div>
    """,
    unsafe_allow_html=True
)