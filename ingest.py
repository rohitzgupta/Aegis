from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

import os
import shutil

# ==========================================================
# CONFIG
# ==========================================================

DOCS_PATH = "docs"
VECTOR_DB_PATH = "./vectordb"

# ==========================================================
# LOAD DOCUMENTS
# ==========================================================

all_docs = []

for root, dirs, files in os.walk(DOCS_PATH):

    for file in files:

        if file.startswith("~$"):
            continue

        if file.startswith("."):
            continue

        if file.lower().endswith((".txt", ".md")):

            filepath = os.path.join(root, file)

            print(f"Loading: {filepath}")

            loader = TextLoader(
                filepath,
                encoding="utf-8"
            )

            docs = loader.load()

            for doc in docs:

                doc.metadata["filename"] = file
                doc.metadata["folder"] = os.path.basename(root)
                doc.metadata["filepath"] = filepath

            all_docs.extend(docs)

print(f"\nDocuments loaded: {len(all_docs)}")

if len(all_docs) == 0:
    raise Exception(
        "No .txt or .md files found under docs/"
    )

# ==========================================================
# CHUNKING
# ==========================================================

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(all_docs)

print(f"Chunks created: {len(chunks)}")

if len(chunks) == 0:
    raise Exception(
        "No chunks created."
    )

# ==========================================================
# REBUILD VECTOR DB
# ==========================================================

if os.path.exists(VECTOR_DB_PATH):
    shutil.rmtree(VECTOR_DB_PATH)

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=VECTOR_DB_PATH
)

print("\nVector DB created successfully.")

# ==========================================================
# SUMMARY
# ==========================================================

folders = {}

for doc in all_docs:

    folder = doc.metadata["folder"]

    folders[folder] = folders.get(folder, 0) + 1

print("\nIndexed Documents:")

for folder, count in sorted(folders.items()):

    print(f"{folder}: {count}")