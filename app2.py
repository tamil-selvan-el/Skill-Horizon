'''import google.generativeai as genai
import os

#config
genai.configure(api_key="AIzaSyCSfMABLQ2kHa9_m3YdiITesLIF0b6guXU")

#model
model_sh = genai.GenerativeModel("gemini-1.5-flash")

#convo
reply = model_sh.generate_content("who is Elon Musk?")

#reply
print(reply.text)
'''



import google.generativeai as genai
from IPython.display import Markdown

genai.configure(api_key="AIzaSyCSfMABLQ2kHa9_m3YdiITesLIF0b6guXU")


#markdown
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello"},
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    ]
)
response = chat.send_message(input())
print(response.text)

