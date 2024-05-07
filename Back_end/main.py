from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from controlleur.query_data import query_rag
import time
from pydantic import BaseModel
from controlleur.populate_database import embedding_main
from controlleur.populate_database import clear_database

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

list_Users = []
path_aticles= "./data/"
class User(BaseModel):
    nom: str
    prenom: str

#Poser une question à LLM model
@app.get("/pose_question/{question}")
def Pose_Question(question)-> str:
    tic = time.time()
    reponse = query_rag(question)
    toc = time.time()
    duree_exc= toc - tic
    print(reponse)
    return reponse


@app.post("/upload_article")
async def upload_article(file: UploadFile = File(...)):
    # Enregistrer article
    content = await file.read()
    with open(f"{path_aticles}{file.filename}","wb") as f:
        f.write(content)
    return {"filename":file.filename, "path":f"{path_aticles}{file.filename}"}

#embedding et ajouter à la base de données Chroma
@app.get("/embedding_db")
def embedding_db():
    embedding_main()
    return {"resultat": "Emedding terminé! "}

# Supprimer la base de données (Vector Chroma)
@app.get("/clear_dbVector")
def clear_dbVector():
    clear_database()
    print("Bien supprimé la base de données Vector")
    return {"resultat":True}

@app.post("/add_User")
def add_User(user: User):
    print(user)
    list_Users.append(user)
    print("Bien enregistré!")
    return user






