def calcular_imc(peso, altura):

    imc = peso / (altura * altura)

    return imc


print("=== CALCULADORA DE IMC ===")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

resultado = calcular_imc(peso, altura)

print(f"Seu IMC é: {resultado:.2f}")


if resultado < 18.5:
    print("Você está abaixo do peso.")

elif resultado < 25:
    print("Peso normal.")

elif resultado < 30:
    print("Sobrepeso.")

else:
    print("Obesidade.")
