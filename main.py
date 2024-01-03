from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/hello")
def get_hello():
  return {"hello": "world"}

@app.get("/wallets")
def get_wallets() -> dict[str, int]:
  return {"wallet_id": 1}

@app.post("/wallets")
def post_wallets() -> dict[str, int]:
  return {"wallet_id": 2}

@app.get("/wallets/meta")
def get_wallet_meta() -> dict[str, dict[str, int]]:
  return {"meta": {"count": 2}}

@app.get("/wallets/{wallet_id}")
def get_wallets_id(
  wallet_id: int,
  include_histories: bool = False,
  user_agent: str = Header(),
) -> dict[str, int | list[dict[str, int]]]:
  print(user_agent)
  wallet = {"wallet_id": wallet_id}
  if include_histories:
    wallet["histories"] = [{"history_id": 1}]
  return wallet
