from langchain_ollama import OllamaLLM
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

from modules.config import *


def load_vectordb():

    embeddings = OllamaEmbeddings(
        model=EMBEDDING_MODEL
    )

    return Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embeddings
    )


def load_llm():

    return OllamaLLM(
        model=LLM_MODEL
    )


def search_runbooks(
    question,
    db,
    llm
):

    results = db.similarity_search_with_score(
        question,
        k=3
    )

    docs = [
        doc
        for doc, score in results
    ]

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
Use ONLY supplied context.

If answer is unavailable return:

KNOWLEDGE GAP

Context:

{context}

Question:

{question}

Answer:
"""

    answer = llm.invoke(prompt)

    return answer, results