from utils import ler_inteiro, ler_opcao

def cadastrar_partida(partidas, selecoes):
    if len(selecoes) < 2:
        print("É necessário haver pelo menos duas seleções cadastradas.")
        return

    if partidas:
        novo_id = max(p["id"] for p in partidas) + 1
    else:
        novo_id = 1

    print("\nSeleções cadastradas:")
    listar_selecoes_resumido(selecoes)

    while True:
        casa_id = ler_inteiro("ID da seleção da casa: ")

        casa_existe = False
        for s in selecoes:
            if s["id"] == casa_id:
                casa_existe = True
                break

        if casa_existe:
            break

        print("Seleção inválida.")

    while True:
        visitante_id = ler_inteiro("ID da seleção visitante: ")

        if visitante_id == casa_id:
            print("A seleção visitante deve ser diferente da seleção da casa.")
            continue

        visitante_existe = False
        for s in selecoes:
            if s["id"] == visitante_id:
                visitante_existe = True
                break

        if visitante_existe:
            break

        print("Seleção inválida.")

    gols_casa = ler_inteiro("Gols da casa: ")
    gols_visitante = ler_inteiro("Gols do visitante: ")

    fase_opcao = ler_opcao("""
Escolha a fase:
1 - Grupos
2 - Oitavas
3 - Quartas
4 - Semifinal
5 - Terceiro Lugar
6 - Final
> """, [1,2,3,4,5,6])

    mapa_fases = {
        1: "Grupos",
        2: "Oitavas",
        3: "Quartas",
        4: "Semifinal",
        5: "Terceiro Lugar",
        6: "Final"
    }

    partida = {
        "id": novo_id,
        "casa_id": casa_id,
        "visitante_id": visitante_id,
        "gols_casa": gols_casa,
        "gols_visitante": gols_visitante,
        "fase": mapa_fases[fase_opcao]
    }

    partidas.append(partida)

    print("Partida cadastrada com sucesso!")


def listar_partidas(partidas, selecoes):
    if not partidas:
        print("Nenhuma partida cadastrada.")
        return

    for p in partidas:
        casa = obter_nome_selecao(selecoes, p["casa_id"])
        visitante = obter_nome_selecao(selecoes, p["visitante_id"])

        print(f"{casa} {p['gols_casa']} x {p['gols_visitante']} {visitante} ({p['fase']})")


def filtrar_partidas_por_fase(partidas, fase):
    resultado = []

    for p in partidas:
        if p["fase"].lower() == fase.lower():
            resultado.append(p)

    return resultado


def ordenar_partidas(partidas, atributo, decrescente=False):
    if not partidas:
        return []

    if atributo not in partidas[0]:
        print("Atributo inválido.")
        return partidas

    def chave(partida):
        valor = partida[atributo]
        if isinstance(valor, str):
            return valor.lower()
        return valor
    return sorted(partidas, key=chave, reverse=decrescente)


def listar_fases(partidas):
    fases = []

    for p in partidas:
        if p["fase"] not in fases:
            fases.append(p["fase"])

    fases.sort()

    return fases


def obter_nome_selecao(selecoes, id_selecao):
    for s in selecoes:
        if s["id"] == id_selecao:
            return s["nome"]

    return "Desconhecida"


def listar_selecoes_resumido(selecoes):
    for s in selecoes:
        print(f"{s['id']} - {s['nome']}")


def calcular_estatisticas(selecao, partidas):
    pontos = 0
    saldo = 0
    gols_pro = 0

    for p in partidas:

        # jogando em casa
        if p["casa_id"] == selecao["id"]:

            gols_pro += p["gols_casa"]
            saldo += p["gols_casa"] - p["gols_visitante"]

            if p["gols_casa"] > p["gols_visitante"]:
                pontos += 3

            elif p["gols_casa"] == p["gols_visitante"]:
                pontos += 1

        # jogand como visitante
        elif p["visitante_id"] == selecao["id"]:

            gols_pro += p["gols_visitante"]
            saldo += p["gols_visitante"] - p["gols_casa"]

            if p["gols_visitante"] > p["gols_casa"]:
                pontos += 3

            elif p["gols_visitante"] == p["gols_casa"]:
                pontos += 1

    return {
        "id": selecao["id"],
        "nome": selecao["nome"],
        "pontos": pontos,
        "saldo": saldo,
        "gols_pro": gols_pro
    }


def tabela_classificacao(selecoes, partidas, grupo):

    tabela = []

    for s in selecoes:

        if s["grupo"].lower() == grupo.lower():

            estatisticas = calcular_estatisticas(s, partidas)

            tabela.append(estatisticas)

    def chave(item):
        return (
            item["pontos"],
            item["saldo"],
            item["gols_pro"]
        )

    tabela = sorted(
        tabela,
        key=chave,
        reverse=True
    )

    return tabela


def listar_classificacao(classificacao):

    if not classificacao:
        print("Nenhuma seleção encontrada.")
        return

    print()

    print(f"{'Pos':<5}{'Seleção':<20}{'Pts':<6}{'SG':<6}{'GP':<6}")

    print("-" * 45)

    posicao = 1

    for s in classificacao:

        print(
            f"{posicao:<5}"
            f"{s['nome']:<20}"
            f"{s['pontos']:<6}"
            f"{s['saldo']:<6}"
            f"{s['gols_pro']:<6}"
        )

        posicao += 1


def total_gols_copa(partidas):
    total = 0

    for p in partidas:
        total += p["gols_casa"]
        total += p["gols_visitante"]

    return total


def media_gols(partidas):
    if not partidas:
        return 0

    total = total_gols_copa(partidas)

    return round(total / len(partidas), 2)


