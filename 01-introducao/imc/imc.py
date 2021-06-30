escala_imc = {
    "map": "muito abaixo do peso",
    "ap": "abaixo do peso",
    "pi": "peso ideal",
    "ac": "acima do peso",
    "ob1": "obesidade 1",
    "ob2": "obesidade 2",
    "ob3": "obesidade 3",
}

def calcular_imc(peso_kg: float, altura_m: float) -> tuple[float, str]:
    imc = peso_kg / altura_m **2

    if imc < 17:
        situacao = "map"

    elif imc < 17.5:
        situacao = "ap"

    elif imc < 25:
        situacao = "pi"

    elif imc < 30:
        situacao = "ap"

    elif imc < 35:
        situacao = "ob1"

    elif imc < 40:
        situacao = "ob2"

    else:
        situacao = "ob3"

    saida = (imc, situacao)

    return saida

def main():

    try:
        peso = float(input("Digite seu peso em Kg: "))
        altura = float(input("Digite sua altura em metros: "))

    except ValueError:
        print("O valor fornecido não é valido")
        return

    (imc, referencia) = calcular_imc(peso, altura)

    situacao = escala_imc[referencia]

    print("Seu IMC é", imc)
    print("A sua situação é", situacao)

if __name__ == "__main__":
    main()