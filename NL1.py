from math import pow, sqrt

PI = 3.14159265359

print("Membros do grupo:\n")
print("Diego Jardim\nGiovanne \nRômulo Canavesso\nLucas Antunes\n\n")

print('Esse programa consiste em calcular parametros de ondas OEM (Ondas eletromagneticas) atraves de formulas e calculos apresentados durante as aulas de fisica.\n')

print('As ondas eletromagneticas sao ondas que possuem oscilacoes formadas por campos eletricos e magneticos, que se propagam pelo vacuo ou em meios materias, que podem ter variacoes de frequencia, comprimento, intensidade e quantidades de ondas.\n\n')

print("Formulas usadas:\n")
print("Em = c*Bm")
print("I = Emˆ2/2*u*c")
print("w = 2*π*f")
print("c = λ*f")
print("k = 2*π/λ\n\n")

def menu():
  
  print("MENU:\n")
  print("1 - Em (Onda eletrica)")
  print("2 - Bm (Onda magnetica)")
  print("3 - I (Intensidade da onda)")
  print("4 - f (Frequencia da onda)")
  print("5 - λ (Comprimento da onda)")
  print("6 - k (Quantidades de ondas)")
  print("7 - Ω (Frequencia angular da onda)\n")

menu()
    
c = 3*pow(10,8) #velocidade da luz no vacuo
u = 4*PI*pow(10,-7)

def opcao():
  resp = int(input("Escolha a opção desejada: "))
  
  if (resp == 1):
    Em = float(input("Entre com o valor de Em: "))
    I = (Em**2)/(2*u*c)
    Bm = Em/c
    print("I = {:.2e} W/mˆ2" .format(I))
    print("Bm = {:.2e} T\n" .format(Bm))
    print("Explicacao: Aqui temos o resultado da intensidade da onda e o valor da onda magnetica, valores calculados atraves do valor da onda eletrica e das formulas usadas durante as aulas.\n\n")


  elif (resp == 2):
    Bm = float(input("Entre com o valor de Bm: "))
    I = (Bm**2)*c/(2*u)
    Em = c*Bm
    print("I = {:.2e} W/mˆ2" .format(I))
    print("Em = {:.2e} V/m\n" .format(Em))
    print("Explicacao: Aqui temos o resultado da intensidade da onda e o valor da onda eletrica, valores calculados atraves do valor da onda magnetica e das formulas usadas durante as aulas.\n\n")


  elif (resp == 3):
    I = float(input("Entre com o valor de I: "))
    Em = sqrt(2*u*c*I)
    Bm = (I*(2*u))/Em
    print("Em = {:.2e} V/m" .format(Em))
    print("Bm = {:.2e} W/mˆ2\n" .format(Bm))
    print("Explicacao: Aqui temos o resultado da onda eletrica e onda magnetica, valores calulcados atraves do valor da intensidade da onda e das formulas usadas durante as aulas.\n\n")


  elif (resp == 4):
    f = float(input("Digite o valor de frequência: "))
    y = c/f
    k = (2*PI)/y 
    w = (2*PI)*f
    print('λ = {:.2e} m' .format(y))
    print('k = {:.2e} rad/m' .format(k))
    print('w = {:.2e} rad/s\n' .format(w))
    print("Explicacao: Aqui temos o resultado do comprimento da onda, quantidade de ondas e a frequencia angular da onda, valores calculados atraves do valor da frenquencia da onda e das formulas usadas durante as aulas.\n\n")


  elif (resp == 5):
    y = float(input("Digite o valor de λ: "))
    f = c/y
    k = (2*PI)/y
    w = (2*PI)*f
    print('f = {:.2e} Hz' .format(f))
    print('k = {:.2e} rad/m' .format(k))
    print('w = {:.2e} rad/s\n' .format(w))
    print("Explicacao: Aqui temos o resultado da frequencia da onda, quantidade da onda e a frequencia angular da onda, valores calculados atraves do comprimento de ondas e das formulas usadas durante as aulas.\n\n")


  elif (resp == 6):
    k = float(input("Digite o valor de k: "))
    y = (2*PI)/k
    f = c/y
    w = k*y*f
    print('λ = {:.2e} m' .format(y))
    print('f = {:.2e} Hz' .format(f))
    print('w = {:.2e} rad/s\n' .format(w))
    print("Explicacao: Aqui temos o resultado do comprimento da onda, frequencia da onda e a frequencia angular da onda, valores calculados atraves da quantidade de ondas e das formulas usadas durante as aulas.\n\n")

  
  elif (resp == 7):
    w = float(input("Digite o valor de Ω: "))
    f = w/(2*PI)
    y = c/f
    k = (2*PI)/y
    print('f = {:.2e} Hz' .format(f))
    print('λ = {:.2e} m' .format(y))
    print('k = {:.2e} rad/m\n' .format(k))
    print("Explicacao: Aqui temos o resultado da frequencia da onda, comprimento da onda e a quantidade de ondas, valores calculados atraves da frequencia angular da onda e das formulas usadas durante as aulas.\n\n")

opcao()

perg = int(input("Quer calcular novamente? Digite 0 -> Nao ou 1 -> Sim: "))

while perg != 0:
  print("")
  menu()
  opcao()
  perg = int(input("Quer calcular novamente? Digite 0 -> Nao ou 1 -> Sim: "))
  
