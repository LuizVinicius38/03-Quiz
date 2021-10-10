print("Qual é minha comida preferida")
resposta = input("").lower()
print("Qual a minha cor favorita")
respostas = input("").lower()
print("Eu prefiro frio ou calor")
respost = input("").lower()
print("Qual animal que eu mas amo?(escreva em inglês)")
res = input("").lower()
print("Qual time de futebol eu torço?")
re = input("").lower()
score = 0
if resposta == "pizza":
    score = +1
if respostas == "vermelho":
    score = score + 1
if respost == "frio":
    score = score + 1
if res == "cat":
    score = score + 1
if re == "nenhum":
    score = score + 1
    print(f"Você tem {score} pontos")
else:
    print(f"Você tem {score} pontos")
if score == 5:
    print("Muito bem")
else:
    print("Tente novamente")


