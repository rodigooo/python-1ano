nome = input("Como te chamas? ")
nascimento = int(input("Quando nasceste? "))
if 2026 - nascimento < 18:
    print("Ainda não tens idade para continuar")
    quit()
classe = input("Qual é a tua classe? ")
especialidade = input("Qual é a tua especialidade? ")

forca = int(input("Força: "))

if forca < 5:
    forcaMsg = "Fracote"
elif 10 > forca >= 5:
    forcaMsg = "Forte"
elif forca >= 10:
    forcaMsg = "Hulk"
print(forcaMsg)

inteligencia = int(input("Inteligência: "))

if inteligencia < 5:
    inteligenciaMsg = "Estuda mais"
elif inteligencia >= 5:
    inteligenciaMsg = "Espertalhão"
print(inteligenciaMsg)

criatividade = int(input("Criatividade: "))

if criatividade < 5:
    criatividadeMsg = "Podes melhorar"
elif criatividade >= 5:
    criatividadeMsg = "Não há melhor que tu!"
print(criatividadeMsg)

persistencia = int(input("Persistência: "))

if persistencia < 5:
    persistenciaMsg = "Não desistas"
elif persistencia >= 5:
    persistenciaMsg = "Corajoso"
print(persistenciaMsg)

humor = int(input("Humor: "))

if humor < 5:
    humorMsg = "Estás zangado?"
elif humor >= 5:
    humorMsg = "Que bom"
print(humorMsg)

print()
print("======================")
print("=== Ficha do Herói ===")
print("======================")
print(f"Nome: {nome}")
print(f"Idade:  {2026 - nascimento}")
print(f"Classe: {classe}")
print(f"Especialidade: {especialidade}")
print()
print("====================")
print("=== Estatísticas ===")
print("====================")
print(f"Força:\t\t\t{forca}")
print(f"Inteligencia:\t{inteligencia}")
print(f"Criatividade:\t{criatividade}")
print(f"Persistencia:\t{persistencia}")
print(f"Humor:\t\t\t{humor}")