import streamlit as st
import pandas
st.set_page_config(layout="wide")
col1,col2=st.columns(2)

with col1:
    st.image("images/new.jpeg",width=400)
with col2:
    st.title("Aby George Mathew")
    content=""" I am Aby George Mathew.I am a developer in python.....
    I’m an aspiring programmer currently learning Python, passionate about building real-world applications and improving my problem-solving skills.
Though I’ve faced challenges with programming logic and critical thinking, I’m committed to growing every day through consistent learning, structured practice, and curiosity.
I believe in learning by doing — whether it’s through LeetCode problems, coding challenges, or simple Streamlit apps.
I may be at the beginning of my coding journey, but I’m driven, resilient, and focused on becoming a confident and capable developer. I don't give up — I level up.

"""
    st.subheader(content)
    st.header("Below you can find some of the apps I have built in python")

col3,empty_col,col4=st.columns([1.5,0.5,1.5])
df=pandas.read_csv("data.csv",sep=";")

with col3:
    for index ,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])

        st.image(f"images/"+row["image"])
        st.write("https://github.com/abygmat/webapp/pulls")

with col4:
    for index ,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/"+row["image"])
        st.write("https://github.com/abygmat/webapp/pulls")




