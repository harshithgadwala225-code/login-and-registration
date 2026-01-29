import streamlit as st

#header.
st.header("Anurag university Student Records Management")
#title of the app

st.title("welceome to student records management system")
#subheader of the app
st.subheader("Mang student efficiently and effectively")

#text method to display information 

st.text("Hi,I am Harshith gadwala")

#horizontal line

st.markdown("----------------------------")

#write method--allows to write something

st.write("hello Harshith")
st.write(123456)
st.write(1,2,3,4,5)

# st.write("name""Harshith","role":"student")
st.markdown("### this is markdown")
st.markdown("**Bold text**")
st.markdown("*Italic*")
st.markdown("-item 1\n item 2-")



st.markdown("<h3 style=color:red>RED TEXT </h3>",unsafe_allow_html=True)


st.code("""
        def add(a,b):
            return a+b
        """,language='python')

#To create latex describe the math expressions
st.latex(r''' a^2 + b^2 = c^2 ''')

# Divider method to separate sections
st.divider()
#button method to create a button
if st.button("Click me"):
  st.write("Button Clicked!")
  st.success("Operation successful!")
  st.balloons()
else:
  st.write("BUtton not clicked yet.")
  st.error("connection error!")

#text input method to get user input
name = st.text_input("Enter your name:")

#show the input if number give a error text
if name == "":
  st.warning("Name cannot be empty !"
             )
elif not name.isalpha():
  st.error("Invalid input X Please enter only alphabets (no numbers or symbols).")

else:
  st.success(f"Hello, {name}!")

# To add some address,comments,description,feadback
feedback = st.text_area("Enter your feedback")

#To add the chekbox 
if st.checkbox("I agree to the terms and conditions"):
  st.write("Thank you from the agreement")

#To add the radio button
gender = st.radio("Select your gender :",{"Male","Female","Other"})
st.write(f"You have selected: {gender}")

#To create the select box
country = st.selectbox("Select your country:",("India","Dubai"))
st.write(f"You have selected {country}")
#To select multple options
skills = st.multiselect(
  "Select skills",
  ["Python","SQL","ML",""]
)

#silder method to create a slider
age = st.slider("Select your age:",0,100,25)
st.write(f"You are {age} years old.")

#file uploader method to upload files
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  st.success("File uploaded successfully!")
else:
  st.write("No file upload yet.")

#form method to create a form
with st.form("my_form"):   #To come in single so we use "with"
  name = st.text_input("Name")
  age = st.number_input("Age",0,100)
  submit = st.form_submit_button("Submit")

  if submit:
    st.write(name,age)

#To create the form submit button inside the for 

with st.form("login"):
  user = st.text_input("Username")
  pwd = st.text_input("password", type="password")
  submit = st.form_submit_button("Submit")

  if submit:
    st.write(name,age)

  #To create the column method 
  col1,col2,col3 = st.columns(3)
  with col1:
      st.header("column 1:")
      st.write("This is column 1")
  with col2:
    st.header("column 2:")
    st.write("This is column 2")
  with col3:
    st.header("column 3:")
    st.write("This is column 3")
#TO create the container()
container = st.container()
container.write("Inside container")
container.button("Click")

#table method to display data in tabular format
data = {
    'Name': ['Ravi', 'Harshith', 'Rohit'],
    'Age': [21, 20, 20],
    'Course': ['M.Tech', 'B.Tech', 'BBA']
}
st.table(data)

#sidebar method to create 
st.sidebar.title("Menu")
option = st.sidebar.selectbox(
"Choose page",
["Home", "About", "Contact"]
)
st.sidebar.write(f"You selected: {option}")

#To create the success()
#To create error
#to create warning
#to create info

#To create cache_data
@st.cache_data
def load_data():
  return [1, 2, 3, 4]
data = load_data()
st.write(data)

# create a registraction form(first,last,register button,successfull message) check in datqa base and  put it in login form (if matches)
