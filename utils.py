from typing import List

from chainlit.types import AskFileResponse
from langchain.document_loaders import TextLoader, PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
import chainlit as cl

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
embeddings = OpenAIEmbeddings()


def process_file(file: AskFileResponse) -> List[Document]:
    import tempfile
    if file.type == "text/plain":
        Loader = TextLoader
    elif file.type == "application/pdf":
        Loader = PyPDFLoader

    with tempfile.NamedTemporaryFile(delete=False) as tempfile:
        tempfile.write(file.content)
        loader = Loader(tempfile.name)
        documents = loader.load()
        docs = text_splitter.split_documents(documents)
        for i, doc in enumerate(docs):
            doc.metadata["source"] = f"source_{i}"
        return docs


from llama_index import download_loader

DadJokesReader = download_loader("DadJokesReader")

loader = DadJokesReader()


# Convert document into Chroma vector database
# Hint: Use cl.AskFileMessage() to ask for a file input
def get_docsearch(file: AskFileResponse) -> Chroma:
    # docs = process_file(file)
    docs = loader.load_data()
    # Save data in the user session
    cl.user_session.set("docs", docs)
    docsearch = Chroma.from_documents(
        docs, embeddings
    )
    return docsearch
