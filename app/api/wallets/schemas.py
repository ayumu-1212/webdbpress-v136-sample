from pydantic import BaseModel, Field
from .histories.schemas import History

class Wallet(BaseModel):
  wallet_id: int = Field(..., ge=1)
  name: str = Field(
    ...,
    pattern="^[a-zA-Z]+$",
    description="Wallet name",
  )
  histories: list[History]

class CreateWalletRequest(BaseModel):
  name: str
