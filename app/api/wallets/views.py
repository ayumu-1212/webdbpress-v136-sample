from fastapi import APIRouter, Header, Path, Query
from .schemas import CreateWalletRequest, Wallet
from .histories.views import router as histories_router

router = APIRouter(prefix="/wallets")

@router.get("")
def get_wallets() -> dict[str, int]:
  return {"wallet_id": 1}

@router.post("", response_model=Wallet)
def post_wallets(data: CreateWalletRequest) -> dict:
  return {"wallet_id": 2, "name": data.name}

@router.get("/meta")
def get_wallet_meta() -> dict[str, dict[str, int]]:
  return {"meta": {"count": 2}}

@router.get("/{wallet_id}")
def get_wallets_id(
  wallet_id: int = Path(..., ge=1),
  include_histories: bool = Query(False),
  user_agent: str | None = Header(default=None),
) -> dict[str, int | list[dict[str, int]]]:
  print(user_agent)
  wallet = {"wallet_id": wallet_id}
  if include_histories:
    wallet["histories"] = [{"history_id": 1}]
  return wallet

router.include_router(histories_router, prefix="/{wallet_id}")
