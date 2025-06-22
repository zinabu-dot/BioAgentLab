# prompts/templates.py

import os

TEMPLATES = {
    "target_validation": """You are a biomedical research agent assisting with early-stage drug discovery.

You will be given a user query related to a potential drug target. Your task is to:
1. Assess the target's biological relevance and known function.
2. Retrieve and synthesize information from literature, protein databases, clinical trials, and internal RAG memory.
3. Provide a concise summary of current evidence.
4. List known limitations or regulatory issues (especially in US/EU).

Respond in clear scientific language appropriate for a biotech R&D team.

---

Query: {input}

Start your analysis below:
"""
}


def load_prompt_template(name: str) -> str:
    if name not in TEMPLATES:
        raise ValueError(f"Prompt template '{name}' not found.")
    return TEMPLATES[name]
