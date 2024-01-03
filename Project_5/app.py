import os
os. environ['OPENAI_API_KEY'] = "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"
from langchain.llms import OpenAI
llm = OpenAI(model_name='text-davinci-003')
our_prompt = """
I love trips. I have been to many countries.
I plan to visit few more soon.
can you create a post for tweet in 10 words for the above.
"""
print(our_prompt)
print(llm(our_prompt))