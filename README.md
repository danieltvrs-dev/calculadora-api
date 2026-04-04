# 🧮 Calculadora API

![Python](https://img.shields.io/badge/Python-3.13-e8132a?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.135-e8132a?style=flat-square&logo=fastapi&logoColor=white)
![Status](https://img.shields.io/badge/status-concluído-22c55e?style=flat-square)

> Meu primeiro projeto com FastAPI. Uma API REST simples para operações matemáticas — desenvolvida do zero enquanto aprendo desenvolvimento backend com Python.

---

## 💡 Por que esse projeto?

Estou no início da minha jornada como desenvolvedor fullstack. Antes de construir sistemas complexos, quis entender como uma API funciona de verdade — como ela recebe dados, processa e responde. Esse projeto foi o meu primeiro passo.

---

## 🚀 O que essa API faz?

Recebe dois números e uma operação matemática, e retorna o resultado. Simples assim — mas por baixo dos panos, é uma API REST real rodando em produção.

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/` | Status da API |
| GET | `/somar?a=10&b=5` | Retorna `15.0` |
| GET | `/subtrair?a=10&b=3` | Retorna `7.0` |
| GET | `/multiplicar?a=4&b=6` | Retorna `24.0` |
| GET | `/dividir?a=10&b=2` | Retorna `5.0` |
| GET | `/dividir?a=10&b=0` | Retorna erro tratado |

---

## 🛠️ Tecnologias utilizadas

- **Python 3.13** — linguagem principal
- **FastAPI** — framework moderno para APIs REST
- **Uvicorn** — servidor ASGI para rodar a aplicação
- **Swagger UI** — documentação automática gerada pelo FastAPI

---

## ▶️ Como rodar localmente
```bash
# 1. Clone o repositório
git clone https://github.com/danieltvrs-dev/calculadora-api.git
cd calculadora-api

# 2. Instale as dependências
pip install fastapi uvicorn

# 3. Rode o servidor
uvicorn main:app --reload
```

Acesse a API: http://127.0.0.1:8000  
Documentação interativa: http://127.0.0.1:8000/docs

---

## 📸 Documentação

A documentação foi gerada automaticamente pelo FastAPI via Swagger UI.  
Acesse `/docs` para testar todos os endpoints diretamente no navegador.

---

## 📚 O que aprendi

- Como criar e estruturar uma API REST com FastAPI
- Como definir rotas, parâmetros e retornos em JSON
- Como tratar erros (ex: divisão por zero)
- Como o FastAPI gera documentação automática com Swagger
- Como subir um projeto no GitHub com Git

---

## 🗺️ Próximos projetos

Este é o **Projeto 01** de um roadmap de 11 projetos que estou desenvolvendo até meados de 2026, evoluindo do básico ao avançado com Python, FastAPI, PostgreSQL e React.

➡️ Veja o roadmap completo no meu [GitHub](https://github.com/danieltvrs-dev)

---

## 👨‍💻 Autor

**Daniel Tavares**  
Estudante de ADS · Fullstack Developer em formação  
Nossa Senhora de Lourdes, SE — Brasil 🇧🇷

[![GitHub](https://img.shields.io/badge/GitHub-danieltvrs--dev-e8132a?style=flat-square&logo=github)](https://github.com/danieltvrs-dev)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-daniel--campostvrs-e8132a?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/daniel-campostvrs)