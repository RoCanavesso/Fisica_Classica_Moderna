import math

print("\n")

print("Programa criado por: Rômulo Carneiro de Oliveira Canavesso")

print("\n")

print("Objetivo do programa: ")

print("Este programa tem o intuito de calcular a intensidade de uma luz não polarizada após ou antes de passar sobre 2 ou 3 filtros polarizadores, onde tal polarizadores possuem ângulos definidos e diferentes (ou não) da luz incidente, tendo o objetivo de absorver a intensidade dessa luz (dependendo do ângulo da luz e do filtro polarizador) para que a enfraqueça ou até mesmo absorva totalmente a intensidade da luz, nos impossibilitando de vê-la.")

print("\n")

print("Como forma didática, temos o exemplo dos óculos de sol polarizados, que enfraquecem a intensidade da luz solar através da absorção, deixando a luz mais fraca para nossos olhos após passar pelas lentes polarizadas (tal ato acontece pelo fato da luz não polarizada incidente do sol estar em um ângulo difetente do ângulo das lentes dos óculos de sol, assim enfraquecendo a luz incidente.")

#============================================================================================#

def loop():
  print("\n")
  perg = int(input("Deseja voltar ao menu? 1 - sim ou 2 - não: "))

  if(perg == 1):
    menu()
    calcI1 = 0
    calcI2 = 0
    calcI3 = 0

  elif(perg == 2):
    print("\n")    

#============================================================================================#

cos = math.cos
rad = math.radians

def polarizadores2(): 
  #aqui será feio o calculo com 2 polarizadores

  print("1 - Calcular com Intensidade 0")
  print("2 - Calcular com Intensidade 1")
  print("3 - Calcular com Intensidade 2")
  print("\n")

  esc_polarizadores2 = int(input("Digite o nº desejado: "))
  print("\n")

  if(esc_polarizadores2 == 1):
    pol1 = float(input("Digite o valor do polarizador 1: "))
    pol2 = float(input("Digite o valor do polarizador 2: "))
    i0 = float(input("Digite o valor da Intensidade 0 (I0): "))
    print("\n")
    
    calcI1 = (i0/2) #calcula a intensidade I1 apos passar do polarizador 1
    calcI2 = (calcI1 * pow(cos(rad(pol2 - pol1)), 2)) #calcula a intensidade I2 apos passar do polarizador 2

    print("I1 = %.2f W/cm²" % calcI1)
    print("I2 = %.2f W/cm²" % calcI2)
  
    loop()
  
  elif(esc_polarizadores2 == 2):
    pol1 = float(input("Digite o valor do polarizador 1: "))
    pol2 = float(input("Digite o valor do polarizador 2: "))
    i1 = float(input("Digite o valor da Intensidade 1 (I1): "))
    print("\n")
    
    calcI0 = (i1 * 2)
    calcI2 = (i1 * pow(cos(rad(pol2 - pol1)), 2))

    print("I0 = %.2f W/cm²" % calcI0)
    print("I2 = %.2f W/cm²" % calcI2)
  
    loop()

  elif(esc_polarizadores2 == 3):
    pol1 = float(input("Digite o valor do polarizador 1: "))
    pol2 = float(input("Digite o valor do polarizador 2: "))
    i2 = float(input("Digite o valor da Intensidade 2 (I2): "))
    print("\n")
    
    calcI1 = (i2 / pow(cos(rad(pol2 - pol1)), 2))
    calcI0 = (calcI1 * 2)

    print("I0 = %.2f W/cm²" % calcI0)
    print("I1 = %.2f W/cm²" % calcI1)
  
    loop()

#========================================================================================#

def polarizador3():
  #aqui será feio o calculo com 3 polarizadores
  
  print("1 - Calcular com Intensidade 0")
  print("2 - Calcular com Intensidade 1")
  print("3 - Calcular com Intensidade 2")
  print("4 - Calcular com Intensidade 3")
  print("\n")

  esc_polarizadores3 = int(input("Digite o nº desejado: "))
  print("\n")

  if(esc_polarizadores3 == 1):
    pol1 = float(input("Digite o valor do polarizador 1: "))
    pol2 = float(input("Digite o valor do polarizador 2: "))
    pol3 = float(input("Digite o valor do polarizador 3: "))
    i0 = float(input("Digite o valor da Intensidade 0 (I0): "))
    print("\n")
    
    calcI1 = (i0/2) #calcula a intensidade I1 apos passar do polarizador 1
    calcI2 = (calcI1 * pow(cos(rad(pol2 - pol1)), 2)) #calcula a intensidade I2 apos passar do polarizador 2
    calcI3 = (calcI2 * pow(cos(rad(pol3 - pol2)), 2)) #calcula a intensidade I3 apos passar do polarizador 3

    print("I1 = %.2f W/cm²" % calcI1)
    print("I2 = %.2f W/cm²" % calcI2)
    print("I3 = %.2f W/cm²" % calcI3)
  
    loop()

  elif(esc_polarizadores3 == 2):
    pol1 = float(input("Digite o valor do polarizador 1: "))
    pol2 = float(input("Digite o valor do polarizador 2: "))
    pol3 = float(input("Digite o valor do polarizador 3: "))
    i1 = float(input("Digite o valor da Intensidade 1 (I1): "))
    print("\n")
    
    calcI0 = (i1 * 2)
    calcI2 = (i1 * pow(cos(rad(pol2 - pol1)), 2))
    calcI3 = (calcI2 * pow(cos(rad(pol3 - pol2)), 2))

    print("I0 = %.2f W/cm²" % calcI0)
    print("I2 = %.2f W/cm²" % calcI2)
    print("I3 = %.2f W/cm²" % calcI3)
  
    loop()

  elif(esc_polarizadores3 == 3):
    pol1 = float(input("Digite o valor do polarizador 1: "))
    pol2 = float(input("Digite o valor do polarizador 2: "))
    pol3 = float(input("Digite o valor do polarizador 3: "))
    i2 = float(input("Digite o valor da Intensidade 2 (I2): "))
    print("\n")
    
    calcI1 = (i2 / pow(cos(rad(pol2 - pol1)), 2))
    calcI0 = (calcI1 * 2)
    calcI3 = (i2 * pow(cos(rad(pol3 - pol2)), 2))

    print("I0 = %.2f W/cm²" % calcI0)
    print("I1 = %.2f W/cm²" % calcI1)
    print("I3 = %.2f W/cm²" % calcI3)
  
    loop()

  elif(esc_polarizadores3 == 4):
    pol1 = float(input("Digite o valor do polarizador 1: "))
    pol2 = float(input("Digite o valor do polarizador 2: "))
    pol3 = float(input("Digite o valor do polarizador 3: "))
    i3 = float(input("Digite o valor da Intensidade 3 (I3): "))
    print("\n")
    
    calcI2 = (i3 / pow(cos(rad(pol3 - pol2)), 2))
    calcI1 = (calcI2 / pow(cos(rad(pol2 - pol1)), 2))
    calcI0 = (calcI1 * 2)

    print("I0 = %.2f W/cm²" % calcI0)
    print("I1 = %.2f W/cm²" % calcI1)
    print("I2 = %.2f W/cm²" % calcI2)
  
    loop()

#========================================================================================#

def menu():
  print("\n")
  print("Menu\n")
  print("1 - Calculo com 2 polarizadores")
  print("2 - Calculo com 3 polarizadores")
  print("\n")
  
  escolha = int(input("Digite o nº desejado: "))
  print("\n")

  if(escolha == 1):
    polarizadores2()

  elif(escolha == 2):
    polarizador3()

#=======================================================================================#

menu()
