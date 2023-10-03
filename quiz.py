print("Seja muito bem vindo ao quiz do Alex!")
answer_user = input("Quer começar? (S/N) ")

if answer_user != "S":
  quit()

score = 0

print("Começando...")
print("Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n (A) Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) EA \n ")
answer_1 = input("Resposta? ")

if answer_1 == "A" :
  print("Correto!")
  score = score + 50
else:
  print("Incorreto!")

print("Qual é o nome do protagonista jogo GTA San Andreas? \n (A) Carlos Jhon \n (B) Carl Jhonson \n (C) Carl Jaqueline \n (D) Carlos Jhonson \n ")
answer_1 = input("Resposta? ")

if answer_1 == "B" :
  print("Correto!")
  score = score + 50
else:
  print("Incorreto!")


print(f"Quiz acabou... Pontuação: {score}%")