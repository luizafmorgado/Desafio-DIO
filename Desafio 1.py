#  Crie uma Função: recomendar_plano para receber o consumo médio mensal: def recomendar_plano(consumo_medio): 
# Crie uma Estrutura Condicional para verifica o consumo médio mensal]

def recomendar_plano(consumo):
    consumo = float(consumo)  
    if consumo <= 10:
        return "Plano Essencial Fibra - 50Mbps"
    elif consumo > 10 and consumo <= 20:
        return "Plano Prata Fibra - 100Mbps"
    else:
        return "Plano Premium Fibra - 300Mbps"

consumo_mensal = input("") 

print(recomendar_plano(consumo_mensal))