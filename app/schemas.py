from enum import StrEnum
from pydantic import BaseModel, PositiveInt

class HistoryType(StrEnum):
  INCOME = "INCOME"
  OUTCOME = "OUTCOME"

class History(BaseModel):
  history_id: int
  name: str
  amount: PositiveInt
  type: HistoryType

class Wallet(BaseModel):
  wallet_id: int
  name: str
  histories: list[History]

class CreateWalletRequest(BaseModel):
  name: str
