from fastapi import FastAPI, HTTPException, status, Request
from fastapi.responses import RedirectResponse, FileResponse
from models import UrlRequest
from config.database import collection_name
import shortuuid
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from fastapi.staticfiles import StaticFiles


app = FastAPI()

@app.get("/")
def read_index():
    return FileResponse("static/index.html")

# Configuração do MongoDB
MONGO_URI = "mongodb+srv://jungle000ww:000gustavo@cluster0.4gxzomt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
db = client["Mongo-shortURL"]

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

def generate_short_id() -> str:
    """Gera um ID curto usando shortuuid"""
    return shortuuid.ShortUUID().random(length=8)

@app.post("/api/shorten/")
def generate_url(data: UrlRequest, request: Request):
    original_url = data.originalUrl
    short_id = generate_short_id()
    # Monta a shortUrl completa
    full_short_url = str(request.base_url) + f"api/{short_id}"
    new_url = {"originalUrl": original_url, "shortUrl": full_short_url, "shortId": short_id}
    collection_name.insert_one(new_url)
    
    return {"shortUrl": new_url["shortUrl"]}

#@app.get("{short_url}")
#def get_original_url(short_url: str):
    # Busca pelo campo shortId, não pela shortUrl completa
    #url = collection_name.find_one({"shorturl": short_url})
    #if not url:
    #    raise HTTPException(status_code=404, detail="URL não encontrada")
    #return RedirectResponse(url["originalUrl"])

@app.get("/api/list")
async def listar_urls():
    try:
        urls = list(collection_name.find({}))
        for url in urls:
            url["id"] = str(url.get("_id", ""))
            url.pop("_id", None)  # Remove _id se existir, sem erro
        return urls
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao listar URLs: {str(e)}"
        )

@app.get("/api/{short_id}")
def get_original_url(short_id: str):
    url = collection_name.find_one({"shortId": short_id})
    if not url:
        raise HTTPException(status_code=404, detail="URL não encontrada")
    return RedirectResponse(url["originalUrl"])

