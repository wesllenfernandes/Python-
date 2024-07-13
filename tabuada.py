print("-----------------------")
print("tabuada das 4 operações")
numero = int(input("digite um valor que você deseja ver da tabuada: "))
print(f"Tabuada de {numero}:")
operacao = str(input("qual tabuada vc deseja: "))
for i in range(1, 11):
  if operacao == "adição":
    resultado = numero + i
    print(f"{numero} + {i} = {resultado}")
  elif operacao == "multiplicação":
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")
  elif operacao == "divisão":
    resultado = numero / 1
    print(f"{numero} / {i} = {resultado}")
  elif operacao == "subtração":
    resultado = numero - 1
    print(f"{numero} - {i} = {resultado}")