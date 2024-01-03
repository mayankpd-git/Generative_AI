import os
os. environ['OPENAI_API_KEY'] = "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"
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain import FewShotPromptTemplate
llm = OpenAI(model_name="gpt-3.5-turbo-instruct")
examples = [
    {
        "query": "What is a mobile?",
        "answer": "A mobile is a magical device that fits in your pocket, like a mini-enchanted playground. It has games, videos, and talking pictures, but be careful, it can turn grown-ups into screen-time monsters too!"
    }, {
        "query": "What are your dreams?",
        "answer": "My dreams are like colorful adventures, where I become a superhero and save the day! I dream of giggles, ice cream parties, and having a pet dragon named Sparkles.."
    }
]
example_template = """
Question: {query}
Response: {answer}
"""
example_prompt = PromptTemplate(
    input_variables=["query", "answer"],
    template=example_template
)
prefix = """You are a 5 year old girl, who is very funny,mischievous and sweet: 
Here are some examples: 
"""

suffix = """
Question: {userInput}
Response: """

few_shot_prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix=prefix,
    suffix=suffix,
    input_variables=["userInput"],
    example_separator="\n\n"
)
query = "What is a house?"

print(few_shot_prompt_template.format(userInput=query))
print(llm(few_shot_prompt_template.format(userInput=query)))