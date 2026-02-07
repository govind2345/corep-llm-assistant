from fastapi import FastAPI
from app.rag import retrieve_rules
from app.schema import CorepOwnFunds

app = FastAPI(title="LLM-Assisted COREP Assistant")

@app.post("/corep/ownfunds")
def generate_corep(scenario: str):
    rules = retrieve_rules()

    # Simulated LLM output (safe for demo)
    result = CorepOwnFunds(
        cet1_amount=12500000,
        explanation="CET1 calculated based on ordinary share capital and retained earnings.",
        regulatory_reference="PRA Rulebook Own Funds – CET1 definition"
    )

    return {
        "input_scenario": scenario,
        "rules_used": rules,
        "corep_output": result
    }
