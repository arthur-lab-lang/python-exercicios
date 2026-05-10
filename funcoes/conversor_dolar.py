def converter_dolar(valor_dolar, cotacao):

    valor_convertido = valor_dolar * cotacao

    return valor_convertido


print("=== CONVERSOR DÓLAR → REAL ===")

dolar = float(input("Digite o valor em dólar: "))
cotacao = float(input("Digite a cotação atual do dólar: "))

resultado = converter_dolar(dolar, cotacao)

print(f"Valor convertido: R${resultado:.2f}")
