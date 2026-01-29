import streamlit as st
import mysql.connector
from mysql.connector import Error
import re
import time
from datetime import datetime

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Nexus Auth | Secure Portal",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- ADVANCED CUSTOM STYLING ---
st.markdown("""
    <style>
    /* Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Main Container Glassmorphism */
    .stApp {
        background: radial-gradient(circle at top right, #1e293b, #0f172a);
    }

    /* Card Styling */
    .st-emotion-cache-1r6slb0 {
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 2rem;
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }

    /* Button Styling */
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        height: 3em;
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white;
        border: none;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(99, 102, 241, 0.4);
        border: none;
        color: white;
    }

    /* Metric Styling */
    [data-testid="stMetricValue"] {
        font-weight: 800;
        color: #a855f7;
    }

    /* Success/Error Animations */
    @keyframes slideIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .stAlert {
        animation: slideIn 0.4s ease-out;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DATABASE LOGIC (Kept as per your original structure) ---
DB_HOST, DB_USER, DB_PASSWORD, DB_NAME = "localhost", "root", "H7jai,5ram", "Student_db"

def get_db_connection():
    try:
        return mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
    except Error as e:
        st.error(f"📡 Database Offline: {e}")
        return None

def create_users_table():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) UNIQUE NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        cursor.close()
        conn.close()

def register_user(username, email, password, confirm_password):
    if not username or not email or not password:
        st.warning("⚠️ All fields are required.")
        return False
    if password != confirm_password:
        st.warning("⚠️ Passwords do not match.")
        return False
    
    try:
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
            conn.commit()
            return True
    except Error as e:
        st.error(f"❌ Account creation failed: {e}")
    return False

def login_user(username, password):
    try:
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT username FROM users WHERE username = %s AND password = %s", (username, password))
            result = cursor.fetchone()
            return True if result else False
    except Error: return False

# --- UI COMPONENTS ---
def main():
    create_users_table()
    
    if 'logged_in' not in st.session_state: st.session_state.logged_in = False
    if 'page' not in st.session_state: st.session_state.page = "home"

    # --- AUTHENTICATED VIEW ---
    if st.session_state.logged_in:
        # Sidebar Stats
        with st.sidebar:
            st.markdown("### 🛠️ Nexus Control")
            st.caption(f"Logged in as: **{st.session_state.username}**")
            if st.button("🚪 Sign Out"):
                st.session_state.logged_in = False
                st.rerun()

        # Top Navigation Bar (Attractive Buttons)
        tabs = st.columns(4)
        pages = ["Home", "Profile", "Dashboard", "Settings"]
        icons = ["🏠", "👤", "📊", "⚙️"]
        
        for i, col in enumerate(tabs):
            if col.button(f"{icons[i]} {pages[i]}", key=f"nav_{pages[i]}"):
                st.session_state.page = pages[i].lower()

        st.markdown("---")

        # Page Logic
        if st.session_state.page == "home":
            st.markdown(f"## Welcome back, <span style='color:#a855f7'>{st.session_state.username}</span>! 👋", unsafe_allow_html=True)
            
            # Action Cards
            c1, c2, c3 = st.columns(3)
            with c1:
                st.info("**Learning Hub**\n\nContinue your courses where you left off.")
            with c2:
                st.success("**Project Alpha**\n\nYour recent project is 80% complete.")
            with c3:
                st.warning("**Updates**\n\n3 new security patches available.")
                
            st.markdown("### 📈 Quick Metrics")
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Points", "1,250", "+120")
            m2.metric("Rank", "#4", "↑ 1")
            m3.metric("Level", "15", "Active")
            m4.metric("Tasks", "12", "-2")

        elif st.session_state.page == "dashboard":
            st.markdown("## 📊 Performance Analytics")
            st.line_chart({"Activity": [10, 25, 40, 35, 50, 70, 90]})
            st.bar_chart({"Data": [20, 30, 15, 45, 10]})

        # (Other pages follow same structure...)

    # --- LOGIN / REGISTER VIEW ---
    else:
        col1, col2, col3 = st.columns([1, 4, 1])
        with col2:
            st.markdown("""
                <div style='text-align: center; margin-bottom: 2rem;'>
                    <h1 style='font-size: 3rem; background: -webkit-linear-gradient(#6366f1, #a855f7); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>
                        NEXUS AUTH
                    </h1>
                    <p style='color: #94a3b8;'>Secure entry to your student workspace</p>
                </div>
            """, unsafe_allow_html=True)

            mode = st.tabs(["🔒 Secure Login", "📝 Create Account"])
            
            with mode[0]:
                with st.container():
                    user = st.text_input("Username", key="login_user")
                    pw = st.text_input("Password", type="password", key="login_pw")
                    if st.button("Access Dashboard"):
                        if login_user(user, pw):
                            st.session_state.logged_in = True
                            st.session_state.username = user
                            st.success("Access Granted!")
                            time.sleep(0.5)
                            st.rerun()
                        else:
                            st.error("Invalid Credentials")

            with mode[1]:
                new_user = st.text_input("Username", key="reg_user")
                new_email = st.text_input("Email Address", key="reg_email")
                new_pw = st.text_input("Password", type="password", key="reg_pw")
                conf_pw = st.text_input("Confirm Password", type="password", key="reg_conf")
                if st.button("Initialize Account"):
                    if register_user(new_user, new_email, new_pw, conf_pw):
                        st.success("Account created! Please login.")
    
    # Simple Footer
    st.markdown("<br><br><div style='text-align:center; color:#64748b; font-size: 0.8rem;'>Nexus Secure v2.0 • 2026</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()