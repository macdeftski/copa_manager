def ler_inteiro(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um número inteiro válido.")


def ler_texto(msg):
    while True:
        valor = input(msg).strip()
        if valor == "":
            print("Entrada não pode ser vazia.")
            continue
        return valor


def mostrar_titulo(texto):
    print("\n" + "="*len(texto))
    print(texto)
    print("="*len(texto))


def pausar():
    input("Pressione ENTER para voltar ao menu...")


def ler_opcao(msg, opcoes_validas):
    while True:
        try:
            valor = int(input(msg))
            if valor in opcoes_validas:
                return valor
            print(f"Opção inválida. Use: {opcoes_validas}")
        except ValueError:
            print("Digite um número válido.")