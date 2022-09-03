from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

ethAddresses = []
responses = []

@app.get("/ethAddress", tags=["ethAddresses"])
async def get_ethAddresses() -> dict:
    return {"data": ethAddresses}

@app.post("/ethAddress", tags=["ethAddresses"])
async def add_ethAddress(ethAddress: dict) -> dict:
    ethAddresses.append(ethAddress)
    return {
        "data": {"EthAddress added."}
    }

@app.get("/response", tags=["response"])
async def get_responses() -> dict:
    return responses

@app.post("/response", tags=["reponses"])
async def add_responses(ethAddress: dict) -> dict:
    url = "https://api.opensea.io/api/v1/collections?asset_owner=" + \
        ethAddress["ethAddress"]+"&offset=0&limit=300"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    #response = [response_item[0] for response_item in response.json()]
    responses.append(response.json())
    print(responses)