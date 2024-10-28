import json
import os
import time

# Arquivos JSON
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


# --------------------------------------- !FUNÇÕES DO SISTEMA EMPRESA! ------------------------------------------

# Função para obter o próximo ID de empresa automaticamente
def obter_proximo_id_empresa():
    if os.path.exists(arquivoEmpresas):
        with open(arquivoEmpresas, 'r') as arquivo:
            try:
                empresas = json.load(arquivo)
            except json.JSONDecodeError:
                empresas = []
        if empresas:
            ultimo_id = max(empresa.get('empresaId', 0) for empresa in empresas)
            return ultimo_id + 1
    return 1

# Função de cadastro de empresas com ID automático
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
                
                # Gera o próximo ID automaticamente
                empresa = {
                    "empresaId": obter_proximo_id_empresa(),
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
                VisualizarJson(arquivoEmpresas)
            case 3:
                limpar_console()
                if VisualizarJson(arquivoEmpresas):  
                    indice = int(input("Digite o índice da empresa que deseja atualizar: "))
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
                    AtualizarJson(arquivoEmpresas, indice, novosDados)
            case 4:
                limpar_console()
                VisualizarJson(arquivoEmpresas)
                indice = int(input("Digite o índice da Empresa que deseja excluir: "))
                DeletarNoJson(arquivoEmpresas, indice)
            case 5:
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


# --------------------------------------- !SISTEMA DE VAGAS! ------------------------------------------


def obter_proximo_id_vaga():
    if os.path.exists(arquivoVagas):
        with open(arquivoVagas, 'r') as arquivo:
            try:
                vagas = json.load(arquivo)
            except json.JSONDecodeError:
                vagas = []
        if vagas:
            ultimo_id = max(vaga['vagaId'] for vaga in vagas)
            return ultimo_id + 1
    return 1

# Validando ID
def empresa_existe(id_empresa):
    if os.path.exists(arquivoEmpresas):
        with open(arquivoEmpresas, 'r') as arquivo:
            try:
                empresas = json.load(arquivo)
            except json.JSONDecodeError:
                empresas = []
        return any(empresa.get('empresaId') == id_empresa for empresa in empresas)
    return False


def cadastrar_vaga():
    limpar_console()
    print("Cadastro de Vaga")
    
    vagaEmpresaId = int(input("Digite o ID da empresa: "))
    if not empresa_existe(vagaEmpresaId):
        print("ID de empresa não encontrado.")
        return
    
    vaga = {
        "vagaId": obter_proximo_id_vaga(),
        "vagaEmpresaId": vagaEmpresaId,
        "vagaFunção": input("Função: "),
        "vagaCurso": input("Curso: "),
        "vagaPeríodoMínimo": int(input("Período mínimo: ")),
        "vagaTurno": input("Turno (matutino/vespertino/noturno): "),
        "vagaBolsa": float(input("Bolsa: ")),
        "vagaAuxílioTransporte": input("Auxílio Transporte (sim/não): "),
        "vagaIdadeMinima": int(input("Idade mínima: ")),
        "vagaStatus": "aberta",
        "vagaPrazo": input("Prazo para candidatura (DD/MM/AAAA): ")
    }

    CadastrarNoJson(arquivoVagas, vaga)
    print("Vaga cadastrada com sucesso.")

def visualizar_vagas():
    limpar_console()
    print("Visualização de Vagas")
    
    curso_filtro = input("Filtrar por curso (ou deixe em branco): ")
    periodo_minimo_filtro = input("Filtrar por período mínimo (ou deixe em branco): ")
    periodo_minimo_filtro = int(periodo_minimo_filtro) if periodo_minimo_filtro else None
    
    if os.path.exists(arquivoVagas):
        with open(arquivoVagas, 'r') as arquivo:
            try:
                vagas = json.load(arquivo)
            except json.JSONDecodeError:
                vagas = []
        
        for vaga in vagas:
            if (curso_filtro and vaga['vagaCurso'] != curso_filtro) or \
               (periodo_minimo_filtro and vaga['vagaPeríodoMínimo'] < periodo_minimo_filtro):
                continue
            
            print("\n*******************************")
            print(f"ID da Vaga: {vaga['vagaId']}")
            print(f"Empresa ID: {vaga['vagaEmpresaId']}")
            print(f"Função: {vaga['vagaFunção']}")
            print(f"Curso: {vaga['vagaCurso']}")
            print(f"Período Mínimo: {vaga['vagaPeríodoMínimo']}")
            print(f"Turno: {vaga['vagaTurno']}")
            print(f"Bolsa: R$ {vaga['vagaBolsa']}")
            print(f"Auxílio Transporte: {vaga['vagaAuxílioTransporte']}")
            print(f"Idade Mínima: {vaga['vagaIdadeMinima']}")
            print(f"Status: {vaga['vagaStatus']}")
            print(f"Prazo para Candidatura: {vaga['vagaPrazo']}")
            print("*******************************")
    else:
        print("Nenhuma vaga encontrada.")

def atualizar_vaga():
    limpar_console()
    visualizar_vagas()
    vagaId = int(input("Digite o ID da vaga que deseja atualizar: "))

    if os.path.exists(arquivoVagas):
        with open(arquivoVagas, 'r') as arquivo:
            try:
                vagas = json.load(arquivo)
            except json.JSONDecodeError:
                vagas = []
        
        vaga = next((v for v in vagas if v['vagaId'] == vagaId), None)
        if vaga:
            vaga['vagaFunção'] = input(f"Função ({vaga['vagaFunção']}): ") or vaga['vagaFunção']
            vaga['vagaCurso'] = input(f"Curso ({vaga['vagaCurso']}): ") or vaga['vagaCurso']
            vaga['vagaPeríodoMínimo'] = int(input(f"Período Mínimo ({vaga['vagaPeríodoMínimo']}): ") or vaga['vagaPeríodoMínimo'])
            vaga['vagaTurno'] = input(f"Turno ({vaga['vagaTurno']}): ") or vaga['vagaTurno']
            vaga['vagaBolsa'] = float(input(f"Bolsa ({vaga['vagaBolsa']}): ") or vaga['vagaBolsa'])
            vaga['vagaAuxílioTransporte'] = input(f"Auxílio Transporte ({vaga['vagaAuxílioTransporte']}): ") or vaga['vagaAuxílioTransporte']
            vaga['vagaIdadeMinima'] = int(input(f"Idade Mínima ({vaga['vagaIdadeMinima']}): ") or vaga['vagaIdadeMinima'])
            vaga['vagaStatus'] = input(f"Status ({vaga['vagaStatus']} - aberta/fechada): ") or vaga['vagaStatus']
            vaga['vagaPrazo'] = input(f"Prazo para Candidatura ({vaga['vagaPrazo']}): ") or vaga['vagaPrazo']

            with open(arquivoVagas, 'w') as arquivo:
                json.dump(vagas, arquivo, indent=4, ensure_ascii=False)

            print("Vaga atualizada com sucesso.")
        else:
            print("Vaga não encontrada.")
    else:
        print("Nenhuma vaga encontrada.")

def deletar_vaga():
    limpar_console()
    visualizar_vagas()
    vagaId = int(input("Digite o ID da vaga que deseja deletar: "))

    if os.path.exists(arquivoVagas):
        with open(arquivoVagas, 'r') as arquivo:
            try:
                vagas = json.load(arquivo)
            except json.JSONDecodeError:
                vagas = []
        
        vagas = [vaga for vaga in vagas if vaga['vagaId'] != vagaId]

        with open(arquivoVagas, 'w') as arquivo:
            json.dump(vagas, arquivo, indent=4, ensure_ascii=False)

        print("Vaga deletada com sucesso.")
    else:
        print("Nenhuma vaga encontrada.")

def sistema_vagas():
    while True:
        limpar_console()
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
                break
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
    limpar_console()
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
    while True:
        MenuPrincipal()
        if input("Deseja sair do sistema? (s/n): ").lower() == 's':
            print("Encerrando o programa... Até mais!")
            break
