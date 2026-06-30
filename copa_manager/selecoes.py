from persistencia import salvar_selecoes

def cadastrar_selecao(selecoes):
    if selecoes:
        novo_id = max(s["id"] for s in selecoes) + 1
    else:
        novo_id = 1
    nome = input("Nome da seleção: ").strip()
    confed = input("Confederação: ").strip()
    grupo = input("Grupo: ").strip().upper()
    ranking = int(input("Ranking FIFA: "))
    titulos = int(input("Títulos: "))
    nova = {
        "id": novo_id,
        "nome": nome,
        "confederacao": confed,
        "grupo": grupo,
        "ranking_fifa": ranking,
        "titulos": titulos,
    }
    selecoes.append(nova)
    print(f"[OK] Seleção '{nome}' cadastrada com ID {novo_id}!")


def listar_selecoes(selecoes):
    if not selecoes:
        print("Nenhuma seleção para mostrar.")
        return
    print(f"{'ID':<4} {'Nome':<15} {'Confederação':<12} {'Grupo':<6} {'Ranking':<8} {'Títulos':<7}")
    print("-"*60)
    for s in selecoes:
        print(f"{s['id']:<4} {s['nome']:<15} {s['confederacao']:<12} {s['grupo']:<6} {s['ranking_fifa']:<8} {s['titulos']:<7}")


def buscar_selecao_por_nome(selecoes, termo):
    if not isinstance(termo, str):
        return []
    termo = termo.strip().lower()
    if termo == "":
        return []
    encontrados = []
    for s in selecoes:
        nome = s.get("nome", "")
        if not isinstance(nome, str):
            continue
        if termo in nome.lower():
            encontrados.append(s)
    return encontrados


def filtrar_selecoes(selecoes, tipo, valor):
    if not isinstance(tipo, str) or not isinstance(valor, str):
        return []
    tipo = tipo.strip().lower()
    valor = valor.strip().lower()
    if valor == "":
        return []
    resultado = []
    for s in selecoes:
        if tipo == "grupo":
            campo = s.get("grupo", "")
        elif tipo == "confederacao":
            campo = s.get("confederacao", "")
        else:
            return []
        if not isinstance(campo, str):
            continue
        if campo.strip().lower() == valor:
            resultado.append(s)
    return resultado


def ordenar_por_atributo(lista, atributo, decrescente=False):
    if not isinstance(lista, list):
        return []
    if not isinstance(atributo, str):
        return list
    atributo = atributo.strip()
    if len(lista) == 0:
        return lista
    if atributo not in lista[0]:
        print(f"[ERRO] Atributo '{atributo}' não existe.")
        return lista
    def chave(item):
        valor = item.get(atributo, None)
        if isinstance(valor, str):
            return valor.lower()
        if isinstance(valor, (int, float)):
            return valor
        return float("-inf") if decrescente else float("inf")
    return sorted(lista, key=chave, reverse=decrescente)


def listar_grupos(selecoes):
    grupos = []

    for s in selecoes:
        if s["grupo"] not in grupos:
            grupos.append(s["grupo"])

    grupos.sort()

    return grupos