import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("The Best Company")
st.write("To remain available during these difficult times, we have adapted our processes and help you remotely, both for IT assistance and for repairs. We offer you a complete computer repair service or a quick repair of your smartphone, PC, Mac, etc. We can operate remotely in 90% of cases.")
st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

df = pandas.read_csv("data.csv")
with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()}, {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()}, {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()}, {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])


