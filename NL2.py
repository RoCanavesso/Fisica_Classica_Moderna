from math import pow, sqrt

print("Membros do grupo: \n")

print("Lucas Antunes Sampaio - 24.122.056-5")
print("Romulo Carneiro de Oliveira Canavesso - 24.122.093-8\n\n")

print("O que são os atomos de Bohr?\n")
print("O modelo atomico de Bohr foi baseado na ideia de que o átomo é formado por um núcleo (composto por protons e neutrons) e uma eletrosfera, onde os elétrons ficam orbitando o núcleo atômico.\n\n Nessa eletrosfera, exitem 7 camadas diferentes, nomeadas de K a Q, onde a camada K é a menos energética e a Q a mais energética sendo também o limite do átomo de hidrogênio.\n\n Dessa forma, o elétron pode saltar de camada dependendo da quantidade de energia que ele pode receber.\n\n")

def menu():
  print("Menu: \n")

  print("1 - Propriedades do átomo de H")
  print("2 - Emissão/Absorção de fóton pelo H")
  print("3 - Absorção de fóton pelo H")
  print("4 - Emissão de fóton pelo H\n")

menu()

escolha = int(input("Escolha uma opção: "))
print("\n")
  
h = (4.136 * pow(10, (-15)))
c = (3 * pow(10, 8))

def prop_at():
  n = float(input("Digite o valor de n: "))
  print("\n")
  r = pow(n,2)*(5.29*pow(10,(-11)))
  v = ((2.187 * pow(10,6)) / n)
  y = ((6.626 * pow(10,(-34)))/((9.11 * pow(10,(-31))) * v))
  K = (13.6 / pow(n,2))
  U = ((-27.2) / pow(n,2))
  E = ((-13.6) / pow(n,2))

  print("rn = {:.2e} m" .format(r))
  print("vn = {:.2e} m/s" .format(v))
  print("λ = {:.2e} m" .format(y))
  print("Kn = {:.2e} eV" .format(K))
  print("Un = {:.2e} eV" .format(U))
  print("En = {:.2e} eV" .format(E))
  
  
def ems_abs():
  n_inicial = float(input("Digite o n inicial (ni): "))
  n_final = float(input("Digite o n final (nf): "))
  
  En_inicial = (-13.6 / pow(n_inicial, 2))
  En_final = (-13.6 / pow(n_final, 2))
  
  Eabsorvida = sqrt(pow((En_final - En_inicial), 2))
  
  f = (Eabsorvida/(4.136 * pow(10, (-15))))
  
  lamb = (((4.136 * pow(10, (-15)))*(3*pow(10,8)))/Eabsorvida)

  print("\n")
  
  print("Efóton (Energia de fóton) = {:.2e} eV" .format(Eabsorvida))
  print("λfóton (Comprimento de onda (λ) do fóton) = {:.2e} m" .format(lamb))
  print("Ffóton (Frequencia do fóton) = {:.2e} Hz" .format(f))
    
  
def abs_foton():
    nescolha = int(input("Deseja usar o N inicial (1) ou N final (2): "))
    if nescolha == 1:
      n_inicial = float(input("Digite o n inicial: "))
  
      perg_f_y = int(input("Deseja utilizar Lambda (1) ou Frequencia (2): "))
  
      if perg_f_y == 1:
        lamb = float(input("Digite o valor de λ: "))
        Eini = -(13.6)/pow(n_inicial,2)
        Efot = h*c/lamb
        Ef = sqrt(pow(Eini + Efot,2))
        n = sqrt(13.6/Ef)
        print("Nf = {:.2e}" .format(n))
        
      elif perg_f_y == 2:
        perg_f = float(input("Digite o valor da frequencia: "))
        Eini = -(13.6)/pow(n_inicial,2)
        Efot = h*perg_f
        Ef = sqrt(pow(Eini + Efot,2))
        n = sqrt(13.6/Ef)
        print("Nf = {:.2e}" .format(n))
      
    elif nescolha == 2:
      n_final = float(input("Digite o N final: "))
      perg_f_y2 = int(input("Deseja utilizar Lambda (1) ou Frequencia (2): "))

      if perg_f_y2 == 1:
        lamb = float(input("Digite o valor de λ: "))
        Efinal = -(13.6)/pow(n_final,2)
        Efot = h*c/lamb
        Ef = sqrt(pow(Efinal - Efot,2))
        n = sqrt(13.6/Ef)
        print("Nf = {:.2e}" .format(n))
          
      elif perg_f_y2 == 2:
        freq = float(input("Digite o valor da frequencia: "))
        Efinal = -(13.6)/pow(n_final,2)
        Efot = h*freq
        Ef = sqrt(pow(Efinal - Efot,2))
        n = sqrt(13.6/Ef)
        print("Nf = {:.2e}" .format(n))

  
def ems_foton():
  nnescolha = int(input("Deseja usar o N inicial (1) ou N final (2): "))
  if nnescolha == 1:
    n_inicial = float(input("Digite o n inicial: "))
  
    perg_f_yy = int(input("Deseja utilizar Lambda (1) ou Frequencia (2): "))
  
    if perg_f_yy == 1:
      lamb = float(input("Digite o valor de λ: "))
      Eini = -(13.6)/pow(n_inicial,2)
      Efot = h*c/lamb
      Ef = sqrt(pow(Eini - Efot,2))
      n = sqrt(13.6/Ef)
      print("Nf = {:.2e}" .format(n))
      
    elif perg_f_yy == 2:
      perg_f = float(input("Digite o valor da frequencia: "))
      Eini = -(13.6)/pow(n_inicial,2)
      Efot = h*perg_f
      Ef = sqrt(pow(Eini - Efot,2))
      n = sqrt(13.6/Ef)
      print("Nf = {:.2e}" .format(n))
      
  elif nnescolha == 2:
    n_final = float(input("Digite o N final: "))
    perg_f_yy2 = int(input("Deseja utilizar Lambda (1) ou Frequencia (2): "))

    if perg_f_yy2 == 1:
      lamb = float(input("Digite o valor de λ: "))
      Efinal = -(13.6)/pow(n_final,2)
      Efot = h*c/lamb
      Ef = sqrt(pow(Efinal + Efot,2))
      n = sqrt(13.6/Ef)
      print("Nf = {:.2e}" .format(n))
      
    elif perg_f_yy2 == 2:
      freq = float(input("Digite o valor da frequencia: "))
      Efinal = -(13.6)/pow(n_final,2)
      Efot = h*freq
      Ef = sqrt(pow(Efinal + Efot,2))
      n = sqrt(13.6/Ef)
      print("Nf = {:.2e}" .format(n))
      

if escolha == 1:
  prop_at() #ta certo mas conferir novamente para ter ctz
  menu_escolher = int(input("\nDeseja voltar ao menu principal? (1) -> Sim ou (2) -> Não: "))

elif escolha == 2: #CERTO
  ems_abs()
  menu_escolher = int(input("\nDeseja voltar ao menu principal? (1) -> Sim ou (2) -> Não: "))
  
elif escolha == 3:
  abs_foton() #certo
  menu_escolher = int(input("\nDeseja voltar ao menu principal? (1) -> Sim ou (2) -> Não: "))

elif escolha == 4:
  ems_foton()#certo
  menu_escolher = int(input("\nDeseja voltar ao menu principal? (1) -> Sim ou (2) -> Não: "))


while menu_escolher == 1:
  print()
  menu()
  r = 0
  v = 0
  y = 0
  K = 0
  U = 0
  E = 0
  Eini = 0
  Efot = 0
  Ef = 0
  n = 0
  Efinal = 0
  En_inicial = 0
  En_final = 0
  Eabsorvido = 0
  f = 0
  lamb = 0
  
  escolha = int(input("Escolha uma opção: "))
  print("\n")

  if escolha == 1:
    prop_at() #ta certo mas conferir novamente para ter ctz
    menu_escolher = int(input("\nDeseja voltar ao menu principal? (1) -> Sim ou (2) -> Não: "))

  elif escolha == 2: #CERTO
    ems_abs()
    menu_escolher = int(input("\nDeseja voltar ao menu principal? (1) -> Sim ou (2) -> Não: "))

  elif escolha == 3:
    abs_foton() #certo
    menu_escolher = int(input("\nDeseja voltar ao menu principal? (1) -> Sim ou (2) -> Não: "))

  elif escolha == 4:
    ems_foton()#certo
    menu_escolher = int(input("\nDeseja voltar ao menu principal? (1) -> Sim ou (2) -> Não: "))
