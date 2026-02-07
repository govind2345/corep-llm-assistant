from pydantic import BaseModel

class CorepOwnFunds(BaseModel):
    cet1_amount: float
    explanation: str
    regulatory_reference: str
