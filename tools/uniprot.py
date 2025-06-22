# tools/uniprot.py

import requests


class UniProtTool:
    """
    Wrapper for querying UniProt for protein/gene information.
    """

    def __init__(self):
        self.base_url = "https://rest.uniprot.org/uniprotkb/search"

    def run(self, query: str) -> str:
        """
        Query UniProt for gene/protein information.
        """
        print(f"[UniProt] Searching for: {query}")
        params = {
            "query": query,
            "format": "json",
            "fields": "accession,id,protein_name,gene_names,organism_name,length,function",
        }

        response = requests.get(self.base_url, params=params)

        if not response.ok:
            return f"Error retrieving data from UniProt: {response.status_code}"

        results = response.json().get("results", [])

        if not results:
            return "No results found in UniProt for your query."

        # Extract top result
        top = results[0]
        return (
            f"🧬 **UniProt ID**: {top.get('primaryAccession')}\n"
            f"🔖 **Protein Name**: {top.get('proteinDescription', {}).get('recommendedName', {}).get('fullName', {}).get('value', 'N/A')}\n"
            f"🧪 **Gene Names**: {', '.join(top.get('genes', [{}])[0].get('geneName', {}).values()) if top.get('genes') else 'N/A'}\n"
            f"🌍 **Organism**: {top.get('organism', {}).get('scientificName', 'N/A')}\n"
            f"🧫 **Length**: {top.get('sequence', {}).get('length', 'N/A')} aa\n"
        )
