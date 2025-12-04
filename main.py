from fastapi import FastAPI

app = FastAPI()

@app.get("/calcp")
def calculerp(nombre: int):
    resultat = nombre+1
    return {"resultat": resultat}

@app.get("/calcm")
def calculerm(nombre: int):
    resultat = nombre-1
    return {"resultat": resultat}
