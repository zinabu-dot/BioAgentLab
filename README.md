# 🔬 BioAgentLab — An LLM-Powered Biomedical Research Assistant

## 🚀 Overview

**BioAgentLab** is an autonomous agent framework powered by large language models (LLMs), designed to extract, synthesize, and validate biomedical insights from both structured and unstructured sources such as PubMed, ClinicalTrials.gov, UniProt, and local literature. It leverages Retrieval-Augmented Generation (RAG) and a modular tool system to answer complex biomedical queries with citations and regulatory context.

---

## 🧠 Key Features

- **Prompt Engineering Framework:**  
  Custom prompt templates and chaining strategies for due diligence, target validation, and regulatory summaries.

- **Agentic Architecture:**  
  Uses an LLM-backed agent loop (LangChain) with memory, tool use, and intermediate reasoning.

- **Multi-Source Knowledge Integration:**  
  - 🔍 **PubMed** (biomedical literature via Entrez API)
  - 🔬 **UniProt** (protein/target data)
  - 📄 **ClinicalTrials.gov** (clinical trial landscape)
  - 🗂️ **Local Literature** (vector search over indexed documents)

- **RAG (Retrieval-Augmented Generation):**  
  Vector search over pre-indexed documents using FAISS and HuggingFace embeddings.

- **Scientific Claim Validation:**  
  Claim–evidence scoring pipeline with confidence thresholds.

---

## 🧱 Architecture

```
┌────────────────────┐
│  User Query (e.g.  │
│ "Is XYZ a valid    │
│  cancer target?")  │
└────────┬───────────┘
         ↓
 ┌────────────────────┐
 │ PromptEngine       │◄─ Customizable templates (target validation, MoA, regulatory)
 └────────┬───────────┘
         ↓
 ┌────────────────────┐
 │ BioAgent (LLM Loop)│
 └────────┬───────────┘
         ↓
 ┌────────────────────────────┐
 │  Tools:                    │
 │  • PubMed Scraper API      │
 │  • UniProt Lookup          │
 │  • ClinicalTrials Query    │
 │  • VectorDB Retriever (RAG)│
 └────────┬───────────────────┘
         ↓
 ┌────────────────────┐
 │ Synthesized Output │ → Rationale, citations, confidence score
 └────────────────────┘
```

---

## 📁 Repo Structure

```
BioAgentLab/
├── Bioagentlab.py                # Main entry point: agent orchestration
├── prompts/
│   └── templates.py              # Prompt templates for target validation, etc.
├── tools/
│   ├── pubmed_tool.py            # PubMed API wrapper
│   ├── clinical_trials.py        # ClinicalTrials.gov API client
│   ├── uniprot.py                # UniProt API tool
│   └── vector_retriever.py       # FAISS retriever for local literature
├── data/
│   └── literature/               # Local biomedical text files for RAG
├── .env                          # API keys (OpenAI, HuggingFace)
├── pyproject.toml                # Project dependencies
└── README.md
```

---

## ⚡️ Setup & Usage

### 1. **Clone the Repository**

```sh
git clone https://github.com/yourusername/BioAgentLab.git
cd BioAgentLab
```

### 2. **Install Dependencies**

We recommend using [uv](https://github.com/astral-sh/uv) or `pip` in a virtual environment:

```sh
uv venv .venv
.venv\Scripts\activate  # On Windows
uv pip install -r requirements.txt
```
Or, if using `pyproject.toml`:
```sh
uv pip install .
```

### 3. **Set Up Environment Variables**

Create a `.env` file in the project root with your API keys:

```
OPENAI_API_KEY=your-openai-key
HUGGINGFACEHUB_API_TOKEN=your-huggingface-token
```

### 4. **Prepare Local Literature (Optional)**

Add `.txt` files with biomedical content to `data/literature/` for RAG-based retrieval.

### 5. **Run the Agent**

```sh
uv run python Bioagentlab.py
```

The agent will process the example query or your custom query.

---

## 🧪 Example Use Case

**User Prompt:**
> Is CD47 a viable therapeutic target in solid tumors, and what regulatory hurdles are expected in Europe?

**Agent Response:**
- Yes, CD47 is under investigation as a macrophage checkpoint inhibitor.
- 6 recent studies support efficacy in lung and colorectal cancer (citations).
- 2 ongoing trials in Europe (NCT...).
- EMA Phase 1/2 guidelines require immune-related adverse event profiling.
- No patents currently granted in EU for CD47 + mAb combo with certain scaffolds.

---

## 📝 Notes

- **Model Selection:**  
  The Hugging Face endpoint must point to a model available for hosted inference (see [Hugging Face Hosted Models](https://huggingface.co/models?pipeline_tag=text-generation&library=transformers)).  
  Example: `tiiuae/falcon-7b-instruct`

- **Deprecation Warnings:**  
  Some LangChain classes are deprecated; see code comments for migration tips.

- **Extensibility:**  
  You can add new tools (e.g., patent search, additional APIs) by extending the `tools/` directory.

---

## 🤝 Contributing

Pull requests and issues are welcome! Please open an issue for feature requests or bug reports.

---

## 📄 License

MIT License

---

## 📬 Contact

For questions or collaboration, open an issue or contact the maintainer via GitHub.
