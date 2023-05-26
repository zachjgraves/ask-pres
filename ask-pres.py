import streamlit as st
import openai
import pandas as pd
import os
from PIL import Image

openai.api_key = os.environ["OPENAI_API_KEY"]

st.title("Ask a President")

image = Image.open('header.jpg')
st.image(image, caption='Photo by Jean Beller on Unsplash')

question = st.text_area("Insert a question")

person = st.selectbox("Pick a person", ["Joe Biden", "Donald Trump", "Barack Obama", "George W. Bush", "Abraham Lincoln", "George Washington"])

if st.button("Submit"):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Imagine you are a caricature of the president of the United States, {}, answer this question in two paragraphs as if you were a stand-up comedian: {}?".format(person, question),
        max_tokens=500
    )

    answer = response.choices[0].text
    st.caption(answer)

