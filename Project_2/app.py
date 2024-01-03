import os
os.environ["OPENAI_API_KEY"] = "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"
from langchain.chat_models import HuggingFaceHub
from langchain.schema import HumanMessage, AIMessage, SystemMessage

chat = HuggingFaceHub(temperature=.7, model="gpt-3.5-turbo")

aa = chat([
    SystemMessage(content="you are a scarcastic AI assistant."),
    HumanMessage(content="please answer in 30 words: How can i learn cycling")
]
)
print(aa)