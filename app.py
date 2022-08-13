import streamlit as st
import speech_regcognition as sr
from pythainlp import sent_tokenize, word_tokenize

st.title("🗣💬 to tsl")
st.subheader("Translating Thai speech to Thai Sign Language")

@st.cache
def rec():
  st.text_input("Search here", value="", max_chars=None, disabled=False)
  txt=word_tokenize(value)
  words={
    "ฉัน":"https://www.engdict.com/vocab/?q=I",
    "ชื่อ":"https://th.theasianparent.com/hit-trendy-baby-name",
    "อะไร":"https://www.yuvabadhanafoundation.org/th/%E0%B8%82%E0%B9%88%E0%B8%B2%E0%B8%A7%E0%B8%AA%E0%B8%B2%E0%B8%A3/%E0%B8%9A%E0%B8%97%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%97%E0%B8%B1%E0%B9%88%E0%B8%A7%E0%B9%84%E0%B8%9B/%E0%B9%81%E0%B8%99%E0%B8%B0%E0%B9%81%E0%B8%99%E0%B8%A7-%E0%B8%A7%E0%B8%B1%E0%B8%A2%E0%B8%A3%E0%B8%B8%E0%B9%88%E0%B8%99-%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%80%E0%B8%A3%E0%B8%B5%E0%B8%A2%E0%B8%99/"
    }
  for i in txt:
      print(words[i])
#if st.button_input("record"):


