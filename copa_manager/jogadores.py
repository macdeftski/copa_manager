from utils import ler_inteiro, pausar, ler_opcao, ler_texto

def cadastrar_jogador(jogadores, selecoes):
    if not selecoes:
        print("Nenhuma seleção cadastrada.")
        return

    print("\nSeleções disponíveis:")
    for s in selecoes:
        print(f"{s['id']} - {s['nome']}")

    selecao_id = ler_inteiro("Escolha o ID da seleção: ")

    selecao = None
    for s in selecoes:
        if s["id"] == selecao_id:
            selecao = s
            break

    if not selecao:
        print("Seleção inválida.")
        return

    if jogadores:
        novo_id = max(j["id"] for j in jogadores) + 1
    else:
        novo_id = 1

    nome = ler_texto("Nome do jogador: ")
    idade = ler_inteiro("Idade: ")
    posicao = ler_texto("Posição: ")
    gols = ler_inteiro("Gols: ")

    jogador = {
        "id": novo_id,
        "nome": nome,
        "idade": idade,
        "posicao": posicao,
        "gols": gols,
        "selecao_id": selecao_id
    }

    jogadores.append(jogador)
    print(f"[OK] Jogador {nome} cadastrado!")


def listar_jogadores(jogadores, selecoes):    
    if not jogadores:
        print("Nenhum jogador cadastrado.")
        return

    for j in jogadores:
        selecao_nome = "Desconhecida"

        for s in selecoes:
            if s["id"] == j["selecao_id"]:
                selecao_nome = s["nome"]
                break

        print(f"{j['nome']} - {j['posicao']} - {selecao_nome} - {j['gols']} gols")


def filtrar_por_posicao(jogadores, posicao):
    resultado = []
    for j in jogadores:
        if j["posicao"].lower() == posicao.lower():
            resultado.append(j)
    return resultado


def filtrar_por_idade(jogadores, min_idade, max_idade):
    resultado = []
    for j in jogadores:
        if min_idade <= j["idade"] <= max_idade:
            resultado.append(j)
    return resultado


def filtrar_por_selecao_nome(jogadores, selecoes, termo):
    resultado = []

    for j in jogadores:
        for s in selecoes:
            if j["selecao_id"] == s["id"]:
                if termo.lower() in s["nome"].lower():
                    resultado.append(j)

    return resultado


def ordenar_jogadores(jogadores, atributo, decrescente=False):
    if not jogadores:
        return []

    if atributo not in jogadores[0]:
        print("Atributo inválido.")
        return jogadores

    def chave(j):
        valor = j.get(atributo)

        if isinstance(valor, str):
            return valor.lower()

        if isinstance(valor, (int, float)):
            return valor

        return 0

    return sorted(jogadores, key=chave, reverse=decrescente)


def map_nomes(jogadores):
    nomes = []
    for j in jogadores:
        nomes.append(j["nome"])
    return nomes


def filtrar_atacantes(jogadores, min_gols):
    resultado = []
    for j in jogadores:
        if j["posicao"].lower() == "atacante" and j["gols"] > min_gols:
            resultado.append(j)
    return resultado


def total_gols(jogadores):
    total = 0
    for j in jogadores:
        total += j["gols"]
    return total


def media_idade(jogadores):
    if not jogadores:
        return 0

    total = 0
    for j in jogadores:
        total += j["idade"]

    return total / len(jogadores)


def artilheiro(jogadores):
    if not jogadores:
        return None

    melhor = jogadores[0]

    for j in jogadores:
        if j["gols"] > melhor["gols"]:
            melhor = j

    return melhor


def listar_posicoes(jogadores):
    posicoes = []

    for j in jogadores:
        if j["posicao"] not in posicoes:
            posicoes.append(j["posicao"])

    posicoes.sort()

    return posicoes