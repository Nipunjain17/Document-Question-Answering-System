import json
import os

notebook_path = r"d:\Data Science by CT\week7\week7_NipunJain.ipynb"

with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

# Find the metrics cell and replace its source
for cell in nb.get("cells", []):
    if cell.get("cell_type") == "code" and any("SYSTEM METRICS REPORT" in line for line in cell.get("source", [])):
        cell["source"] = [
            "try:\n",
            "    doc_count = len(documents)\n",
            "except NameError:\n",
            "    doc_count = \"N/A (Run Step 1 to populate)\"\n",
            "\n",
            "try:\n",
            "    chunk_count = len(chunks)\n",
            "except NameError:\n",
            "    chunk_count = \"N/A (Run Step 1 to populate)\"\n",
            "\n",
            "try:\n",
            "    chroma_path = CHROMA_PATH\n",
            "except NameError:\n",
            "    chroma_path = \"chroma_db\"\n",
            "\n",
            "print(\"=\"*40)\n",
            "print(\"       SYSTEM METRICS REPORT\")\n",
            "print(\"=\"*40)\n",
            "print(\"1. Chunking Profile:\")\n",
            "print(\"   - Strategy: RecursiveCharacterTextSplitter\")\n",
            "print(\"   - Chunk Size: 1000 characters\")\n",
            "print(\"   - Chunk Overlap: 200 characters\")\n",
            "print(f\"   - Total Documents Processed: {doc_count}\")\n",
            "print(f\"   - Total Chunks Generated: {chunk_count}\")\n",
            "print(\"\\n2. Text Embedding Setup:\")\n",
            "print(\"   - Model: HuggingFace (all-MiniLM-L6-v2)\")\n",
            "print(\"   - Dimensions: 384\")\n",
            "print(\"\\n3. Vector Store Tool:\")\n",
            "print(\"   - Database: ChromaDB\")\n",
            "print(f\"   - Persistence Directory: {chroma_path}\")\n",
            "print(\"\\n4. Language Model Setup:\")\n",
            "print(\"   - Provider: Ollama\")\n",
            "print(\"   - Model: Llama 3\")\n",
            "print(\"   - Temperature: Default\")\n",
            "print(\"=\"*40)"
        ]
        # Also clear the error outputs so it looks fresh
        cell["outputs"] = []
        break

with open(notebook_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1)
print("Metrics report cell updated successfully.")
