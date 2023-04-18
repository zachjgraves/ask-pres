import streamlit as st
import openai
import pandas as pd
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

MODEL = "gpt-3.5-turbo"
question = []
question = st.text_area("Insert a question")

person = st.selectbox("Pick a person", ["Donald Trump", "Barack Obama", "George W. Bush", "Abraham Lincoln", "George Washington"])

history = [
    {"role": "system",
    "content": "You are a caricature of the president of the United States of America, {}".format(person)
    }
]

response = openai.ChatCompletion.create (
    model = MODEL,
    messages = [
    {"role": "system",
    "content": "Imagine are a caricature of the president of the United States of America, {}".format(person),
    "role": "user",
    "content": "As a caricature of the president of the united states, {}, answer this question in two paragraphs: {}".format(person, question)
    }]
)

answer = response.choices[0]["message"].content

st.caption(answer)
