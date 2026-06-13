from tempfile import NamedTemporaryFile, template

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os


    


def main():
    # Load the PDF document
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

   

    # Split the document into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)

    # Create embeddings for the chunks
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    print("Vector store created.")

    # Initialize the ChatGroq model
    llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7, api_key=groq_api_key)

    template = """You are a powerful ai assistant that can only answer questions
based on the given context. If the question is not related to context say not
answerable. Always use the following format to answer the question.
Also give a short summary of the context before answering the question, and always be relevant
to the question and the context.
Context: {context}
Question: {question}
Answer:"""

    prompt = PromptTemplate(input_variables=["context", "question"], template=template)
    chain = prompt | llm | StrOutputParser()

    # chat loop
    while True:
        query = input("Enter your query (or 'exit' to quit): ")
        if query.lower() == 'exit':
            break

        # Retrieve relevant chunks from the vector store/semantic search
        relevant_chunks = vectorstore.similarity_search(query, k=5)

        # Generate a response using ChatGroq
        response = chain.invoke({"context": relevant_chunks, "question": query})

        print("Response:", response)

if __name__ == "__main__":
    main()

