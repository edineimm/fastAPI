from fastapi import FastAPI
from core.configs import settings
from api.v1.api import api_router

app = FastAPI(title='Curso de FastAPI - Segurança')
app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', port=8000,
                reload=True, log_level='info')

    """token: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNzcyOTkxMTU0LCJpYXQiOjE3NzIzODYzNTQsInN1YiI6Mn0.L3kW5LS3jHysl8d0tXwFOjSrlIpVKVOvj08YyBNlDiE'
       tipo: bearer
    """
