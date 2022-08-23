import streamlit as st
import streamlit.components.v1 as components
from pythaiasr import asr
#import speech_regcognition as sr
#from pythainlp import sent_tokenize, word_tokenize

header=st.container()
dataset=st.container()
features=st.container()
modelTraining=st.container()

with header:
  st.title("🗣💬 to tsl")
  st.subheader("Translating Thai speech to Thai Sign Language")


with features:
  col1, col2 = st.columns([3,1])
  with col1:
    input_txt=st.text_input("Search here", value="", max_chars=None, disabled=False)
  with col2:
    if st.button("record"):
      with st.spinner(text='Recording'):
        time.sleep(0)
        sound.record()
      st.success("Done!")
  
#with modelTraining:
#@st.cache
#if st.text_input("Search here", value="", max_chars=None, disabled=False):
  #txt=word_tokenize(value)
  #words={
    #"ฉัน":"https://www.engdict.com/vocab/?q=I",
    #"ชื่อ":"https://th.theasianparent.com/hit-trendy-baby-name",
    #"อะไร":"https://www.yuvabadhanafoundation.org/th/%E0%B8%82%E0%B9%88%E0%B8%B2%E0%B8%A7%E0%B8%AA%E0%B8%B2%E0%B8%A3/%E0%B8%9A%E0%B8%97%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%97%E0%B8%B1%E0%B9%88%E0%B8%A7%E0%B9%84%E0%B8%9B/%E0%B9%81%E0%B8%99%E0%B8%B0%E0%B9%81%E0%B8%99%E0%B8%A7-%E0%B8%A7%E0%B8%B1%E0%B8%A2%E0%B8%A3%E0%B8%B8%E0%B9%88%E0%B8%99-%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%80%E0%B8%A3%E0%B8%B5%E0%B8%A2%E0%B8%99/"
    #}
  #for i in txt:
      #print(words[i])
#st.button_input("record")



