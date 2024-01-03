from langchain_experimental.agents import create_pandas_dataframe_agent
import pandas as pd
from langchain.llms import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "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"

def query_agent(data, query):
    df = pd.read_csv(data)
    llm = OpenAI()
    agent = create_pandas_dataframe_agent(llm, df, verbose=True)
    return agent.run(query)