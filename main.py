import json
import os
import time

arquivoEmpresas = "empresas.json"
arquivoEstudantes = "estudantes.json"
arquivoVagas = "vagas.json"

# --------------------------------------- FUNÇÕES GLOBAIS ------------------------------------------

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def PararOuContinuar():
    print("")
    opc = int(input("Deseja continuar?\n1 - Voltar | 2 - Encerrar o programa: "))
    if opc == 1:
        return True
    elif opc == 2:
        print("Finalizando o programa!")
        return False
    else:
        print("Opção inválida. Encerrando o programa!!! ")
        return False
    
def CadastrarNoJson (caminhoDoArquivo, dicionarioModelo):
    if os.path.exists(caminhoDoArquivo):
        with open(caminhoDoArquivo, 'r') as arquivo:
            try:
                dicionariosModelos = json.load(arquivo)
            except json.JSONDecodeError:
                dicionariosModelos = []
    else:
        dicionariosModelos = []
    
    dicionariosModelos.append(dicionarioModelo)
    
    with open(caminhoDoArquivo, 'w') as arquivo:
        json.dump(dicionariosModelos, arquivo, indent=4, ensure_ascii=False)
        
def VisualizarJson(caminhoDoArquivo):
    if os.path.exists(caminhoDoArquivo):
        with open(caminhoDoArquivo, 'r') as arquivo:
            try:
                dicionariosModelos = json.load(arquivo)
            except json.JSONDecodeError:
                dicionariosModelos = []
        
        if dicionariosModelos:
            i = 1
            for dicionario in dicionariosModelos:
                print(f"\nRegistro {i}:")
                print("*******************************")
                for chave, valor in dicionario.items():
                    print(f"{chave.capitalize()}: {valor}")
                print("*******************************")
                i += 1
                time.sleep(0.5)
            return True
        else:
            print("Nenhum registro encontrado.")
            return False
    else:
        print("Arquivo não encontrado.")

def AtualizarJson(caminhoDoArquivo, indice, novosDados):
    if os.path.exists(caminhoDoArquivo):
        with open(caminhoDoArquivo, 'r') as arquivo:
            try:
                dicionariosModelos = json.load(arquivo)
            except json.JSONDecodeError:
                dicionariosModelos = []

        if 1 <= indice <= len(dicionariosModelos):
            registro_atual = dicionariosModelos[indice - 1]

            # Atualiza somente os campos que não estão vazios
            for chave, valor in novosDados.items():
                if valor:  # Se o valor não for uma string vazia, atualiza
                    registro_atual[chave] = valor

            # Salva o registro atualizado no arquivo JSON
            with open(caminhoDoArquivo, 'w') as arquivo:
                json.dump(dicionariosModelos, arquivo, indent=4, ensure_ascii=False)

            print("Atualizando registro...")
            time.sleep(2)
            print("Registro atualizado com sucesso!")
        else:
            print("Índice inválido.")
    else:
        print("Arquivo não encontrado.")

def DeletarNoJson(caminhoDoArquivo, indice):
    if os.path.exists(caminhoDoArquivo):
        with open(caminhoDoArquivo, 'r') as arquivo:
            try:
                dicionariosModelos = json.load(arquivo)
            except json.JSONDecodeError:
                dicionariosModelos = []

        # Verifica se o índice está dentro do intervalo
        if 1 <= indice <= len(dicionariosModelos):
            # Remove o registro no índice especificado
            dicionariosModelos.pop(indice - 1)

            # Salva a lista atualizada no arquivo JSON
            with open(caminhoDoArquivo, 'w') as arquivo:
                json.dump(dicionariosModelos, arquivo, indent=4, ensure_ascii=False)

            print("Removendo registro...")
            time.sleep(2)
            print("Registro deletado com sucesso!")
        else:
            print("Índice inválido.")
    else:
        print("Arquivo não encontrado.")

   
# --------------------------------------- !MENU PRINCIPAL! --------------------------------------------------
    
def MenuPrincipal():
    limpar_console()
    print("Vagas de Estágios")
    print("Bem-vindo(a) ao Centro de Vagas!")
    print("Vamos começar?")
    print("1 - Sistema de Estudantes")
    print("2 - Sistema de Empresas")
    print("3 - Sistema de Vagas")
    print("0 - Encerrar o programa")
    
    opcMenuPrincipal = (int(input("Insira a opção desejada: ")))
    
    match(opcMenuPrincipal):
        case 1:
            print("Sistema de Estudantes...") #print temporário
        case 2:
            SistemaEmpresas()
        case 3:
            print("Sistema de Vagas...") #print temporário
        case 0:
            print("Encerrando o programa... Até mais!")
        case _:
            print("Opção inválida. Sistema encerrado.")

# --------------------------------------- !FUNÇÕES DO SISTEMA EMPRESA! ------------------------------------------
def SistemaEmpresas():
    while True:
        limpar_console()
        print("\n" + "=" * 40)
        print(f"{'CADASTRO: EMPRESAS':^40}")
        print("=" * 40)
        print("1 - Cadastrar Empresa")
        print("2 - Visualizar Empresas Cadastradas")
        print("3 - Atualizar informações da Empresa")
        print("4 - Excluir Empresa")
        print("5 - Voltar para o Menu Principal")
        print("0 - Encerrar o Programa")
        print("=" * 40)

        opc = int(input("\nSelecione uma opção: "))
        match(opc):
            case 1:
                limpar_console()
                empresaNome = input("Digite o nome da Empresa: ")
                empresaArea = input("Digite a área de atuação da Empresa: ")
                empresaEmail = input("Digite o e-mail da Empresa: ")
                empresaSite = input("Digite o site da empresa: ")
                empresaTelefone = input("Digite o telefone da Empresa: ")
                empresaEndereco = input("Digite o endereço da Empresa: ")
                empresa = {
                    "Nome": empresaNome,
                    "Area": empresaArea,
                    "Email": empresaEmail,
                    "Site": empresaSite,
                    "Telefone": empresaTelefone,
                    "Endereco": empresaEndereco
                }
                CadastrarNoJson(arquivoEmpresas, empresa)
            case 2:
                VisualizarJson(arquivoEmpresas)
            case 3:
                limpar_console()
                if VisualizarJson(arquivoEmpresas):  
                    indice = int(input("Digite o índice da empresa que deseja atualizar: "))
                    novo_nome = input("Digite o novo nome da Empresa (ou deixe em branco para manter o atual): ")
                    nova_area = input("Digite a nova área de atuação da Empresa (ou deixe em branco para manter a atual): ")
                    novo_email = input("Digite o novo e-mail da Empresa (ou deixe em branco para manter o atual): ")
                    novo_site = input("Digite o novo site da Empresa (ou deixe em branco para manter o atual): ")
                    novo_telefone = input("Digite o novo telefone da Empresa (ou deixe em branco para manter o atual): ")
                    novo_endereco = input("Digite o novo endereço da Empresa (ou deixe em branco para manter o atual): ")

                    novosDados = {
                        "Nome": novo_nome,
                        "Area": nova_area,
                        "Email": novo_email,
                        "Site": novo_site,
                        "Telefone": novo_telefone,
                        "Endereco": novo_endereco
                    }
                    AtualizarJson(arquivoEmpresas, indice, novosDados)
            case 4:
                limpar_console()
                VisualizarJson(arquivoEmpresas)
                indice = int(input("Digite o índice da Empresa que deseja excluir: "))
                DeletarNoJson(arquivoEmpresas, indice)
            case 5:
                MenuPrincipal()
                break
            case 0:
                print("Finalizando o programa!")
                return False
            case _:
                limpar_console()
                print("Opção inválida! Você voltará para o Menu.")
                print("-" * 10)
                continue

        if not PararOuContinuar():
            break



# --------------------------------------- !MAIN! ------------------------------------------

MenuPrincipal()
