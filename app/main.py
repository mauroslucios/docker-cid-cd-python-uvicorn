from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

BASE_URL = "https://apidadosabertos.saude.gov.br/v1"

# Substitua por suas credenciais reais
USERNAME = ""
PASSWORD = ""

@app.post("/login")
async def login():
    async with httpx.AsyncClient() as client:
        payload = {"usuario": USERNAME, "senha": PASSWORD}
        resp = await client.post(f"{BASE_URL}/autenticacao/login", json=payload)
        if resp.status_code != 200:
            raise HTTPException(status_code=resp.status_code, detail="Falha no login")
        data = resp.json()
        return data  # Normalmente contém o token de acesso

@app.get("/dados-protegidos")
async def dados_protegidos():
    async with httpx.AsyncClient() as client:
        # Primeiro faça login para obter token
        payload = {"usuario": USERNAME, "senha": PASSWORD}
        login_resp = await client.post(f"{BASE_URL}/autenticacao/login", json=payload)
        if login_resp.status_code != 200:
            raise HTTPException(status_code=login_resp.status_code, detail="Falha no login")
        token = login_resp.json().get("access_token")
        if not token:
            raise HTTPException(status_code=500, detail="Token não recebido")

        # Use o token para acessar endpoint protegido
        headers = {"Authorization": f"Bearer {token}"}
        resp = await client.get(f"{BASE_URL}/arboviroses/zikavirus", headers=headers)
        if resp.status_code != 200:
            raise HTTPException(status_code=resp.status_code, detail="Erro ao acessar dados protegidos")
        return resp.json()
