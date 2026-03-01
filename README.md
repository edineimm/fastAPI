# 🚀 FastAPI - APIs Modernas e Assíncronas com Python

Esta documentação detalha todos os endpoints, payloads e retornos esperados da API.

---

## 🛠️ Stack Tecnológica
* **FastAPI**
* **JWT** (JSON Web Tokens)
* **Python 3.x**

---

## 👤 Gerenciamento de Usuários

### 1. Cadastro de Usuário (Signup)
* **POST** `http://localhost:8000/api/v1/usuarios/signup`
* **Body (JSON):**
```json
{
    "nome": "Pedro",
    "sobrenome": "Carvalho",
    "email": "pedro@gmail.com",
    "senha": "01234567",
    "eh_admin": true
}
```
* **Return:**
```json
[
    {
        "id": 1,
        "nome": "Pedro",
        "sobrenome": "Carvalho",
        "email": "pedro@gmail.com",
        "eh_admin": true
    }
]
```

### 2. Listar Usuários
* **GET** `http://localhost:8000/api/v1/usuarios`
* **Result:**
```json
[
    {
        "id": 1,
        "nome": "Pedro",
        "sobrenome": "Carvalho",
        "email": "pedro@gmail.com",
        "eh_admin": true
    }
]
```

### 3. Atualizar Usuário
* **PUT** `http://localhost:8000/api/v1/usuarios/1`
* **Body (JSON):**
```json
{
    "email": "carvalho@gmail.com"
}
```
* **Result:**
```json
{
    "id": 1,
    "nome": "Pedro",
    "sobrenome": "Carvalho",
    "email": "carvalho@gmail.com",
    "eh_admin": true
}
```

### 4. Deletar Usuário
* **DELETE** `http://localhost:8000/api/v1/usuarios/1`

---

## 🔐 Autenticação e Perfil

### 1. Login
* **POST** `http://localhost:8000/api/v1/usuarios/login`
* **Body (form-data):**
    * `username`: pedro@gmail.com
    * `password`: 01234567
* **Result:**
```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer"
}
```

### 2. Obter Usuário Logado
* **GET** `http://localhost:8000/api/v1/usuarios/logado`
* **Authorization:** Bearer Token
* **Result:**
```json
{
    "id": 2,
    "nome": "Pedro",
    "sobrenome": "Carvalho",
    "email": "pedro@gmail.com",
    "eh_admin": true
}
```

---

## 📝 Gerenciamento de Artigos

### 1. Criar Artigo
* **POST** `http://localhost:8000/api/v1/artigos`
* **Authorization:** Bearer Token
* **Body (JSON):**
```json
{
    "titulo": "Primeiro artigo",
    "descricao": "Somente um artigo",
    "url_fonte": "https://scholar.google.com.br/"
}
```
* **Result:**
```json
{
    "titulo": "Primeiro artigo",
    "descricao": "Somente um artigo",
    "url_fonte": "https://scholar.google.com.br/",
    "id": 1,
    "usuario_id": 2
}
```

### 2. Listar Usuário com seus Artigos
* **GET** `http://localhost:8000/api/v1/usuarios/2`
* **Result:**
```json
{
    "id": 2,
    "nome": "Pedro",
    "sobrenome": "Carvalho",
    "email": "pedro@gmail.com",
    "eh_admin": true,
    "artigos": [
        {
            "titulo": "Primeiro artigo",
            "descricao": "Somente um artigo",
            "url_fonte": "https://scholar.google.com.br/",
            "id": 1,
            "usuario_id": 2
        }
    ]
}
```

### 3. Listar Todos os Artigos
* **GET** `http://localhost:8000/api/v1/artigos`
* **Result:**
```json
[
    {
        "titulo": "Primeiro artigo",
        "descricao": "Somente um artigo",
        "url_fonte": "https://scholar.google.com.br/",
        "id": 1,
        "usuario_id": 2
    }
]
```

### 4. Obter Artigo por ID
* **GET** `http://localhost:8000/api/v1/artigos/2`
* **Result:**
```json
{
    "titulo": "Segundo artigo",
    "descricao": "Somente um artigo v2",
    "url_fonte": "https://udemy.com.br/",
    "id": 2,
    "usuario_id": 2
}
```

### 5. Atualizar Artigo
* **PUT** `http://localhost:8000/api/v1/artigos/2`
* **Authorization:** Bearer Token
* **Body (JSON):**
```json
{
    "titulo": "FastAPI",
    "descricao": "treinamento de FastAPI"
}
```
* **Result:**
```json
{
    "titulo": "FastAPI",
    "descricao": "treinamento de FastAPI",
    "url_fonte": "https://google.com.br/",
    "id": 2,
    "usuario_id": 2
}
```

### 6. Deletar Artigo
* **DELETE** `http://localhost:8000/api/v1/artigos/2`
* **Authorization:** Bearer Token
* **Result:** `registro apagado`
