import json
import os
import time

arquivoEmpresas = "Database/empresas.json"
arquivoEstudantes = "Database/estudantes.json"
arquivoVagas = "Database/vagas.json"



def Limpar_Console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def PararOuContinuar():
    print("")
    while True:
        try:
            print("\033[0;36m-\033[m" * 70)
            print("\033[1;34m1 - Voltar | 2 - Encerrar o programa")
            opc = int(input("▸ Deseja continuar?\033[m "))
            
            if opc == 1:
                return True
            elif opc == 2:
                print("\033[1;33mFinalizando o programa...\033[m")
                time.sleep(1)
                return False
            else:
                print("\033[1;31m❌ Opção inválida. Digite uma opção válida.\033[m")
        
        except ValueError:
            print("\033[1;31m❌ Entrada inválida! Por favor, digite um número inteiro (1 ou 2).\033[m")


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
        print("\033[1;31m❌ ID inválido.\033[m")
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
            print("\033[1;31m❌ Nenhum registro encontrado.\033[m")
            return False


def AtualizarJson(caminhoDoArquivo, id, novosDados):
    dicionariosModelos = LerArquivo(caminhoDoArquivo)
    for modelo in dicionariosModelos:
        if modelo['Id'] == id:
            for chave, valor in novosDados.items():
                if valor:  
                    modelo[chave] = valor
            break  
    with open(caminhoDoArquivo, 'w', encoding="utf8") as arquivo:
        json.dump(dicionariosModelos, arquivo, indent=4, ensure_ascii=False)

    print("Atualizando registro...")
    time.sleep(2)
    print("\033[1;32m✅ Registro atualizado com sucesso!\033[m")

def DeletarNoJson(caminhoDoArquivo, id):
    if os.path.exists(caminhoDoArquivo):
        with open(caminhoDoArquivo, 'r', encoding="utf8") as arquivo:
            try:
                dicionariosModelos = json.load(arquivo)
            except json.JSONDecodeError:
                dicionariosModelos = []

        modeloEncontrado = None
        for modelo in dicionariosModelos:
            if modelo['Id'] == id:
                modeloEncontrado = modelo
                break
        
        if modeloEncontrado:
            dicionariosModelos.remove(modeloEncontrado)

            with open(caminhoDoArquivo, 'w', encoding="utf8") as arquivo:
                json.dump(dicionariosModelos, arquivo, indent=4, ensure_ascii=False)

            print("Removendo registro...")
            time.sleep(2)
            print("\033[1;32m✅ Registro deletado com sucesso!\033[m")
        else:
            print("\033[1;31m❌ O 'Id' especificado não foi encontrado.\033[m")
    else:
        print("\033[1;31m❌ Arquivo não encontrado.\033[m")




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
            print("\033[0;36m-\033[m" * 80)
            print(f'\033[1;35m{"EMPRESAS CADASTRADAS":^75}\033[m')
            print("\033[0;36m-\033[m" * 80)
            print("")
            for dicionario in dicionariosModelos:
                if 'Id' in dicionario:
                    print("ID: " + str(dicionario['Id']).center(10) + " | EMPRESA: " + str(dicionario['Nome']).center(10))


            id_escolhido = input("\n▸ Digite o ID da empresa que deseja ver os detalhes: ")

            for dicionario in dicionariosModelos:
                if 'Id' in dicionario and str(dicionario['Id']) == id_escolhido:
                    print("")
                    print("\033[0;36m-\033[m" * 70)
                    print(f"\033[1;34mDetalhes da empresa com ID {id_escolhido}\033[m".center(75))
                    print("\033[0;36m-\033[m" * 70)
                    for chave, valor in dicionario.items():
                        print(f"{chave.capitalize()}: {valor}")
                    print("\033[0;36m-\033[m" * 70)
                    return True
            
            print("\033[1;31m❌ ID não encontrado.\033[m")
            return False
        else:
            print("\033[1;31m❌ Nenhum registro encontrado.\033[m")
            return False
    else:
        print("\033[1;31m❌ Arquivo não encontrado.\033[m")
        return False    

def BuscarNoJsonEmpresas(caminhoDoArquivo):
    Limpar_Console()
    dicionariosModelos = LerArquivo(caminhoDoArquivo)
    
    print("")
    print("\033[0;36m-\033[m" * 70)
    print(f'\033[1;35m{"EMPRESAS CADASTRADAS NO SISTEMA":^75}\033[m')
    print("\033[0;36m-\033[m" * 70)
    
    for modelo in dicionariosModelos:
        print("[", modelo["Nome"], "]")
    
    empresaEscolhida = input("\n ▸ Digite o nome da Empresa que deseja visualizar: ")
    
    empresaEncontrada = False  
    
    for dicionario in dicionariosModelos:
        if 'Nome' in dicionario and str(dicionario['Nome']) == empresaEscolhida:
            empresaEncontrada = True
            print(f"\nEmpresa: {empresaEscolhida}:")
            print("*******************************")
            for chave, valor in dicionario.items():
                print(f"{chave.capitalize()}: {valor}")
            print("*******************************")
            break 
    
    if not empresaEncontrada:
        print("\033[1;31m❌ Empresa não foi encontrada. Verifique se digitou o nome corretamente.\033[m")
        return False
    
    return True

    

def SistemaEmpresas():
    while True:
        Limpar_Console()
        print("\033[0;36m=\033[m" * 50)
        print(f"\033[1;35m{'✩░▒▓▆▅▃▂▁MÓDULO DE CADASTRO DE EMPRESAS▁▂▃▅▆▓▒░✩':^50}\033[m")
        print("\033[0;36m=\033[m" * 50)
        print("1 - Cadastrar Empresa")
        print("2 - Visualizar Empresas")
        print("3 - Atualizar Empresa")
        print("4 - Excluir Empresa")
        print("5 - Buscar Empresa")
        print("6 - Voltar para o Menu Principal")
        print("0 - Encerrar o Programa")
        print("\033[0;36m=\033[m" * 50)

        opc = int(input("\n\033[0;34m➤  Selecione uma opção:\033[m "))
        match(opc):
            case 1:
                Limpar_Console()
                print("\033[0;36m-\033[m" * 70)
                print(f'\033[1;35m{"CADASTRAR NOVA EMPRESA":^60}\033[m')
                print("\033[0;36m-\033[m" * 70)
                print("")
                empresaNome = input("▸ Digite o nome da Empresa: ")
                empresaArea = input("▸ Digite a área de atuação da Empresa: ")
                empresaEmail = input("▸ Digite o e-mail da Empresa: ")
                empresaSite = input("▸ Digite o site da empresa: ")
                empresaTelefone = input("▸ Digite o telefone da Empresa: ")
                empresaEndereco = input("▸ Digite o endereço da Empresa: ")
                
                empresa = {
                    "Id": Obter_Prox_Id_Empresa(),
                    "Nome": empresaNome,
                    "Area": empresaArea,
                    "Email": empresaEmail,
                    "Site": empresaSite,
                    "Telefone": empresaTelefone,
                    "Endereco": empresaEndereco
                }
                
                CadastrarNoJson(arquivoEmpresas, empresa)
                print("\033[1;32m✅ Empresa cadastrada com sucesso!\033[m")
            case 2:
                Limpar_Console()
                VisualizarJsonEmpresas(arquivoEmpresas)
            case 3:
                Limpar_Console()
                print("\033[0;36m-\033[m" * 80)
                print(f'\033[1;35m{"ATUALIZAR EMPRESA":^75}\033[m')
                print("\033[0;36m-\033[m" * 80)
                print("")
                if VisualizarJson(arquivoEmpresas):
                    id = int(input("▸ Digite o ID da empresa que deseja atualizar: "))
                    if ValidarIndice(arquivoEmpresas, id): 
                        novo_nome = input("▸ Digite o novo nome da Empresa (ou deixe em branco para manter o atual): ")
                        nova_area = input("▸ Digite a nova área de atuação da Empresa (ou deixe em branco para manter o atual): ")
                        novo_email = input("▸ Digite o novo e-mail da Empresa (ou deixe em branco para manter o atual): ")
                        novo_site = input("▸ Digite o novo site da Empresa (ou deixe em branco para manter o atual): ")
                        novo_telefone = input("▸ Digite o novo telefone da Empresa (ou deixe em branco para manter o atual): ")
                        novo_endereco = input("▸ Digite o novo endereço da Empresa (ou deixe em branco para manter o atual): ")

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
                indice = int(input("▸ Digite o índice da Empresa que deseja excluir: "))
                DeletarNoJson(arquivoEmpresas, indice)
            case 5:
                BuscarNoJsonEmpresas(arquivoEmpresas)
            case 6:
                print("\n\033[1;36mVoltando para o menu principal...\033[m")
                time.sleep(2)
                MenuPrincipal()
                return
            case 0:
                print("\033[1;33mFinalizando o programa!\033[m")
                return False
            case _:
                Limpar_Console()
                print("\033[1;31m❌ Opção inválida! Você voltará para o Menu.\033[m")
                print("-" * 10)
                continue

        if not PararOuContinuar():
            break






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
    print("\033[0;36m-\033[m" * 70)
    print(f'\033[1;35m{"CADASTRAR NOVA VAGA":^60}\033[m')
    print("\033[0;36m-\033[m" * 70)
    print("")
    
    vaga = {
        "Id": Obter_Prox_Id_Vaga(),
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
    print("\033[1;32m✅ Vaga cadastrada com sucesso!\033[m")

def visualizar_vagas():
    Limpar_Console()
    print("\033[0;36m-\033[m" * 70)
    print(f'\033[1;35m{"VAGAS CADASTRADAS":^60}\033[m')
    print("\033[0;36m-\033[m" * 70)
    print("")
    VisualizarJson(arquivoVagas)

def atualizar_vaga():
    Limpar_Console()
    visualizar_vagas()
    indice = int(input("▸ Digite o índice da vaga que deseja atualizar: "))
    if ValidarIndice(arquivoVagas, indice):
        nova_funcao = input("▸ Digite a nova função (ou deixe em branco para manter a atual): ")
        novo_curso = input("▸ Digite o novo curso relacionado (ou deixe em branco para manter o atual): ")
        novo_periodo_minimo = input("▸ Digite o novo período mínimo (ou deixe em branco para manter o atual): ")
        novo_turno = input("▸ Digite o novo turno (ou deixe em branco para manter o atual): ")
        nova_bolsa = input("▸ Digite o valor da nova bolsa (ou deixe em branco para manter o atual): ")
        novo_auxilio_transporte = input("▸ A vaga oferece auxílio transporte? (Sim/Não ou deixe em branco para manter o atual): ")
        nova_idade_minima = input("▸ Digite a nova idade mínima (ou deixe em branco para manter o atual): ")
        novo_status = input("▸ Digite o novo status da vaga (ou deixe em branco para manter o atual): ")
        novo_prazo = input("▸ Digite o novo prazo para candidatura (ou deixe em branco para manter o atual): ")

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
    print("\033[0;36m-\033[m" * 70)
    print(f'\033[1;35m{"DELETAR VAGA":^60}\033[m')
    print("\033[0;36m-\033[m" * 70)
    print("")
    visualizar_vagas()
    id = int(input("▸ Digite o ID da vaga que deseja deletar: "))

    DeletarNoJson(arquivoVagas, id)

def BuscarNoJsonVagas(caminhoDoArquivo):
    Limpar_Console()
    dicionariosModelos = LerArquivo(caminhoDoArquivo)
    print("\033[0;36m-\033[m" * 70)
    print(f'\033[1;35m{"VAGAS CADASTRADAS NO SISTEMA":^60}\033[m')
    print("\033[0;36m-\033[m" * 70)
    print("")
    
    cursos = set()  
    for modelo in dicionariosModelos:
        cursos.add(modelo["Curso"]) 
    print("Cursos disponíveis:", ", ".join(cursos))
    
    
    cursoEscolhido = input("▸ Digite o nome do curso que deseja visualizar as vagas de estágio: ")

    encontrou_vagas = False  

   
    for dicionario in dicionariosModelos:
        if 'Curso' in dicionario and str(dicionario['Curso']) == cursoEscolhido:
            if not encontrou_vagas:
                print(f"Vagas para o curso de {cursoEscolhido}:")
                print("*******************************")
            encontrou_vagas = True
            print(f"VAGA")
            print("*******************************")
            for chave, valor in dicionario.items():
                print(f"{chave.capitalize()}: {valor}")
            print("*******************************")
    
    if not encontrou_vagas:
        print("\033[1;31m❌ Nenhuma vaga encontrada para o curso:\033[m", cursoEscolhido)
        return False
    
    return True


def sistema_vagas():
    while True:
        Limpar_Console()
        print("\033[0;36m=\033[m" * 40)
        print(f"\033[1;35m{'✩░▒▓▆▅▃▂▁MÓDULO DE VAGAS▁▂▃▅▆▓▒░✩':^40}\033[m")
        print("\033[0;36m=\033[m" * 40)
        print("1 - Cadastrar Vaga")
        print("2 - Visualizar Vagas")
        print("3 - Atualizar Vaga")
        print("4 - Excluir Vaga")
        print("5 - Buscar vaga")
        print("6 - Voltar para o Menu Principal")
        print("0 - Encerrar o Programa")
        print("\033[0;36m=\033[m" * 40)

        opc = int(input("\n\033[0;34m➤  Selecione uma opcao:\033[m "))
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
                BuscarNoJsonVagas(arquivoVagas)
            case 6:
                print("\n\033[1;36mVoltando para o menu principal...\033[m")
                time.sleep(2)
                MenuPrincipal()
                return
            case 0:
                print("\033[1;33mFinalizando o programa...\033[m")
                return False
            case _:
                print("\033[1;31m❌ Opção inválida! Você voltará para o Menu.\033[m")
                continue

        if not PararOuContinuar():
            break



def carregar_estudantes():
    if not os.path.exists(arquivoEstudantes):
        with open(arquivoEstudantes, "w") as f:
            json.dump([], f, indent=4)
    
    with open(arquivoEstudantes, "r") as f:
        return json.load(f)

def exibir_titulo():
    print("\033[0;36m=\033[m" * 45)
    print(f"\033[1;35m{'✩░▒▓▆▅▃▂▁MÓDULO DOS ESTUDANTES▁▂▃▅▆▓▒░✩':^45}\033[m")
    print("\033[0;36m=\033[m" * 45)

def exibir_subtitulo(texto):
    Limpar_Console()
    linha = f'\033[0;36m-\033[m' * 75
    print(linha)
    print(texto)
    print(linha)
    print("")

def cadastrar_estudante(nome, curso, periodo, turno):
    estudantes = carregar_estudantes()

    estudantes.append({"nome": nome, "curso": curso, "periodo": periodo, "turno": turno})

    with open(arquivoEstudantes, "w") as f:
        json.dump(estudantes, f, indent=4, ensure_ascii=False)
    print("\n \033[1;32m✅ ESTUDANTE ADICIONADO COM SUCESSO!\033[m")
    voltar_menu()
  

def atualizar_estudante(nome_antigo, novo_nome, novo_curso, novo_periodo, novo_turno):
    estudantes = carregar_estudantes()

    for estudante in estudantes: 
        if estudante["nome"] == nome_antigo:
            estudante["nome"] = novo_nome
            estudante["curso"] = novo_curso
            estudante["periodo"] = novo_periodo
            estudante["turno"] = novo_turno
            break

    with open(arquivoEstudantes, "w") as f:
        json.dump(estudantes, f, indent=4, ensure_ascii=False)
    print("\n\033[1;32m✅ ESTUDANTE ATUALIZADO COM SUCESSO!\033[m")
    voltar_menu()

def exibir_estudantes(): 
    estudantes = carregar_estudantes()

    if estudantes:
        for estudante in estudantes:
            print("NOME: " + estudante["nome"].center(14) + 
                  " | CURSO: " + estudante["curso"].center(14) + 
                  " | PERIODO: " + str(estudante["periodo"]).center(14) + 
                  " | TURNO: " + estudante["turno"].center(14))
    else:
        print("\n\033[1;31m❌ NENHUM ESTUDANTE CADASTRADO!\033[m")
    voltar_menu()

def excluir_estudante(nome): 
    estudantes = carregar_estudantes()
    encontrado = False

    for estudante in estudantes:
        if estudante["nome"] == nome:
            estudantes.remove(estudante)
            encontrado = True
            print("\n\033[1;32m✅ ESTUDANTE EXCLUÍDO COM SUCESSO!\033[m")

    if not encontrado:
        print("\n\033[1;31m❌ ESTUDANTE NÃO ENCONTRADO.\033[m")

    with open(arquivoEstudantes, "w") as f:
        json.dump(estudantes, f, indent=4, ensure_ascii=False)
    voltar_menu()

def buscar_estudante(nome): 
    estudantes = carregar_estudantes()  
    encontrado = False

    for estudante in estudantes:
        if estudante["nome"] == nome:
            print("\nSegue dados do(a) estudante:")
            print("NOME: " + estudante["nome"].center(14) + 
                  " | CURSO: " + estudante["curso"].center(14) + 
                  " | PERIODO: " + str(estudante["periodo"]).center(14) + 
                  " | TURNO: " + estudante["turno"].center(14))
            encontrado = True
            break  
    if not encontrado:
        print("\n\033[1;31m❌ ESTUDANTE NÃO ENCONTRADO.\033[m")
    voltar_menu()

def exibir_menu_estudantes():
    Limpar_Console()
    exibir_titulo()
    print("1 - Cadastrar novo estudante")
    print("2 - Atualizar estudante")
    print("3 - Exibir estudantes cadastrados")
    print("4 - Excluir estudante")
    print("5 - Buscar estudante")
    print("6 - Encerrar e voltar ao menu principal")
    print("\033[0;36m=\033[m" * 45)
    escolher_opcao()

def escolher_opcao():
    while True:
        try:
            op = int(input("\n\033[0;34m➤  Escolha uma opcao:\033[m "))

            if (op == 1):
                exibir_subtitulo(f'\033[1;35m{"Novo Cadastro":^75}\033[m')
                nome = input("▸ Informe o NOME do estudante: ")
                curso = input("▸ Informe o CURSO do estudante: ")
                periodo = int(input("▸ Informe o PERÍODO em que o estudante está: "))
                turno = input("▸ Informe o TURNO do curso (matutino/vespertino/noturno): ")
                cadastrar_estudante(nome, curso, periodo, turno)
                break

            elif (op == 2):
                exibir_subtitulo(f'\033[1;35m{"Atualizar Estudante":^75}\033[m')
                nome_antigo = input("▸ Informe o ESTUDANTE (nome) a ser atualizado: \n")
                novo_nome = input("▸ Informe o novo NOME: ")
                novo_curso = input("▸ Informe o novo CURSO: ")
                novo_periodo = int(input("▸ Informe o novo PERÍODO: "))
                novo_turno = input("▸ Informe o novo TURNO (matutino/vespertino/noturno): ")
                atualizar_estudante(nome_antigo, novo_nome, novo_curso, novo_periodo, novo_turno)
                break

            elif (op == 3):
                exibir_subtitulo(f'\033[1;35m{"Estudantes Cadastrados":^75}\033[m')
                exibir_estudantes()
                break

            elif (op == 4):
                exibir_subtitulo(f'\033[1;35m{"Excluir Estudante":^75}\033[m')
                nome = input("▸ Informe o nome do estudante que você deseja excluir: ")
                excluir_estudante(nome)
                break

            elif (op == 5):
                exibir_subtitulo(f'\033[1;35m{"Buscar Estudante":^75}\033[m')
                nome = input("▸ Informe o nome do estudante que você deseja buscar: ")
                buscar_estudante(nome)
                break

            elif (op == 6):
                print("\n\033[1;36mVoltando para o menu principal...\033[m")
                time.sleep(2)
                MenuPrincipal()

            else:
                print("\n\033[1;33m⚠️  OPÇÃO INVÁLIDA!\033[m")
                
        except ValueError:
            print("\n\033[1;33m⚠️  OPÇÃO INVÁLIDA!\033[m")
    return True

def voltar_menu():
    input("\n\033[0;34m➤  Digite qualquer tecla para voltar ao menu anterior:\033[m ")
    exibir_menu_estudantes()




def MenuPrincipal():
    Limpar_Console()
    print("\033[34mBem-vindo(a) ao Centro de Vagas de Estágio!")
    print("\033[34mVamos começar?\033[m\n")
    time.sleep(1)
    print("\033[0;36m=\033[m" * 50)
    print(f'\033[1;35m{"✩░▒▓▆▅▃▂▁SISTEMA DE VAGAS DE ESTAGIO▁▂▃▅▆▓▒░✩":^50}\033[m')
    print("\033[0;36m=\033[m" * 50)
    print("1 - Sistema de Estudantes")
    print("2 - Sistema de Empresas")
    print("3 - Sistema de Vagas")
    print("0 - Encerrar o programa")
    print("\033[0;36m=\033[m" * 50)
    opcMenuPrincipal = int(input("\033[34m\n➤  Insira a opção desejada:\033[m "))
    
    match opcMenuPrincipal:
        case 1:
            exibir_menu_estudantes()
        case 2:
            SistemaEmpresas()
        case 3:
            sistema_vagas()
        case 0:
            print("\033[1;36mEncerrando o programa...")
            time.sleep(1)
            print("Até mais!\033[m")
        case _:
            print("\033[1;31m❌  Opção inválida. Sistema encerrado.\033[m")



if __name__ == "__main__":
    MenuPrincipal()
