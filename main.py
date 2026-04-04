from fastapi import FastAPI

# Cria a aplicação
app = FastAPI(
    title="Calculadora API",
    description="API REST para operações matemáticas básicas. Projeto 01 do portfólio de Daniel Tavares.",
    version="1.0.0"
)

# Rota inicial
@app.get("/", summary="Status da API", description="Verifica se a API está funcionando.")
def inicio():
    return {"mensagem": "Calculadora API funcionando!"}

# Soma
@app.get("/somar", summary="Soma dois números", description="Recebe dois valores e retorna a soma entre eles.")
def somar(a: float, b: float):
    return {"operacao": "soma", "resultado": a + b}

# Subtração
@app.get("/subtrair", summary="Subtrai dois números", description="Recebe dois valores e retorna a subtração entre eles.")
def subtrair(a: float, b: float):
    return {"operacao": "subtracao", "resultado": a - b}

# Multiplicação
@app.get("/multiplicar", summary="Multiplica dois números", description="Recebe dois valores e retorna o produto entre eles.")
def multiplicar(a: float, b: float):
    return {"operacao": "multiplicacao", "resultado": a * b}

# Divisão
@app.get("/dividir", summary="Divide dois números", description="Recebe dois valores e retorna a divisão. Retorna erro se o divisor for zero.")
def dividir(a: float, b: float):
    if b == 0:
        return {"erro": "Não é possível dividir por zero!"}
    return {"operacao": "divisao", "resultado": a / b}