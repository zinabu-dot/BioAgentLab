# tools/clinical_trials.py

import requests


class ClinicalTrialsTool:
    """
    Tool for querying ClinicalTrials.gov using its public API.
    """

    def __init__(self):
        self.base_url = "https://clinicaltrials.gov/api/query/study_fields"

    def run(self, query: str) -> str:
        """
        Run a search for active trials matching the input query.
        """
        print(f"[ClinicalTrials] Searching for: {query}")
        params = {
            "expr": query,
            "fields": "NCTId,Condition,BriefTitle,Phase,LocationCountry,OverallStatus",
            "min_rnk": 1,
            "max_rnk": 5,
            "fmt": "json",
        }

        response = requests.get(self.base_url, params=params)

        if not response.ok:
            return f"Error fetching clinical trial data: {response.status_code}"

        data = response.json()
        trials = data.get("StudyFieldsResponse", {}).get("StudyFields", [])

        if not trials:
            return "No active clinical trials found for this query."

        results = []
        for t in trials:
            results.append(
                f"🔹 **{t.get('BriefTitle', ['N/A'])[0]}**\n"
                f"• ID: {t.get('NCTId', [''])[0]}\n"
                f"• Condition: {t.get('Condition', [''])[0]}\n"
                f"• Phase: {t.get('Phase', ['N/A'])[0]}\n"
                f"• Country: {t.get('LocationCountry', ['N/A'])[0]}\n"
                f"• Status: {t.get('OverallStatus', [''])[0]}\n"
            )

        return "\n".join(results)
