# DBA AI Assistant

![Version](https://img.shields.io/badge/version-v1.0-blue)
![Python](https://img.shields.io/badge/python-3.11+-green)
![License](https://img.shields.io/badge/license-Apache%202.0-orange)


# DBA AI Assistant

AI-powered Aurora PostgreSQL assistant using:

- Ollama
- Qwen 2.5
- ChromaDB
- Nomic Embeddings
- Streamlit

## Features

- Aurora PostgreSQL troubleshooting
- SQL knowledge search
- Inventory lookup
- RAG architecture

## Tech Stack

- Python
- Ollama
- ChromaDB
- Streamlit

## Installation

git clone ...

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

ollama pull qwen2.5:7b
ollama pull nomic-embed-text

python ingest.py

streamlit run app.py

## Screenshots

![Home](screenshots/home.png)

## Disclaimer

This project provides AI-generated recommendations.

Always validate SQL statements, maintenance actions, and operational guidance before executing in production environments.
