from flask import Flask, render_template, request
import os
from langchain.llms import HuggingFaceHub

app = Flask(__name__)

# Get the access token from https://huggingface.co/settings/tokens
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

llm = HuggingFaceHub(repo_id="google/flan-t5-large")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def generate_answer():
    query = request.form['query']
    completion = llm(query)
    return render_template('index.html', query=query, completion=completion)

if __name__ == '__main__':
    app.run(debug=True)
