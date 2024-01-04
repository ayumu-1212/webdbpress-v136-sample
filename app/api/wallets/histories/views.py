from fastapi import APIRouter

router = APIRouter(prefix="/histories")

@router.get("")
def get_histories() -> dict[str, int]:
  return {"history_id": 1}
