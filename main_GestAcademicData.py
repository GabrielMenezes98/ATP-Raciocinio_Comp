#NOME: Gabriel Soares de Menezes
#RA: 112023100378
#Curso: Análise e desenvolvimento de sistemas

#VARIAVEIS GLOBAIS
#lista_estudantes = []
#lista_professores = []
import json

###########  CARREGA DADOS DO ARQUIVO EM ARMAZENAMENTO  ##############
def carrega_dados():
    
    if op == 1:
        try:
            with open('dados_estudantes.json','r',encoding='utf8') as f:
                dados_estudantes = json.load(f)
                return dados_estudantes
        except FileNotFoundError:
            dados_estudantes = []
        return dados_estudantes
    
    elif op == 2:
        try:
            with open('dados_professores.json','r',encoding='utf8') as f:
                dados_professores = json.load(f)
                return dados_professores
        except FileNotFoundError:    
            dados_professores = []
        return dados_professores
    
    elif op == 3:
        try:
            with open('dados_disciplinas.json','r', encoding='utf8') as f:
                dados_disciplinas = json.load(f)
                return dados_disciplinas
        except FileNotFoundError:    
            dados_disciplinas = []
        return dados_disciplinas

################ GRAVA DADOS NO ARQUIVO EM ARMAZENAMENTO ###############
def registra_dados(dados_estudantes, dados_professores):
    if op == 1:
        with open('dados_estudantes.json','w',encoding='utf8') as f:
            json.dump(dados_estudantes,f, ensure_ascii=False)
    
    if op == 2:
        with open('dados_professores.json','w',encoding='utf8') as f:
            json.dump(dados_professores,f, ensure_ascii=False)


#########  INSERE DADOS NO ARQUIVO #########################
def inserir(op, dados_estudantes, dados_professores):
    if op == 1:
        while True:
            codigo = int(input("Insira o código do estudante: "))
            nome = input("Insira o nome do estudante: ") 
            cpf = input("Insira o CPF: ")
            infoestudante = {"Código":codigo,"Nome":nome,"CPF":cpf}
            dados_estudantes.append(infoestudante)
            if input("Deseja inserir outro estudante?(s/n): ") == "n":
                break
    elif op == 2:
        while True:
            codigo = int(input("Insira o código do professor: "))
            nome = input("Insira o nome do professor: ")
            cpf =input("Insira o CPF: ")
            infoprofessor = {"Código":codigo,"Nome":nome,"CPF":cpf}
            dados_professores.append(infoprofessor)
            if input("Deseja inserir outro estudante?(s/n) ") == "n":
                break
        

############  FUNÇÃO PARA LISTAGEM DE ESTUDANTES  #################
def listar_estudantes(dados_estudantes):
    dados_estudantes = carrega_dados()
    if len(dados_estudantes) == 0:
        print("A lista está vazia")
    
    else:
        print('********** LISTA DE ESTUDANTES **********')
        for estudante in dados_estudantes:
            print(estudante)

############ FUNÇÃO PARA LISTAGEM DE PROFESSORES
def listar_professores(dados_professores):
    dados_professores = carrega_dados()
    if len(dados_professores) == 0:
        print("A lista está vazia")

    else:
        print('********** LISTA DE PROFESSORES **********')
        for professor in dados_professores:
            print(professor)

########   FUNÇÃO PARA ATUALIZAR CADASTROS  ###############
def atualizar_estudante(lista_estudantes, codigo_atualizacao, novo_estudante):
    #PERCORRE A LISTA PARA ENCONTRAR O CODIGO INFORMADO
    for i, estudante in enumerate(lista_estudantes):
        if estudante[0] == codigo_atualizacao: 
            #SUBSTITUI O ESTUDANTE ANTERIOR PELO NOVO ESTUDANTE
            lista_estudantes[i] = novo_estudante
            #RETORNA A LISTA ATUALIZADA
            return lista_estudantes
    #CASO O CÓDIGO NÃO SEJA ENCONTRADO, RETORNA A LISTA ORIGINAL
    return lista_estudantes


#####   FUNÇÃO PARA EXCLUIR CADASTROS  ##############
def excluir_estudante(lista_estudantes, indice_exclusao):
    #Percorre a lista de estudantes em busca do código copiado
    for i, estudante in enumerate(lista_estudantes):  
        if estudante[0] == indice_exclusao:
            #remove a TUPLA da LISTA de estudantes
            del lista_estudantes[i]
            #retorna a lista de estudantes atualizada
            return lista_estudantes
    #caso não encontre o indice de exclusão, retorna a lista original
    return lista_estudantes
               

#####       AVISO DE DESENVOLVIMENTO   ##############
def em_desenvolvimento():
     print("Em desenvolvimento")

#######   OPÇÕES DO MENU DE OPERAÇÕES   #############
def opcoes_menu_operacoes():
    print("(1) Incluir.")  
    print("(2) Listar.")
    print("(3) Atualizar.")
    print("(4) Excluir.")
    print("(5) Voltar ao menu principal.")


#########   MENU DE ESTUDANTES #############
def menu_estudantes():
    subop = int
    while subop != 5:
        opcoes_menu_operacoes()
        retorno_menu = int(input())
        dados_estudantes = carrega_dados()
        dados_professores = carrega_dados()
        if retorno_menu == 1:
            inserir(op, dados_estudantes, dados_professores)
            registra_dados(dados_estudantes,dados_professores)
            titulo_menu_estudantes()    
        
        elif retorno_menu == 2:
            dados_estudantes = carrega_dados()
            listar_estudantes(dados_estudantes)
            titulo_menu_estudantes()
                
        elif retorno_menu == 3: 
            titulo_menu_estudantes()
            codigo_atualizacao = input("Qual o código do estudante que deseja atualizar? ")
            nome = input("Insira o nome: ")
            cpf = input("Insira o CPF: ")
            novo_estudante = codigo_atualizacao, nome, cpf
            atualizar_estudante(dados_estudantes, codigo_atualizacao, novo_estudante)
            
        elif retorno_menu == 4:
            titulo_menu_estudantes()
            codigo_exclusao = (input("Qual o código do estudante que deseja excluir? "))
            excluir_estudante(dados_estudantes, codigo_exclusao)
            
        elif retorno_menu == 5:  
            subop = 5

########### MENU DE PROFESSORES ########### 
def menu_professores():
    subop = int
    while subop != 5:
        opcoes_menu_operacoes()
        retorno_menu = int(input())
        dados_estudantes = carrega_dados()
        dados_professores = carrega_dados()
        if retorno_menu == 1:
            inserir(op, dados_estudantes, dados_professores)
            registra_dados(dados_estudantes,dados_professores)
            titulo_menu_estudantes()    
        
        elif retorno_menu == 2:
            dados_professores = carrega_dados()
            listar_professores(dados_professores)
            titulo_menu_estudantes()
                
        elif retorno_menu == 3: 
            titulo_menu_estudantes()
            codigo_atualizacao = input("Qual o código do estudante que deseja atualizar? ")
            nome = input("Insira o nome: ")
            cpf = input("Insira o CPF: ")
            novo_professor = codigo_atualizacao, nome, cpf
            atualizar_estudante(dados_professores, codigo_atualizacao, novo_professor)
            
        elif retorno_menu == 4:
            titulo_menu_estudantes()
            codigo_exclusao = (input("Qual o código do estudante que deseja excluir? "))
            excluir_estudante(dados_professores, codigo_exclusao)
            
        elif retorno_menu == 5:  
            subop = 5
        
###########  TITULOS   ################
def titulo_menu_estudantes():
        print("***** [ESTUDANTES] MENU DE OPERAÇÕES *****")

def titulo_menu_professores():
        print("***** [PROFESSORES] MENU DE OPERAÇÕES *****")

def titulo_menu_disciplinas():
        print("***** [DISCIPLINAS] MENU DE OPERAÇÕES *****") 

def titulo_menu_turmas():
         print("***** [TURMA] MENU DE OPERAÇÕES *****")

def titulo_menu_matriculas(): 
        print("***** [MATRÍCULAS] MENU DE OPERAÇÕES *****")


#MENU PRINCIPAL
def menu_principal(op):
    
    while True:
        
        if op == 1:
            titulo_menu_estudantes()
            menu_estudantes()
            break
        elif op == 2: 
            titulo_menu_professores()
            menu_professores()
            break
        elif op == 3:
            titulo_menu_disciplinas()
            em_desenvolvimento()
            break
        elif op == 4:
            titulo_menu_turmas()
            em_desenvolvimento()
            break
        elif op == 5:
            titulo_menu_matriculas()
            em_desenvolvimento()
            break
        else:
            print("SAINDO...")
            break
                

#PROGRAMÃO
op = int      
while op != 6:
    print("----- MENU PRINCIPAL -----")
    print("1 - Gerenciar estudantes. ")
    print("2 - Gerenciar professores.")
    print("3 - Gerenciar disciplinas.")
    print("4 - Gerenciar turmas.")
    print("5 - Gerenciar matrículas.")
    print("6 - Sair")
    op = int(input())
    if 1 <= op <= 6:
        menu_principal(op)
    else:
        print("Opção inválida") 