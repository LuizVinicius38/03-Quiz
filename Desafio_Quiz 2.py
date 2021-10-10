print('''
1- Qual é minha cor preferida?
a - Verde
b - Azul
c - Amarelo
d - Rosa
e - Vermelho
''')
resposta = input("").lower()
if resposta == "a":
    print(" Você errou, essa não e minha cor preferida:( ")
elif resposta == "b":
    print("Você errou :( ")
elif resposta == "c":
    print("Essa é a cor que mais detesto >:( ")
elif resposta == "d":
    print("É umas das cor que gosto, mas não é minha favorita:( ")
elif resposta == "e":
    print("Você acertou, essa é minha cor favorita :3 ")
else:
    print("Você deveria ter escolhido umas das alternativas")
print("Obrigado pela sua resposta")
