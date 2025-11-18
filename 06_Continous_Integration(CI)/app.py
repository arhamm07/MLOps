import streamlit as st

st.title("Power Calculator")
st.write("Enter a number to calculate its square, cube and fifth power")

number = st.number_input("Enter a number", value=1, step=1)

square = number**2
cube = number**3
fifth_power = number**5

st.write(f"The square of {number} is {square}")
st.write(f"The cube of {number} is {cube}")
st.write(f"The fifth power of {number} is {fifth_power}")