nascimento = int(input("Digite o ano de nascimento: "))
idade = 2026 - nascimento
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")