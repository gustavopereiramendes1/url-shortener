# 🔗 Encurtador de URL - FastAPI + MongoDB
![PYTHON](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![MONGODB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white) ![FASTAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) ![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) ![JAVASCRIPT](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) ![.ENV Badge](https://img.shields.io/badge/.ENV-ECD53F?logo=dotenv&logoColor=000&style=for-the-badge) ![Insomnia Badge](https://img.shields.io/badge/Insomnia-4000BF?logo=insomnia&logoColor=fff&style=for-the-badge)

Um serviço moderno para encurtar URLs desenvolvido com:

- **Backend**: Python + FastAPI
- **Banco de Dados**: MongoDB Atlas
- **Frontend**: HTML/CSS/JS

## 🚀 Como usar

### Via API REST

**1. Encurtar URL:**
```http
POST /api/shorten/
Content-Type: application/json

{
  "originalUrl": "https://url-muito-longa.com/parametros?query=complexa"
}
```
**Resposta:**
```json
{
  "shortUrl": "http://localhost:8000/api/abc123"
}
```

**2. Acessar URL encurtada:**
```http
GET /api/abc123
```
(Redireciona automaticamente para a URL original)

**3. Listar todas URLs:**
```http
GET /api/list
```

---

### Via Interface Web

Acesse [http://localhost:8000](http://localhost:8000) e:

- Cole sua URL longa
- Clique em "Encurtar URL"
- Copie o link gerado

---

## 🛠️ Configuração

Instale as dependências:
```bash
pip install -r requirements.txt
```

Configure o Atlas MongoDB:
- Crie um arquivo chamado .env na raiz do projeto.
- Adicione a seguinte variável ao arquivo:
MONGO_URI= "<link do banco de dados no atlas>"
exemplo:
```bash
MONGO_URI="mongodb+srv://<usuario>:<senha>@<cluster>.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
````

Execute o servidor:
```bash
uvicorn main:app --reload
```

---

## 🌟 Recursos

✔ Geração automática de short codes  
✔ Redirecionamento HTTP eficiente  
✔ Armazenamento em nuvem (MongoDB Atlas)  
✔ Interface web responsiva  
✔ API RESTful documentada  

---

## 📌 Exemplo Prático

**Encurtar:**
```python
import requests

response = requests.post(
    "http://localhost:8000/api/shorten/",
    json={"originalUrl": "https://www.google.com"}
)
print(response.json())  # {"shortUrl": "http://localhost:8000/api/xyz789"}
```

**Acessar:**

Abra no navegador:
```
http://localhost:8000/api/xyz789
```
(Redireciona para Google)
