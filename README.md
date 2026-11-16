# RefraScan RAG Assistant
A Retrieval-Augmented Generation (RAG) application that allows users to ask questions about the RefraScan research project and receive context-based answers using a locally running Large Language Model (LLM).

## Overview

RefraScan RAG Assistant is a question-and-answer application designed to make information from the RefraScan thesis easier to access and understand.

Instead of relying solely on an LLM's general knowledge, the application retrieves relevant passages from a prepared knowledge base before generating an answer. This helps ground responses in the project's research information.

## Features

- **Knowledge-Based Question Answering** – Ask questions about the RefraScan research project.
- **TF-IDF Retrieval** – Converts knowledge-base text and user queries into numerical representations.
- **Cosine Similarity Matching** – Ranks knowledge-base passages according to their relevance to the user's question.
- **Query Expansion** – Adds related keywords to selected queries to improve retrieval.
- **Local LLM Integration** – Uses Llama 3.2 through Ollama for answer generation.
- **Source Transparency** – Displays retrieved passages and similarity scores alongside generated answers.
- **Context-Grounded Responses** – Uses prompt instructions to restrict answers to the retrieved information.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application development |
| Streamlit | Interactive web interface |
| Scikit-learn | TF-IDF vectorization and cosine similarity |
| Ollama | Local LLM integration |
| Llama 3.2 (3B) | Natural-language answer generation |

## System Architecture

The application consists of four main components:

1. **User Interface (`app.py`)** – Accepts user questions and displays generated answers and retrieved passages.
2. **Retrieval Engine (`rag_engine.py`)** – Loads the knowledge base, processes text into chunks, and retrieves relevant passages using TF-IDF and cosine similarity.
3. **RAG Pipeline (`rag_pipeline.py`)** – Combines retrieved passages with the user's question and sends the prompt to Llama 3.2 through Ollama.
4. **Knowledge Base (`knowledge_base.txt`)** – Contains prepared information about the RefraScan research project.

### How It Works

1. The user submits a question through the Streamlit interface.
2. The retrieval engine processes the question using TF-IDF.
3. Cosine similarity identifies and ranks the most relevant knowledge-base passages.
4. The top five passages are combined and provided as context to the language model.
5. Llama 3.2 generates an answer based on the retrieved context.
6. The application displays the answer, retrieved passages, and their similarity scores.

## Project Structure

```text
RefraScan-RAG-Assistant/
│
├── app.py                 # Streamlit user interface
├── rag_engine.py          # Knowledge-base processing and retrieval
├── rag_pipeline.py        # Retrieval and answer generation pipeline
├── knowledge_base.txt     # RefraScan research knowledge base
│
├── test_ollama.py         # Tests Ollama connectivity and generation
├── test_retriever.py      # Tests knowledge-base retrieval
└── test_rag.py            # Tests the complete RAG pipeline
```

## Installation and Setup

### Prerequisites

- Python 3.9 or later
- Ollama installed
- Llama 3.2 (3B) model downloaded

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd RefraScan-RAG-Assistant
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install streamlit scikit-learn ollama
```

### 4. Download the LLM

Make sure Ollama is installed and download the required model:

```bash
ollama pull llama3.2:3b
```

Ensure the Ollama service is running before starting the application.

### 5. Run the Application

```bash
streamlit run app.py
```

The Streamlit application will provide a local URL that you can open in your browser.

## Testing

The project includes three test scripts for checking individual components and the complete RAG workflow.

| Test File | Description |
|---|---|
| `test_ollama.py` | Checks whether Ollama can generate responses using the selected model. |
| `test_retriever.py` | Tests whether relevant passages are retrieved from the knowledge base. |
| `test_rag.py` | Tests the complete retrieval and answer-generation process. |

Run the tests individually:

```bash
python test_ollama.py
python test_retriever.py
python test_rag.py
```

## Current Limitations

- **Keyword-Based Retrieval:** TF-IDF relies on word and phrase overlap and may struggle with questions that have similar meanings but different wording.
- **No Similarity Threshold:** The retriever returns the top results even when their similarity scores are low.
- **No Conversation History:** Each question is processed independently.
- **Manually Maintained Knowledge Base:** Research updates must also be reflected in `knowledge_base.txt`.
- **No Formal Source Citations:** Retrieved passages are displayed, but they are not linked to specific thesis pages or sections.
- **Prompt-Based Grounding:** Prompt instructions help limit unsupported answers but do not completely eliminate hallucinations.

## Future Improvements

- Integrate semantic embeddings for improved retrieval.
- Implement a minimum similarity threshold.
- Cache the processed knowledge base to reduce repeated initialization.
- Add more structured source references and citations.
- Introduce answer validation to improve response reliability.

---

**Project:** RefraScan RAG Assistant  
**Category:** Retrieval-Augmented Generation (RAG) / AI Application  
**Primary Language:** Python
