# BioAgentLab - Core Biomedical Agent

import os
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain_community.utilities import PubMedAPIWrapper
from langchain_huggingface import HuggingFaceEndpoint

from tools.uniprot import UniProtTool
from tools.clinical_trials import ClinicalTrialsTool
from tools.vector_retriever import VectorRetriever
from prompts.templates import load_prompt_template
from dotenv import load_dotenv

load_dotenv()


# Initialize Hugging Face LLM (replace with your own HF token)
llm = HuggingFaceEndpoint(
    endpoint_url="https://api-inference.huggingface.co/models/meta-llama/Llama-3.1-8B-Instruct",
    # "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    temperature=0.2,
    max_new_tokens=512,
    repetition_penalty=1.03,
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
)


# Load prompt template for target validation
prompt_template = load_prompt_template("target_validation")

# Define tools
pubmed_tool = Tool(
    name="PubMed",
    func=PubMedAPIWrapper().run,
    description="Useful for retrieving abstracts from PubMed. Input should be a biomedical topic or gene.",
)

uniprot_tool = Tool(
    name="UniProt",
    func=UniProtTool().run,
    description="Provides protein and gene target information from UniProt database.",
)

clinical_trials_tool = Tool(
    name="ClinicalTrials",
    func=ClinicalTrialsTool().run,
    description="Searches ClinicalTrials.gov for current trials related to the input query.",
)

vector_retriever_tool = Tool(
    name="BiomedicalRAG",
    func=VectorRetriever().retrieve,
    description="Retrieves vector-embedded biomedical literature related to the query for synthesis.",
)

# Initialize agent with tools
agent = initialize_agent(
    tools=[pubmed_tool, uniprot_tool, clinical_trials_tool, vector_retriever_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)


def run_bioagent(query: str):
    print("\n[User Query]:", query)
    result = agent.run(prompt_template.format(input=query))
    print("\n[Agent Output]:\n", result)
    return result


if __name__ == "__main__":
    # Example query
    user_query = "Is CD47 a valid cancer immunotherapy target in solid tumors, and what are the regulatory hurdles in the EU?"
    run_bioagent(user_query)
