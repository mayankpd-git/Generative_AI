# From OpenAI GPT 3.5
# import os
# from langchain.llms import OpenAI
# # Fetch the Open API key from https://platform.openai.com/api-keys
# os.environ["OPENAI_API_KEY"] = "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"
# # there are multiple language models but currently test-davinci-003 is used [egs : code-davinci-003,gpt-3.5-turbo]
# llm = OpenAI(model_name = 'gpt-3.5-turbo')
# query = "What is the currency of India?"
# completion  = llm(query)
# print(completion)



# From Hugging face 
# pip install huggingface_hub

import os
from langchain.llms import HuggingFaceHub

# Get the access token from https://huggingface.co/settings/tokens
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

llm = HuggingFaceHub(repo_id = "google/flan-t5-large")

query = "What is the currency of India?"
completion  = llm(query)
print(query , " : ", completion)

query = "when was it launched?"
completion  = llm(query)
print(query , " : ", completion)