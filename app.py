import os
from config import openai_api_key

import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.agents.agent_toolkits import (
    create_vectorstore_agent, VectorStoreToolkit, VectorStoreInfo)

# Set API key for OpenAI
os.environ["OPENAI_API_KEY"] = openai_api_key


# App framework
st.title('LangChain Document Response Generator')
user_prompt = st.text_input('Enter your prompt here:')

# Set LLMs and embeddings
llm_chat = ChatOpenAI(temperature=0.9, max_tokens=150,
                      model='gpt-3.5-turbo-0613', client='')

embeddings = OpenAIEmbeddings(client='')

# Load and split the pdf
pdfLoader = PyPDFLoader(
    'How_Conversational_Business_Can_Help_You_Get_and_Stay_Closer_to_Customers.pdf')
pages = pdfLoader.load_and_split()

# Load document pages into Chroma
store = Chroma.from_documents(
    pages, embedding=embeddings, collection_name='sample')

# Create vectorstore info object
vectorstore_info = VectorStoreInfo(
    name='vectorStoreTool',
    description='a sample vectorstore',
    vectorstore=store,
)


# Convert vectorstore info object to agent toolkit
toolkit = VectorStoreToolkit(vectorstore_info=vectorstore_info, llm=llm_chat
                             )
# Create the agent executor
PREFIX = """You are an agent designed to answer questions about sets of documents.
You have access to tools for interacting with the documents, and the inputs to the tools are questions.
"""
agent_executor = create_vectorstore_agent(
    llm=llm_chat, toolkit=toolkit, prefix=PREFIX, verbose=True)

# Check Streamlit input
if user_prompt:
    # Generate LLM response
    try:
        response = agent_executor.run(user_prompt)
        st.write(response)
    except Exception as e:
        st.write('It looks like you entered an invalid prompt. Please try again.')
        print(e)

    with st.expander('Document Similarity Search'):
        # Find relevant pages
        search = store.similarity_search_with_score(user_prompt)

        # Display results
        st.write(search[0][0].page_content)
