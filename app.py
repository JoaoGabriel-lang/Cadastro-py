nome = input("Digite seu nome completo: ")
idade = int(input("Digite sua idade:"))
estudante = input("Você é estdudante?(Sim/Não):")


print("\nIforamções Cadastradas :")
print(f"Nome completo: {nome}")
print(f"Idade: {idade} anos")
if estudante == "Sim":
    print("á estudante: Sim ")
else:
    print("É estudante: Não")