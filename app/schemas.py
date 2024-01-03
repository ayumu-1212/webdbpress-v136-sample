from enum import StrEnum
from pydantic import BaseModel, Field, PositiveInt

class HistoryType(StrEnum):
  INCOME = "INCOME"
  OUTCOME = "OUTCOME"

class History(BaseModel):
  history_id: int
  name: str
  amount: PositiveInt
  type: HistoryType

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
