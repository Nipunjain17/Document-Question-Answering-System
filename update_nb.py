import json
import os

notebook_path = r"d:\Data Science by CT\week7\week7_NipunJain.ipynb"

with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

# Find if we already added it to prevent duplicates
already_added = False
for cell in nb.get("cells", []):
    if cell.get("cell_type") == "markdown" and any("System Metrics Report" in line for line in cell.get("source", [])):
        already_added = True
        break

if not already_added:
    new_cell = {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "### Step 5: System Metrics Report"
     ]
    }
    
    new_code_cell = {
     "cell_type": "code",
     "execution_count": None,
     "metadata": {},
     "outputs": [],
     "source": [
      "print(\"=\"*40)\n",
      "print(\"       SYSTEM METRICS REPORT\")\n",
      "print(\"=\"*40)\n",
      "print(\"1. Chunking Profile:\")\n",
      "print(\"   - Strategy: RecursiveCharacterTextSplitter\")\n",
      "print(\"   - Chunk Size: 1000 characters\")\n",
      "print(\"   - Chunk Overlap: 200 characters\")\n",
      "print(f\"   - Total Documents Processed: {len(documents)}\")\n",
      "print(f\"   - Total Chunks Generated: {len(chunks)}\")\n",
      "print(\"\\n2. Text Embedding Setup:\")\n",
      "print(\"   - Model: HuggingFace (all-MiniLM-L6-v2)\")\n",
      "print(\"   - Dimensions: 384\")\n",
      "print(\"\\n3. Vector Store Tool:\")\n",
      "print(\"   - Database: ChromaDB\")\n",
      "print(f\"   - Persistence Directory: {CHROMA_PATH}\")\n",
      "print(\"\\n4. Language Model Setup:\")\n",
      "print(\"   - Provider: Ollama\")\n",
      "print(\"   - Model: Llama 3\")\n",
      "print(\"   - Temperature: Default\")\n",
      "print(\"=\"*40)"
     ]
    }
    
    # Remove the last empty cell if it exists to keep it clean
    if len(nb["cells"]) > 0 and nb["cells"][-1]["cell_type"] == "code" and not nb["cells"][-1]["source"]:
        nb["cells"].pop()

    nb["cells"].append(new_cell)
    nb["cells"].append(new_code_cell)
    
    with open(notebook_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1)
    print("Metrics report cell added successfully.")
else:
    print("Metrics report cell already exists.")
