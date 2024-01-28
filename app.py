import streamlit as st

st.title("計算アプリ")

a = st.number_input("数字1")
b = st.number_input("数字2")

method = st.sidebar.selectbox("計算方法",["+","-","×","÷"])

if method == "+":
  c = a + b
elif method == "-":
  c = a - b
elif method == "×":
  c = a * b
elif method == "÷":
  c = a / b
else:
  pass 

st.title("計算結果")
st.text(c)