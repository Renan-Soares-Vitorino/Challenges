import json

with open("faturDesafio3.json", 'r') as arquivo:
    faturamento = json.load(arquivo)

print(faturamento)