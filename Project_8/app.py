import os
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings

loader = TextLoader('sample.txt')
documents = loader.load()
print(len(documents))
text_splitter = CharacterTextSplitter (chunk_size=200,chunk_overlap=0)

texts= text_splitter.split_documents(documents)
print(len(texts))
#print(texts)


os.environ["OPENAI_API_KEY"] = "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"
embeddings=OpenAIEmbeddings()
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma.from_documents(texts, embeddings)
db._collection.get(include=['embeddings'])
retriever = db.as_retriever(search_kwargs={"k": 2})
#print(retriever)
docs = retriever.get_relevant_documents("What is the capital of india?")
print(docs)
docs = retriever.get_relevant_documents("What is the currency india?")
print(docs)