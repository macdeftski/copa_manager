from selecoes import cadastrar_selecao, listar_selecoes, buscar_selecao_por_nome, filtrar_selecoes, ordenar_por_atributo, listar_grupos
from jogadores import cadastrar_jogador, listar_jogadores, filtrar_por_posicao, filtrar_por_idade, filtrar_por_selecao_nome, ordenar_jogadores, map_nomes, filtrar_atacantes, total_gols, media_idade, artilheiro, listar_posicoes
from partidas import total_gols_copa, media_gols, listar_classificacao, tabela_classificacao, calcular_estatisticas, listar_selecoes_resumido, obter_nome_selecao, listar_fases, ordenar_partidas, filtrar_partidas_por_fase, listar_partidas, cadastrar_partida
from persistencia import salvar_selecoes, salvar_jogadores, salvar_partidas
from utils import ler_inteiro, pausar, ler_opcao, ler_texto

def menu_selecoes(selecoes):
    while True:
        print("\n=== SELEÇÕES ===")
        print("1 - Cadastrar seleção")
        print("2 - Listar / Ordenar seleções")
        print("3 - Buscar seleção por nome")
        print("4 - Filtrar seleções")
        print("0 - Voltar")
        op = ler_opcao("Escolha: ", [0,1,2,3,4])

        #voltar pro menu inicial
        if op == 0:
            break
        #cadastrar uma seleção
        elif op == 1:
            cadastrar_selecao(selecoes)
            salvar_selecoes("copa_manager/selecoes.txt", selecoes)
            pausar()
        #listar e ordenar eas seleções
        elif op == 2:
            ordenar = ler_opcao("""
Ordenar por:
1 - Nome
2 - Ranking FIFA
3 - Títulos
> """, [1,2,3])
            ordem = ler_opcao("""
Ordem:
1 - Crescente
2 - Decrescente
> """, [1,2])
            mapa = {
                1: "nome",
                2: "ranking_fifa",
                3: "titulos"
            }
            atributo = mapa[ordenar]
            decrescente = (ordem == 2)
            resultado = ordenar_por_atributo(selecoes, atributo, decrescente)
            listar_selecoes(resultado)
            pausar()
        #buscar seleções
        elif op == 3:
            termo = ler_texto("Digite parte do nome: ")
            encontrados = buscar_selecao_por_nome(selecoes, termo)
            listar_selecoes(encontrados)
            pausar()
        #filtrar seleç~oes
        elif op == 4:
            tipo = ler_opcao("""
Filtrar por:
1 - Grupo
2 - Confederação
> """, [1,2])
            mapa = {
                1: "grupo",
                2: "confederacao"
            }
            valor = ler_texto("Digite o valor: ")
            filtradas = filtrar_selecoes(
                selecoes,
                mapa[tipo],
                valor
            )
            listar_selecoes(filtradas)
            pausar()


def menu_jogadores(jogadores, selecoes):
    while True:
        print("\n=== JOGADORES ===")
        print("1 - Cadastrar jogador")
        print("2 - Listar jogadores")
        print("3 - Filtrar jogadores")
        print("4 - Artilheiro")
        print("5 - Estatísticas (Map/Filter/Reduce)")
        print("0 - Voltar")
        op = ler_opcao("Escolha: ", [0,1,2,3,4,5])

        #voltar pro menu inicial
        if op == 0:
            break
        #cadastrar jogadores
        elif op == 1:
            cadastrar_jogador(jogadores, selecoes)
            salvar_jogadores("copa_manager/jogadores.txt", jogadores)
            pausar()
        #listar jogadores
        elif op == 2:
            listar_jogadores(jogadores, selecoes)
            pausar()
        #filtrar jogadores
        elif op == 3:
            print("\n=== FILTRO ===")
            print("1 - Por posição")
            print("2 - Por idade")
            print("3 - Por seleção")
            f = ler_opcao("Escolha filtro: ", [1,2,3])
            if f == 1:
                posicoes = listar_posicoes(jogadores)
                if not posicoes:
                    print("Nenhum jogador cadastrado.")
                    pausar()
                    continue
                print("\nPosições disponíveis:")
                for p in posicoes:
                    print(f"- {p}")
                pos = ler_texto("\nPosição: ")
                resultado = filtrar_por_posicao(jogadores, pos)
            elif f == 2:
                min_idade = ler_inteiro("Idade mínima: ")
                max_idade = ler_inteiro("Idade máxima: ")
                resultado = filtrar_por_idade(jogadores, min_idade, max_idade)
            elif f == 3:
                termo = ler_texto("Nome da seleção: ")
                resultado = filtrar_por_selecao_nome(jogadores, selecoes, termo)
            listar_jogadores(resultado, selecoes)
            pausar()
        #listar artilheiro(s)
        elif op == 4:
            jogador = artilheiro(jogadores)
            if jogador:
                listar_jogadores([jogador], selecoes)
            else:
                print("Nenhum jogador cadastrado.")
            pausar()
        #menu de estatísticas
        elif op == 5:
            print("\n=== ESTATÍSTICAS ===")
            print("1 - Map (nomes)")
            print("2 - Filter (atacantes + gols)")
            print("3 - Reduce (total gols / média idade)")
            e = ler_opcao("Escolha: ", [1,2,3])
            if e == 1:
                print(map_nomes(jogadores))
            elif e == 2:
                n = ler_inteiro("Mínimo de gols: ")
                print(filtrar_atacantes(jogadores, n))
            elif e == 3:
                print("Total gols:", total_gols(jogadores))
                print("Média idade:", media_idade(jogadores))
            pausar()


def menu_partidas(partidas, selecoes):
    while True:
        print("\n=== PARTIDAS ===")
        print("1 - Cadastrar partida")
        print("2 - Listar partidas")
        print("3 - Classificação")
        print("4 - Filtrar partidas por fase")
        print("5 - Estatísticas")
        print("0 - Voltar")

        op = ler_opcao("Escolha: ", [0,1,2,3,4,5])

        # voltar
        if op == 0:
            break

        # cadastrar partida
        elif op == 1:
            cadastrar_partida(partidas, selecoes)
            salvar_partidas("copa_manager/partidas.txt", partidas)
            pausar()

        # listar partidas
        elif op == 2:
            listar_partidas(partidas, selecoes)
            pausar()

        # classificação
        elif op == 3:

            grupos = listar_grupos(selecoes)

            if not grupos:
                print("Nenhuma seleção cadastrada.")
                pausar()
                continue

            print("\nGrupos disponíveis:")

            for g in grupos:
                print("-", g)

            grupo = ler_texto("\nGrupo: ").upper()

            classificacao = tabela_classificacao(
                selecoes,
                partidas,
                grupo
            )

            listar_classificacao(classificacao)

            pausar()
        # filtrar partidas
        elif op == 4:

            fases = listar_fases(partidas)

            if not fases:
                print("Nenhuma partida cadastrada.")
                pausar()
                continue

            print("\nFases disponíveis:")

            for f in fases:
                print("-", f)

            fase = ler_texto("\nFase: ")

            resultado = filtrar_partidas_por_fase(partidas, fase)

            listar_partidas(resultado, selecoes)
            pausar()

        # estatísticas
        elif op == 5:

            print("\n=== ESTATÍSTICAS ===")
            print("1 - Total de gols da Copa")
            print("2 - Média de gols por partida")

            e = ler_opcao("Escolha: ", [1,2])

            if e == 1:
                print("Total de gols:", total_gols_copa(partidas))

            elif e == 2:
                print("Média de gols:", media_gols(partidas))

            pausar()