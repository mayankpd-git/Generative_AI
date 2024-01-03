from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
import pandas as pd

embeddings = OpenAIEmbeddings(openai_api_key='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')

df  = {'words':['Apple','Mango','Banana','car','scooter','house']}
df['embedding'] = df['words'].apply(lambda x: embeddings.embed_query(x))
df.to_csv('word_embedding.csv')
new_df = pd.read_csv('word_embedding.csv')
print(new_df)