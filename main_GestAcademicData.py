#NOME: Gabriel Soares de Menezes
#RA: 112023100378
#Curso: Análise e desenvolvimento de sistemas
#GitHub: https://github.com/GabrielMenezes98/ATP-Raciocinio_Comp

import json

##########  CARREGA DADOS DO ARQUIVO EM ARMAZENAMENTO  ##########
def carrega_dados_estudantes():   
    ########## CARREGA DADOS DOS ESTUDANTES ######### 
        try:
            with open('dados_estudantes.json','r',encoding='utf8') as f:
                dados_estudantes = json.load(f)
                return dados_estudantes
        except FileNotFoundError:
            dados_estudantes = []
        return dados_estudantes
    
    
########## CARREGA DADOS DOS PROFESSORES ##########
def carrega_dados_professores():  
        try:
            with open('dados_professores.json','r',encoding='utf8') as f:
                dados_professores = json.load(f)
                return dados_professores
        except FileNotFoundError:    
            dados_professores = []
        return dados_professores


########## CARREGA DADOS DAS DISCIPLINAS ##########
def carrega_dados_disciplinas(): 
        try:
            with open('dados_disciplinas.json','r', encoding='utf8') as f:
                dados_disciplinas = json.load(f)
                return dados_disciplinas
        except FileNotFoundError:    
            dados_disciplinas = []
        return dados_disciplinas


########## CARREGA DADOS DAS TURMAS ##########
def carrega_dados_turmas():
        try:
            with open('dados_turmas.json','r', encoding='utf8') as f:
                dados_turmas = json.load(f)
                return dados_turmas
        except FileNotFoundError:    
            dados_turmas = []
        return dados_turmas


########## CARREGA DADOS DAS MATRÍCULAS ##########
def carrega_dados_matriculas():
        try:
            with open('dados_matriculas.json','r', encoding='utf8') as f:
                dados_matriculas = json.load(f)
                return dados_matriculas
        except FileNotFoundError:    
            dados_matriculas = []
        return dados_matriculas



##########  GRAVA DADOS NO ARQUIVO EM ARMAZENAMENTO  ##########
def registra_dados_estudantes(dados_estudantes):
        with open('dados_estudantes.json','w',encoding='utf8') as f:
            json.dump(dados_estudantes,f, ensure_ascii=False)
    
def registra_dados_professores(dados_professores):
        with open('dados_professores.json','w',encoding='utf8') as f:
            json.dump(dados_professores,f, ensure_ascii=False)

def registra_dados_disciplinas(dados_disciplinas):
        with open('dados_disciplinas.json','w',encoding='utf8') as f:
            json.dump(dados_disciplinas,f, ensure_ascii=False)

def registra_dados_turmas(dados_turmas):
        with open('dados_turmas.json','w',encoding='utf8') as f:
            json.dump(dados_turmas,f, ensure_ascii=False)

def registra_dados_matriculas(dados_matriculas):
        with open('dados_matriculas.json','w',encoding='utf8') as f:
            json.dump(dados_matriculas,f, ensure_ascii=False)


##########  INSERE DADOS NO ARQUIVO  ##########
def inserir(op,dados_estudantes,dados_professores, dados_disciplinas, dados_turmas, dados_matriculas):
    if op == 1:
        while True:
            codigo = int(input("Insira o código do estudante: "))
            if valida_cod_estudante(codigo, dados_estudantes) == True:
                continue
            nome = input("Insira o nome do estudante: ") 
            cpf = input("Insira o CPF: ")
            infoestudante = {"Código":codigo,"Nome":nome,"CPF":cpf}
            dados_estudantes.append(infoestudante)
            if input("Deseja inserir outro estudante?(s/n): ") == "n":
                break

    elif op == 2:
        while True:
            codigo = int(input("Insira o código do professor: "))
            if valida_cod_professores(codigo, dados_professores):
                continue
            nome = input("Insira o nome do professor: ")
            cpf =input("Insira o CPF: ")
            infoprofessor = {"Código":codigo,"Nome":nome,"CPF":cpf}
            dados_professores.append(infoprofessor)
            if input("Deseja inserir outro professor?(s/n) ") == "n":
                break
    
    elif op == 3:
        while True:
            codigo = int(input("Insira o código da disciplina: "))
            if valida_cod_disciplinas(codigo, dados_disciplinas):
                continue
            nome = input("Insira o nome da disciplina: ")
            infodisciplina = {"Código":codigo,"Nome":nome}
            dados_disciplinas.append(infodisciplina)
            if input("Deseja inserir outra disciplina?(s/n) ") == "n":
                break

    elif op == 4:
        while True:
            codigo = int(input("Insira o código da turma: "))
            insere_professores_em_turmas(dados_turmas, dados_professores)
            if input("Deseja inserir outra turma?(s/n) ") == "n":
                break

    elif op == 5:
        while True:
            cod_codigo = int(input("Insira o código da turma: "))
            #valid codigo turma
            cod_estudante = int(input("Insira o código do estudante: "))
            valida_cod_estudante()
            if input("Deseja inserir outra matrícula(s/n) ") == "n":
                break
        

##########  FUNÇÃO PARA LISTAGEM DE ESTUDANTES  ##########
def listar_estudantes(dados_estudantes):
    if len(dados_estudantes) == 0:
        print("A lista está vazia")
    
    else:
        print('********** LISTA DE ESTUDANTES **********')
        for estudante in dados_estudantes:
            print(estudante)


##########  FUNÇÃO PARA ATUALIZAR ESTUDANTES  ##########
def atualizar_estudante(dados_estudantes):
    codigo_att = int(input("Qual o código do estudante que deseja alterar?: "))
    novo_nome = input("Insira o nome: ")
    novo_cpf = input("Insira o CPF: ")
    #PERCORRE A LISTA PARA ENCONTRAR O CODIGO INFORMADO
    for estudante in dados_estudantes:
    #SUBSTITUI AS INFORMAÇÕES RESPECTIVAMENTE
        if estudante['Código'] == codigo_att:
            estudante['Nome'] = novo_nome
            estudante['CPF'] = novo_cpf
            registra_dados_estudantes(dados_estudantes)
    

##########  FUNÇÃO PARA EXCLUIR ESTUDANTES  ##########
def excluir_estudante(dados_estudantes):
    #Percorre a lista de estudantes em busca do código copiado
    codigo_exclusao = int(input("Qual código do estudante que deseja excluir?: "))
    for index, estudante in enumerate(dados_estudantes):
        if estudante['Código'] == codigo_exclusao:
            dados_estudantes.pop(index)
            registra_dados_estudantes(dados_estudantes)
            print("Estudante","*",estudante['Nome'],"*","foi excluido.")


##########  VALIDA ESTUDANTES  ##########
def valida_cod_estudante(codigo, dados_estudantes):
    for estudante in dados_estudantes:
        if codigo == estudante['Código']:
            print("Este código já existe, tente novamente")
            return True



##########  FUNÇÃO PARA LISTAGEM DE PROFESSORES  ##########
def listar_professores(dados_professores):
    if len(dados_professores) == 0:
        print("A lista está vazia")

    else:
        print('********** LISTA DE PROFESSORES **********')
        for professor in dados_professores:
            print(professor)


##########  FUNÇÃO PARA ATUALIZAR PROFESSORES ##########
def atualizar_professores(dados_professores):
    codigo_att = int(input("Qual o código do professor que deseja alterar?: "))
    novo_nome = input("Insira o nome: ")
    novo_cpf = input("Insira o CPF: ")
    #PERCORRE A LISTA PARA ENCONTRAR O CODIGO INFORMADO
    for professor in dados_professores:
    #SUBSTITUI AS INFORMAÇÕES RESPECTIVAMENTE
        if professor['Código'] == codigo_att:
            professor['Nome'] = novo_nome
            professor['CPF'] = novo_cpf
            registra_dados_professores(dados_professores)


##########  FUNÇÃO PARA EXCLUIR PROFESSORES  ##########
def excluir_professores(dados_professores):
    #Percorre a lista em busca do código copiado
    codigo_exclusao = int(input("Qual código do estudante que deseja excluir?: "))
    for index, professor in enumerate(dados_professores):
        if professor['Código'] == codigo_exclusao:
            dados_professores.pop(index)
            registra_dados_professores(dados_professores)
            print("Professor","*",professor['Nome'],"*","foi excluido.")


##########  VALIDA PROFESSORES  ##########
def valida_cod_professores(codigo, dados_professores):
    for professor in dados_professores:
        if codigo == professor['Código']:
            print("Este código já existe, tente novamente")
            return True
       

##########  FUNÇÃO PARA LISTAGEM DE DISCIPLINAS  ##########
def listar_disciplinas(dados_disciplinas):
    dados_disciplinas = carrega_dados_disciplinas()
    if len(dados_disciplinas) == 0:
        print("A lista está vazia")

    else:
        print('********** LISTA DE DISCIPLINAS **********')
        for disciplina in dados_disciplinas:
            print(disciplina)


##########  ATUALIZA DISCIPLINAS  ##########
def atualizar_disciplinas(dados_disciplinas):
    codigo_att = int(input("Qual o código da disciplina que deseja alterar?: "))
    novo_nome = input("Insira o nome: ")
    #PERCORRE A LISTA PARA ENCONTRAR O CODIGO INFORMADO
    for disciplina in dados_disciplinas:
    #SUBSTITUI AS INFORMAÇÕES RESPECTIVAMENTE
        if disciplina['Código'] == codigo_att:
            disciplina['Nome'] = novo_nome
            registra_dados_disciplinas(dados_disciplinas)


##########  FUNÇÃO PARA EXCLUIR DISCIPLINAS  ##########
def excluir_disciplinas(dados_disciplinas):
    #Percorre a lista em busca do código copiado
    codigo_exclusao = int(input("Qual código da disciplina que deseja excluir?: "))
    for index, disciplina in enumerate(dados_disciplinas):
        if disciplina['Código'] == codigo_exclusao:
            dados_disciplinas.pop(index)
            registra_dados_disciplinas(dados_disciplinas)
            print("Disciplina","*",disciplina['Nome'],"*","foi excluida.")


##########  VALIDA DISCIPLINAS  ##########
def valida_cod_disciplinas(codigo, dados_disciplinas):
    for disciplina in dados_disciplinas:
        if codigo == disciplina['Código']:
            print("Este código já existe, tente novamente")
            return True
        

########## INSERE PROFESSORES EM TURMAS ##########
def insere_professores_em_turmas(dados_turmas, dados_professores):
    cod_professor = int(input("Insira o código do professor: "))
    for professor in dados_professores:
        if professor['Código'] == cod_professor:
            infoturmas = {"Professor":professor}
            dados_turmas.append(infoturmas)
            print(dados_turmas)


##########  AVISO DE DESENVOLVIMENTO  ##########
def em_desenvolvimento():
     print("Em desenvolvimento")


##########  MENU DE ESTUDANTES  ##########
def menu_estudantes():
    while True:
        opcoes_menu_operacoes()
        retorno_menu = int(input())
        dados_estudantes = carrega_dados_estudantes()
        
        if retorno_menu == 1:
            inserir(op,dados_estudantes, dados_professores, dados_disciplinas, dados_turmas, dados_matriculas)
            registra_dados_estudantes(dados_estudantes)
            titulo_menu_estudantes()    
        
        elif retorno_menu == 2:
            listar_estudantes(dados_estudantes)
            titulo_menu_estudantes()
                
        elif retorno_menu == 3: 
            titulo_menu_estudantes()
            atualizar_estudante(dados_estudantes)
            
        elif retorno_menu == 4:
            titulo_menu_estudantes()
            excluir_estudante(dados_estudantes)
            
        elif retorno_menu == 5:  
            break

        else:
            print("Opção inválida, tente novamente")
            continue


########### MENU DE PROFESSORES ########### 
def menu_professores():
    while True:
        opcoes_menu_operacoes()
        retorno_menu = int(input())
        dados_professores = carrega_dados_professores()

        if retorno_menu == 1:
            inserir(op,dados_estudantes, dados_professores, dados_disciplinas, dados_turmas, dados_matriculas)
            registra_dados_professores(dados_professores)
            titulo_menu_professores()    
        
        elif retorno_menu == 2:
            listar_professores(dados_professores)
            titulo_menu_professores()
                
        elif retorno_menu == 3: 
            titulo_menu_professores()
            atualizar_professores(dados_professores)
            
        elif retorno_menu == 4:
            titulo_menu_professores()
            excluir_professores(dados_professores)
            
        elif retorno_menu == 5:  
            break

        else:
            print("Opção inválida, tente novamente!")
            continue

########### MENU DE DISCIPLINAS ###########
def menu_disciplinas():
        while True:
            opcoes_menu_operacoes()
            retorno_menu = int(input())
            dados_disciplinas = carrega_dados_disciplinas()

            if retorno_menu == 1:
                inserir(op,dados_estudantes, dados_professores, dados_disciplinas, dados_turmas, dados_matriculas)
                registra_dados_disciplinas(dados_disciplinas)
                titulo_menu_disciplinas()    
            
            elif retorno_menu == 2:
                listar_disciplinas(dados_disciplinas)
                titulo_menu_disciplinas()
                    
            elif retorno_menu == 3: 
                titulo_menu_disciplinas()
                atualizar_disciplinas(dados_disciplinas)
                
            elif retorno_menu == 4:
                titulo_menu_disciplinas()
                excluir_disciplinas(dados_disciplinas)
                
            elif retorno_menu == 5:  
                break

            else:
                print("Opção inválida, tente novamente!")
                continue


########### MENU TURMAS ###########
def menu_turmas():
    while True:
            opcoes_menu_operacoes()
            retorno_menu = int(input())
            dados_turmas = carrega_dados_turmas()

            if retorno_menu == 1:
                inserir(op,dados_estudantes, dados_professores, dados_disciplinas, dados_turmas, dados_matriculas)
                registra_dados_turmas(dados_turmas)
                titulo_menu_turmas()    
            
            elif retorno_menu == 2:
                listar_turmas()
                titulo_menu_turmas()
                    
            elif retorno_menu == 3: 
                titulo_menu_turmas()
                atualizar_turmas(dados_turmas)
                
            elif retorno_menu == 4:
                titulo_menu_turmas()
                excluir_turmas(dados_turmas)
                
            elif retorno_menu == 5:  
                break

            else:
                print("Opção inválida, tente novamente!")
                continue

##########  OPÇÕES DO MENU DE OPERAÇÕES  ##########
def opcoes_menu_operacoes():
    print("(1) Incluir.")  
    print("(2) Listar.")
    print("(3) Atualizar.")
    print("(4) Excluir.")
    print("(5) Voltar ao menu principal.")

  
##########  TITULOS  ##########
def titulo_menu_estudantes():
        print("***** [ESTUDANTES] MENU DE OPERAÇÕES *****")

def titulo_menu_professores():
        print("***** [PROFESSORES] MENU DE OPERAÇÕES *****")

def titulo_menu_disciplinas():
        print("***** [DISCIPLINAS] MENU DE OPERAÇÕES *****") 

def titulo_menu_turmas():
         print("***** [TURMAS] MENU DE OPERAÇÕES *****")

def titulo_menu_matriculas(): 
        print("***** [MATRÍCULAS] MENU DE OPERAÇÕES *****")


##########  MENU PRINCIPAL  ##########
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
            menu_disciplinas()
            break

        elif op == 4:
            titulo_menu_turmas()
            menu_turmas()
            break

        elif op == 5:
            titulo_menu_matriculas()
            em_desenvolvimento()
            break
        
        else:
            print("SAINDO...")
            exit()
                

##########  PROGRAMA PRINCIPAL  ##########
print("***** INFORMAÇÕES ARMAZENADAS *****")
dados_estudantes = carrega_dados_estudantes()
dados_professores = carrega_dados_professores()
dados_disciplinas = carrega_dados_professores()
dados_turmas = carrega_dados_turmas()
dados_matriculas = carrega_dados_matriculas()
op = int      
while True:
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
        continue
         