import os

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

chat = ChatOpenAI(temperature=0.7, model='gpt-3.5-turbo', openai_api_key='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')

chat ([
    SystemMessage(content = "You are a scarcastic AI"),
    HumanMessage(content = "Please answer in 30 words, How can i drive a car")
]
)

our_conv = chat ([
    SystemMessage(content = "You are a scarcastic AI"),
    HumanMessage(content = "Please answer in 30 words, How can i drive a car"),
    AIMessage(content = "I cant drive yet, But my dad can drive"),
    HumanMessage(content = "Teach me a cycle")
]
)

print(our_conv)