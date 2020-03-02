SLP = int(8000)
OLP = int(8000)
AM = int(input("Qual o ataque do seu monstro? "))
DM = int(input("Qual a defesa do seu monstro? "))
P = input('Qual a posição do seu monstro? ')
AP = input ("Seu monstro tem um ataque perfurante? ")
AMO = int()
DMO = int()
c = 0
while SLP > 0 or OLP > 0 :
  MOP = input("Seu opnente possui monstros? ")

  if MOP == "SIM" or MOP =="Sim" or MOP == "sim" :
    AMO = int(input("Qual é o ataque do monstro inimigo? "))
    DMO = int(input("Qual é o defesa do monstro inimigo? "))
    POP = int(input("Qual é a posição do monstro inimigo? "))
  else :
    OLP += - AM
    print (f"Vc atacou os pontos de vida do seu oponente diretamente causando {AM} de dano no seu inimigo")
    print("Seu oponente tem {OLP} de vida")

  MP = input ("Vc vai querer mudar a posição do seu monstro?")
  if MP == "SIM" or MP == "Sim" or MP == "sim" :
    if P == "defesa" or P == "Defesa" or P == "DEFESA" or P == "Def" :
       P == "Ataque"
    else :
      P == "Defesa"
  
  b = input("Vc quer batalhar? ")
  if b == "SIM" or b == "Sim" or b == "sim" : 
     if POP == "defesa" or POP == "Defesa" or POP == "DEFESA" or POP == "Def" :