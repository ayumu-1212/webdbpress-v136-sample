from enum import StrEnum
from datetime import datetime
from pydantic import BaseModel, PositiveInt

class HistoryType(StrEnum):
  INCOME = "INCOME"
  OUTCOME = "OUTCOME"

class History(BaseModel):
  history_id: int
  name: str
  amount: PositiveInt
  type: HistoryType
  history_at: datetime
