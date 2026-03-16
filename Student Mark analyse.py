import streamlit as st

st.title("Student Marks Analyzer")

name = st.text_input("Enter Student Name")

m1 = st.number_input("Maths Marks", 0, 100)
m2 = st.number_input("Physics Marks", 0, 100)
m3 = st.number_input("Chemistry Marks", 0, 100)
m4 = st.number_input("English Marks", 0, 100)
m5 = st.number_input("Computer Marks", 0, 100)

if st.button("Calculate Result"):
    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "Fail"

    st.write("Name:", name)
    st.write("Total Marks:", total)
    st.write("Percentage:", percentage)
    st.write("Grade:", grade)