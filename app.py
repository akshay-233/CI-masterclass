import streamlit as st
st.title('Power Calculagtor')
st.write("Enter a number to get it's square,cube and %th power")
n=st.number_input('Enter an integer',value=1,step=1)

square=n**2
cube=n**3
fifer=n**5
st.write(f"The square of number is: {square}")
st.write(f"The cube of number is: {cube}")
st.write(f"The fifth power of number is: {fifer}")