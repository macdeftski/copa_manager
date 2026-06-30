SEPARADOR = ";"


#PERSISTENCIA SELEÇÃO
def montar_linha_selecao(s):
    valores = [
        str(s["id"]),
        s["nome"],
        s["confederacao"],
        s["grupo"],
        str(s["ranking_fifa"]),
        str(s["titulos"]),
    ]
    return SEPARADOR.join(valores)


def montar_selecao_da_linha(linha):
    partes = linha.split(SEPARADOR)
    if len(partes) != 6:
        return None
    selecao = {
        "id": int(partes[0]),
        "nome": partes[1],
        "confederacao": partes[2],
        "grupo": partes[3],
        "ranking_fifa": int(partes[4]),
        "titulos": int(partes[5]),
    }
    return selecao


def carregar_selecoes(caminho):
    selecoes = []
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if not linha:
                    continue
                selecao = montar_selecao_da_linha(linha)
                if selecao:
                    selecoes.append(selecao)
    except FileNotFoundError:
        print("Arquivo de seleções ainda não existe. Começando com lista vazia.")
    return selecoes


def salvar_selecoes(caminho, selecoes):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        for s in selecoes:
            linha = montar_linha_selecao(s)
            arquivo.write(linha + "\n")
    print("Seleções salvas com sucesso!")


#PERSISTENCIA JOGADORES
def montar_linha_jogadores(s):
    valores = [
        str(s["id"]),
        s["nome"],
        str(s["selecao_id"]),
        s["posicao"],
        str(s["idade"]),
        str(s["gols"]),
    ]
    return SEPARADOR.join(valores)


def montar_jogadores_da_linha(linha):
    partes = linha.split(SEPARADOR)
    if len(partes) != 6:
        return None
    jogador = {
        "id": int(partes[0]),
        "nome": partes[1],
        "selecao_id": int(partes[2]),
        "posicao": partes[3],
        "idade": int(partes[4]),
        "gols": int(partes[5]),
    }
    return jogador


def carregar_jogadores(caminho):
    jogadores = []
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if not linha:
                    continue
                jogador = montar_jogadores_da_linha(linha)
                if jogador:
                    jogadores.append(jogador)
    except FileNotFoundError:
        print("Arquivo de jogadores ainda não existe. Começando com lista vazia.")
    return jogadores


def salvar_jogadores(caminho, jogadores):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        for s in jogadores:
            linha = montar_linha_jogadores(s)
            arquivo.write(linha + "\n")
    print("Jogadores salvos com sucesso!")


# PERSISTENCIA PARTIDAS

def montar_linha_partida(p):
    valores = [
        str(p["id"]),
        str(p["casa_id"]),
        str(p["visitante_id"]),
        str(p["gols_casa"]),
        str(p["gols_visitante"]),
        p["fase"],
    ]
    return SEPARADOR.join(valores)


def montar_partida_da_linha(linha):
    partes = linha.split(SEPARADOR)

    if len(partes) != 6:
        return None

    partida = {
        "id": int(partes[0]),
        "casa_id": int(partes[1]),
        "visitante_id": int(partes[2]),
        "gols_casa": int(partes[3]),
        "gols_visitante": int(partes[4]),
        "fase": partes[5],
    }

    return partida


def carregar_partidas(caminho):
    partidas = []

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()

                if not linha:
                    continue

                partida = montar_partida_da_linha(linha)

                if partida:
                    partidas.append(partida)

    except FileNotFoundError:
        print("Arquivo de partidas ainda não existe. Começando com lista vazia.")

    return partidas


def salvar_partidas(caminho, partidas):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        for p in partidas:
            linha = montar_linha_partida(p)
            arquivo.write(linha + "\n")

    print("Partidas salvas com sucesso!")