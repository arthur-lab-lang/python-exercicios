def converter_hora(hora, minuto):

    if hora == 0:
        hora_convertida = 12
        periodo = "A.M"

    elif hora < 12:
        hora_convertida = hora
        periodo = "A.M"

    elif hora == 12:
        hora_convertida = 12
        periodo = "P.M"

    else:
        hora_convertida = hora - 12
        periodo = "P.M"

    return hora_convertida, minuto, periodo


def mostrar_hora(hora, minuto, periodo):
    print(f"{hora}:{minuto} {periodo}")


while True:

    hora = int(input("Digite a hora: "))
    minuto = int(input("Digite o minuto: "))

    h, m, p = converter_hora(hora, minuto)

    mostrar_hora(h, m, p)

    continuar = input("Deseja continuar? (s/n): ")

    if continuar.lower() == "n":
        break
