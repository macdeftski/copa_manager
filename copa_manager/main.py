from selecoes import cadastrar_selecao, listar_selecoes, buscar_selecao_por_nome, filtrar_selecoes, ordenar_por_atributo
from persistencia import carregar_selecoes, salvar_selecoes, carregar_jogadores, salvar_jogadores, carregar_partidas, salvar_partidas
from utils import ler_inteiro, pausar, ler_opcao, ler_texto
from menus import menu_selecoes, menu_jogadores, menu_partidas

def main():
    selecoes = carregar_selecoes("copa_manager/selecoes.txt")
    jogadores = carregar_jogadores("copa_manager/jogadores.txt")
    partidas = carregar_partidas("copa_manager/partidas.txt")

    while True:
        print("="*60)
        print("⚽COPA MANAGER 2026 - FIFA⚽")
        print("="*60)
        print(f"Status: {len(selecoes)} seleções cadastradas")
        print("""
Selecione uma opção (abrirá um sub-menu):
1. Seleções
2. Jogadores
3. Partidas
0. Sair (salva automaticamente)""")

        opcao = ler_opcao("Escolha uma opção: ", [0,1,2,3])

        if opcao == 1:
            menu_selecoes(selecoes)

        elif opcao == 2:
            menu_jogadores(jogadores, selecoes)

        elif opcao == 3:
            menu_partidas(partidas, selecoes)

        elif opcao == 0:
            print("Salvando seleções...")
            salvar_selecoes("copa_manager/selecoes.txt", selecoes)
            salvar_jogadores("copa_manager/jogadores.txt", jogadores)
            salvar_partidas("copa_manager/partidas.txt", partidas)
            print("Até a próxima!")
            break


main()