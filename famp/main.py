from fastapi import FastAPI

app = FastAPI()


@app.get('/msg')
async def mensagem():
    return {"msg": "Olá, mundo!"}

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host='0.0.0.0', port=8000,  # qualquer ip na mesma rede pode acessar, porta 8000
                log_level='info', reload=True)
