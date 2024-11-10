import json
import os
import time

# Arquivos JSON
arquivoEmpresas = "Database/empresas.json"
arquivoEstudantes = "Database/estudantes.json"
arquivoVagas = "Database/vagas.json"

# --------------------------------------- FUNÇÕES GLOBAIS ------------------------------------------

def Limpar_Console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def PararOuContinuar():
    print("")
    while True:
        try:
            # Tentativa de conversão da entrada para int
            opc = int(input("Deseja continuar?\n1 - Voltar | 2 - Encerrar o programa: "))
            
            if opc == 1:
                return True
            elif opc == 2:
                print("Finalizando o programa!")
                return False
            else:
                print("Opção inválida. Digite uma opção válida.")
        
        except ValueError:
            # Se não for possível converter para int, o ValueError será lançado
            print("Entrada inválida! Por favor, digite um número inteiro (1 ou 2).")


def LerArquivo(caminhoDoArquivo):
    if os.path.exists(caminhoDoArquivo):
        with open(caminhoDoArquivo, 'r', encoding="utf8") as arquivo:
            try:
                dicionariosModelos = json.load(arquivo)
            except json.JSONDecodeError:
                dicionariosModelos = []
    else:
        dicionariosModelos = []
    return dicionariosModelos

def ValidarIndice(caminhoDoArquivo,indice):
    dicionariosModelos = LerArquivo(caminhoDoArquivo)
    id_encontrado = False
    for dicionario in dicionariosModelos:
        if dicionario['Id'] == indice:
            id_encontrado = True
            break
    if not id_encontrado:
        print("ID inválido.")
        return False
    return True


def CadastrarNoJson (caminhoDoArquivo, dicionarioModelo):
    dicionariosModelos = LerArquivo(caminhoDoArquivo)
    dicionariosModelos.append(dicionarioModelo)
    
    with open(caminhoDoArquivo, 'w', encoding="utf8") as arquivo:
        json.dump(dicionariosModelos, arquivo, indent=4, ensure_ascii=False)

def VisualizarJson(caminhoDoArquivo):
    dicionariosModelos = LerArquivo(caminhoDoArquivo)
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


def AtualizarJson(caminhoDoArquivo, id, novosDados):
    # Ler o arquivo JSON
    dicionariosModelos = LerArquivo(caminhoDoArquivo)
    # Verificar se o JSON é uma lista e procurar o item com o 'Id' correspondente
    for modelo in dicionariosModelos:
        if modelo['Id'] == id:
            for chave, valor in novosDados.items():
                if valor:  # Se o valor não for vazio, atualiza
                    modelo[chave] = valor
            break  # Saímos do loop após encontrar o modelo
    # Salva o registro atualizado no arquivo JSON
    with open(caminhoDoArquivo, 'w', encoding="utf8") as arquivo:
        json.dump(dicionariosModelos, arquivo, indent=4, ensure_ascii=False)

    print("Atualizando registro...")
    time.sleep(2)
    print("Registro atualizado com sucesso!")

def DeletarNoJson(caminhoDoArquivo, indice):
    if os.path.exists(caminhoDoArquivo):
        with open(caminhoDoArquivo, 'r', encoding="utf8") as arquivo:
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


# --------------------------------------- !FUNÇÕES DO SISTEMA EMPRESA! ------------------------------------------

def Obter_Prox_Id_Empresa():
    if os.path.exists(arquivoEmpresas):
        with open(arquivoEmpresas, 'r') as arquivo:
            try:
                empresas = json.load(arquivo)
            except json.JSONDecodeError:
                empresas = []
        if empresas:
            ultimo_id = max(empresa.get('Id', 0) for empresa in empresas)
            return ultimo_id + 1
    return 1

def VisualizarJsonEmpresas(caminhoDoArquivo):
    if os.path.exists(caminhoDoArquivo):
        with open(caminhoDoArquivo, 'r', encoding="utf8") as arquivo:
            try:
                dicionariosModelos = json.load(arquivo)
            except json.JSONDecodeError:
                dicionariosModelos = []
        
        if dicionariosModelos:
            # Exibir IDs disponíveis
            print("IDs disponíveis:")
            for dicionario in dicionariosModelos:
                if 'Id' in dicionario:
                    print(f"ID: {dicionario['Id']} | Empresa: {dicionario['Nome']}")

            # Solicitar ao usuário o ID da empresa
            id_escolhido = input("Digite o ID da empresa que deseja ver os detalhes: ")

            # Encontrar e exibir os detalhes do registro correspondente ao ID escolhido
            for dicionario in dicionariosModelos:
                if 'Id' in dicionario and str(dicionario['Id']) == id_escolhido:
                    print(f"\nDetalhes da empresa com ID {id_escolhido}:")
                    print("*******************************")
                    for chave, valor in dicionario.items():
                        print(f"{chave.capitalize()}: {valor}")
                    print("*******************************")
                    return True
            
            print("ID não encontrado.")
            return False
        else:
            print("Nenhum registro encontrado.")
            return False
    else:
        print("Arquivo não encontrado.")
        return False    

def SistemaEmpresas():
    while True:
        Limpar_Console()
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
                Limpar_Console()
                empresaNome = input("Digite o nome da Empresa: ")
                empresaArea = input("Digite a área de atuação da Empresa: ")
                empresaEmail = input("Digite o e-mail da Empresa: ")
                empresaSite = input("Digite o site da empresa: ")
                empresaTelefone = input("Digite o telefone da Empresa: ")
                empresaEndereco = input("Digite o endereço da Empresa: ")
                
                # Gera o próximo ID automaticamente
                empresa = {
                    "Id": Obter_Prox_Id_Empresa(),
                    "Nome": empresaNome,
                    "Area": empresaArea,
                    "Email": empresaEmail,
                    "Site": empresaSite,
                    "Telefone": empresaTelefone,
                    "Endereco": empresaEndereco
                }
                
                # Salva a empresa no JSON
                CadastrarNoJson(arquivoEmpresas, empresa)
                print("Empresa cadastrada com sucesso!")
            case 2:
                Limpar_Console()
                VisualizarJsonEmpresas(arquivoEmpresas)
            case 3:
                Limpar_Console()
                if VisualizarJson(arquivoEmpresas):
                    id = int(input("Digite o ID da empresa que deseja atualizar: "))
                    if ValidarIndice(arquivoEmpresas, id): 
                        novo_nome = input("Digite o novo nome da Empresa (ou deixe em branco para manter o atual): ")
                        nova_area = input("Digite a nova área de atuação da Empresa (ou deixe em branco para manter o atual): ")
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
                        AtualizarJson(arquivoEmpresas, id, novosDados)
            case 4:
                Limpar_Console()
                VisualizarJson(arquivoEmpresas)
                indice = int(input("Digite o índice da Empresa que deseja excluir: "))
                DeletarNoJson(arquivoEmpresas, indice)
            case 5:
                MenuPrincipal()
                return
            case 0:
                print("Finalizando o programa!")
                return False
            case _:
                Limpar_Console()
                print("Opção inválida! Você voltará para o Menu.")
                print("-" * 10)
                continue

        if not PararOuContinuar():
            break



# --------------------------------------- !SISTEMA DE VAGAS! ------------------------------------------



def Obter_Prox_Id_Vaga():
    if os.path.exists(arquivoVagas):
        with open(arquivoVagas, 'r') as arquivo:
            try:
                vagas = json.load(arquivo)
            except json.JSONDecodeError:
                vagas = []
        if vagas:
            ultimo_id = max(vaga['Id'] for vaga in vagas)
            return ultimo_id + 1
    return 1

def cadastrar_vaga():
    Limpar_Console()
    print("Cadastro de Vaga")
    
    # exibir ID da empresa em construção
    
    vaga = {
        "IdEmpresa": input("Id da Empresa: "),
        "Funcao": input("Função: "),
        "Curso": input("Curso: "),
        "Periodo Minimo": int(input("Período mínimo: ")),
        "Turno": input("Turno (matutino/vespertino/noturno): "),
        "Bolsa": float(input("Bolsa: ")),
        "Auxilio Transporte": input("Auxílio Transporte (sim/não): "),
        "Idade Minima": int(input("Idade mínima: ")),
        "Status": "aberta",
        "Prazo": input("Prazo para candidatura (DD/MM/AAAA): ")
    }

    CadastrarNoJson(arquivoVagas, vaga)
    print("Vaga cadastrada com sucesso.")

def visualizar_vagas():
    Limpar_Console()
    print("Visualização de Vagas")
    VisualizarJson(arquivoVagas)

def atualizar_vaga():
    Limpar_Console()
    visualizar_vagas()
    indice = int(input("Digite o índice da vaga que deseja atualizar: "))
    nova_funcao = input("Digite a nova função (ou deixe em branco para manter a atual): ")
    novo_curso = input("Digite o novo curso relacionado (ou deixe em branco para manter o atual): ")
    novo_periodo_minimo = input("Digite o novo período mínimo (ou deixe em branco para manter o atual): ")
    novo_turno = input("Digite o novo turno (ou deixe em branco para manter o atual): ")
    nova_bolsa = input("Digite o valor da nova bolsa (ou deixe em branco para manter o atual): ")
    novo_auxilio_transporte = input("A vaga oferece auxílio transporte? (Sim/Não ou deixe em branco para manter o atual): ")
    nova_idade_minima = input("Digite a nova idade mínima (ou deixe em branco para manter o atual): ")
    novo_status = input("Digite o novo status da vaga (ou deixe em branco para manter o atual): ")
    novo_prazo = input("Digite o novo prazo para candidatura (ou deixe em branco para manter o atual): ")

    novosDados = {
        "Funcao": nova_funcao,
        "Curso": novo_curso,
        "Periodo Minimo": novo_periodo_minimo,
        "Turno": novo_turno,
        "Bolsa": nova_bolsa,
        "Auxilio Transporte": novo_auxilio_transporte,
        "Idade Minima": nova_idade_minima,
        "Status": novo_status,
        "Prazo": novo_prazo
    }
    AtualizarJson(arquivoVagas, indice, novosDados)

def deletar_vaga():
    Limpar_Console()
    visualizar_vagas()
    id = int(input("Digite o ID da vaga que deseja deletar: "))

    DeletarNoJson(arquivoVagas, id)

def sistema_vagas():
    while True:
        Limpar_Console()
        print("\n" + "=" * 40)
        print(f"{'SISTEMA DE VAGAS':^40}")
        print("=" * 40)
        print("1 - Cadastrar Vaga")
        print("2 - Visualizar Vagas")
        print("3 - Atualizar Vaga")
        print("4 - Excluir Vaga")
        print("5 - Voltar para o Menu Principal")
        print("0 - Encerrar o Programa")
        print("=" * 40)

        opc = int(input("\nSelecione uma opção: "))
        match opc:
            case 1:
                cadastrar_vaga()
            case 2:
                visualizar_vagas()
            case 3:
                atualizar_vaga()
            case 4:
                deletar_vaga()
            case 5:
                MenuPrincipal()
                return
            case 0:
                print("Finalizando o programa!")
                return False
            case _:
                print("Opção inválida! Você voltará para o Menu.")
                continue

        if not PararOuContinuar():
            break


# --------------------------------------- !MENU PRINCIPAL! ------------------------------------------

def MenuPrincipal():
    Limpar_Console()
    print("Vagas de Estágios")
    print("Bem-vindo(a) ao Centro de Vagas!")
    print("Vamos começar?")
    print("1 - Sistema de Estudantes")
    print("2 - Sistema de Empresas")
    print("3 - Sistema de Vagas")
    print("0 - Encerrar o programa")
    
    opcMenuPrincipal = int(input("Insira a opção desejada: "))
    
    match opcMenuPrincipal:
        case 1:
            print("Sistema de Estudantes...")  # print temporário
        case 2:
            SistemaEmpresas()
        case 3:
            sistema_vagas()
        case 0:
            print("Encerrando o programa... Até mais!")
        case _:
            print("Opção inválida. Sistema encerrado.")

# --------------------------------------- !MAIN! ------------------------------------------

if __name__ == "__main__":
    MenuPrincipal()
