import streamlit as st

# Header
st.header("🎓 Anurag University - Student Records Management")

# Title
st.title("👋 Welcome to Student Records Management System")

# Subheader
st.subheader("📋 Manage Students Efficiently and Effectively")

# Text
st.text("👤 Hi, I am Harshith Gadwala")

# Horizontal line
st.markdown("---")

# Write
st.write("👋 Hello Harshith")

# Markdown
st.markdown("### 📝 Student Registration Details")
st.markdown("**Please fill in all the fields below**")
st.markdown("*All fields marked with * are required*")

# Divider
st.divider()

# Button
if st.button("📌 Click Me"):
    st.write("✅ Button Clicked!")
    st.success("Operation successful!")
    st.balloons()
else:
    st.write("👆 Button not clicked yet.")

# Text input - Name
name = st.text_input("👤 Enter Your Name:")

if name == "":
    st.warning("⚠️ Name cannot be empty!")
elif not name.isalpha():
    st.error("❌ Invalid input. Please enter only alphabets (no numbers or symbols).")
else:
    st.success(f"✅ Hello, {name}!")

# Text area - Feedback
feedback = st.text_area("💬 Enter Your Feedback")

# Checkbox
if st.checkbox("📜 I agree to the Terms and Conditions"):
    st.write("✅ Thank you for the agreement")

# Radio button - Gender
gender = st.radio("⚧️ Select Your Gender:", ["👨 Male", "👩 Female", "🧑 Other"])
st.write(f"You have selected: {gender}")

# Selectbox - Country
country = st.selectbox("🌍 Select Your Country:", ("🇮🇳 India", "🇦🇪 Dubai"))
st.write(f"You have selected: {country}")

# Multiselect - Skills
skills = st.multiselect(
    "💻 Select Your Skills:",
    ["🐍 Python", "🗄️ SQL", "🤖 ML", "📊 Data Science"]
)

# Slider - Age
age = st.slider("🎂 Select Your Age:", 0, 100, 25)
st.write(f"You are {age} years old.")

# File uploader
uploaded_file = st.file_uploader("📎 Upload Your Document")
if uploaded_file is not None:
    st.success("✅ File uploaded successfully!")
else:
    st.write("📁 No file uploaded yet.")

# Registration Form
with st.form("registration_form"):
    st.markdown("### 📝 Registration Form")
    reg_first = st.text_input("👤 First Name")
    reg_last = st.text_input("👤 Last Name")
    reg_email = st.text_input("📧 Email Address")
    reg_pwd = st.text_input("🔒 Password", type="password")
    reg_pwd2 = st.text_input("🔒 Confirm Password", type="password")
    register = st.form_submit_button("🚀 Register")

    if register:
        if not reg_first or not reg_last or not reg_email or not reg_pwd:
            st.error("❌ All fields are required.")
        elif reg_pwd != reg_pwd2:
            st.error("❌ Passwords do not match.")
        else:
            st.success(f"🎉 Registration successful! Welcome, {reg_first} {reg_last}!")
            st.balloons()

# Login Form
with st.form("login_form"):
    st.markdown("### 🔐 Login Form")
    user = st.text_input("📧 Username")
    pwd = st.text_input("🔒 Password", type="password")
    submit = st.form_submit_button("🔐 Login")

    if submit:
        if not user or not pwd:
            st.error("❌ Please fill in all fields.")
        else:
            st.success(f"✅ Logged in successfully as {user}!")

# Columns
col1, col2, col3 = st.columns(3)
with col1:
    st.header("🏫 Campus")
    st.write("Main Campus, Hyderabad")
with col2:
    st.header("📞 Support")
    st.write("24/7 Help Desk Available")
with col3:
    st.header("📬 Contact")
    st.write("info@anurag.edu")

# Container
container = st.container()
container.write("📦 Inside Container")
container.button("📌 Click")

# Table
data = {
    '👤 Name': ['Ravi', 'Harshith', 'Rohit'],
    '🎂 Age': [21, 20, 20],
    '📚 Course': ['M.Tech', 'B.Tech', 'BBA']
}
st.table(data)

# Sidebar
st.sidebar.title("📚 Menu")
option = st.sidebar.selectbox(
    "Choose Page:",
    ["🏠 Home", "📝 About", "📬 Contact"]
)
st.sidebar.write(f"You selected: {option}")