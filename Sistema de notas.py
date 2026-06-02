alunos = {}

def adicionar_aluno(nome, nota):
    alunos[nome] = nota
    print(f"{nome} adicionado com nota {nota:.1f}")

def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    print("\n --- Lista de Alunos ---")
    for nome, nota in alunos.items():
        status = "Aprovado" if nota >= 6 else "Reprovado"
        print(f"{nome}: {nota:.1f} - {status}")

def media_turma():
    if not alunos:
        print("Sem dados.")
        return
    media = sum(alunos.values()) / len(alunos)
    print(f"\nMédia da turma: {media:.2f}")

def menu():
    while True:
        print("\n === MENU ===")
        print("1. Adicionar aluno")
        print("2. Listar alunos")
        print("3. Média da turma")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do aluno: ")
            nota = float(input('Nota (0-10): '))
            adicionar_aluno(nome, nota)
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            media_turma()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()