import json

notebook_path = r"d:\Data Science by CT\week7\week7_NipunJain.ipynb"

with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

explanation_content = """### Notebook Architecture & Execution Flow
Below is a detailed explanation of what each section in this notebook accomplishes:

1. **Imports & Setup**: Loads all the essential libraries required for the pipeline, including LangChain components, HuggingFace embeddings, ChromaDB, and Ollama.
2. **Configuration**: Defines the paths for the input documents (`data/`) and the persistent vector database (`chroma_db/`).
3. **Step 1: Data Ingestion**: Loads the raw PDF and Text files from the data directory. It then uses a `RecursiveCharacterTextSplitter` to break down large documents into smaller, overlapping chunks (1000 characters each) to preserve context, and assigns a unique ID to every chunk.
4. **Step 2: Store Embeddings in ChromaDB**: Converts the text chunks into numerical vectors (embeddings) using the `all-MiniLM-L6-v2` model. These vectors are stored persistently in ChromaDB, allowing the system to quickly find semantically similar text during a query.
5. **Step 3: Set Up RAG Query Chain**: Configures the local **Llama 3** model (via Ollama) and ties it together with the ChromaDB retriever. It establishes a strict prompt template forcing the LLM to ground its answers *only* in the retrieved context.
6. **Step 4: Ask Questions**: Tests the pipeline with various dynamic domain questions (e.g., about Databases, Classes, Data Centers). It prints the context-aware answer and explicitly lists the source chunks used to generate it.
7. **Step 5: System Metrics Report**: Dynamically calculates and prints a comprehensive overview of the pipeline's configuration, including chunking profiles, embedding dimensions, and model setups."""

new_cell = {
    "cell_type": "markdown",
    "metadata": {},
    "source": [line + "\n" for line in explanation_content.split("\n")]
}

# Remove the trailing newline from the last string to match standard Jupyter format
if new_cell["source"]:
    new_cell["source"][-1] = new_cell["source"][-1].rstrip("\n")

# Insert right after the first markdown cell (the title cell)
nb["cells"].insert(1, new_cell)

with open(notebook_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1)

print("Explanation cell added successfully.")
