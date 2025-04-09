def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b  

def divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero!")
    return a / b

def potencia_operator(base, expoente):  
    return base ** expoente  # Usando operador **

def optencia_loop (base, expoente):
    resultado = 1  
    for _ in range(expoente):  # Usando loop for  
        resultado *= base  
    return resultado