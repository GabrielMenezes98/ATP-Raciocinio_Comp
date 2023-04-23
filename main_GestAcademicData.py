#NOME: Gabriel Soares de Menezes
#RA: 112023100378
#Curso: Análise e desenvolvimento de sistemas
#GitHub: https://github.com/GabrielMenezes98/ATP-Raciocinio_Comp

import json

##########  CARREGA DADOS DO ARQUIVO EM ARMAZENAMENTO  ##########
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
    
    elif op == 4:
        try:
            with open('dados_turmas.json','r', encoding='utf8') as f:
                dados_turmas = json.load(f)
                return dados_turmas
        except FileNotFoundError:    
            dados_turmas = []
        return dados_turmas
    
    elif op == 5:
        try:
            with open('dados_matriculas.json','r', encoding='utf8') as f:
                dados_matriculas = json.load(f)
                return dados_matriculas
        except FileNotFoundError:    
            dados_matriculas = []
        return dados_matriculas


##########  GRAVA DADOS NO ARQUIVO EM ARMAZENAMENTO  ##########
def registra_dados(dados_estudantes, dados_professores, dados_disciplinas,dados_turmas,dados_matriculas):
    if op == 1:
        with open('dados_estudantes.json','w',encoding='utf8') as f:
            json.dump(dados_estudantes,f, ensure_ascii=False)
    
    if op == 2:
        with open('dados_professores.json','w',encoding='utf8') as f:
            json.dump(dados_professores,f, ensure_ascii=False)

    if op == 3:
        with open('dados_disciplinas.json','w',encoding='utf8') as f:
            json.dump(dados_disciplinas,f, ensure_ascii=False)

    if op == 4:
        with open('dads_turmas.json','w',encoding='utf8') as f:
            json.dump(dados_turmas,f, ensure_ascii=False)

    if op == 5:
        with open('dads_matriculas.json','w',encoding='utf8') as f:
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
            if valida_cod_professores(codigo, dados_professores):
                continue
            nome = input("Insira o nome do professor: ")
            cpf =input("Insira o CPF: ")
            infoprofessor = {"Código":codigo,"Nome":nome,"CPF":cpf}
            dados_professores.append(infoprofessor)
            if input("Deseja inserir outro professor?(s/n) ") == "n":
                break

    elif op == 5:
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
        

##########  FUNÇÃO PARA LISTAGEM DE ESTUDANTES  ##########
def listar_estudantes(dados_estudantes):
    dados_estudantes = carrega_dados()
    if len(dados_estudantes) == 0:
        print("A lista está vazia")
    
    else:
        print('********** LISTA DE ESTUDANTES **********')
        for estudante in dados_estudantes:
            print(estudante)


##########  FUNÇÃO PARA ATUALIZAR ESTUDANTES  ##########
def atualizar_estudante(dados_estudantes, dados_professores, dados_disciplinas, dados_turmas, dados_matriculas):
    codigo_att = int(input("Qual o código do estudante que deseja alterar?: "))
    novo_nome = input("Insira o nome: ")
    novo_cpf = input("Insira o CPF: ")
    #PERCORRE A LISTA PARA ENCONTRAR O CODIGO INFORMADO
    for estudante in dados_estudantes:
    #SUBSTITUI AS INFORMAÇÕES RESPECTIVAMENTE
        if estudante['Código'] == codigo_att:
            estudante['Nome'] = novo_nome
            estudante['CPF'] = novo_cpf
            registra_dados(dados_estudantes,dados_professores, dados_disciplinas, dados_turmas, dados_matriculas)
    

##########  FUNÇÃO PARA EXCLUIR ESTUDANTES  ##########
def excluir_estudante(dados_estudantes, dados_professores, dados_disciplinas, dados_turmas, dados_matriculas):
    #Percorre a lista de estudantes em busca do código copiado
    codigo_exclusao = int(input("Qual código do estudante que deseja excluir?: "))
    for index, estudante in enumerate(dados_estudantes):
        if estudante['Código'] == codigo_exclusao:
            dados_estudantes.pop(index)
            registra_dados(dados_estudantes, dados_professores, dados_disciplinas, dados_turmas, dados_matriculas)
            print("Estudante","*",estudante['Nome'],"*","foi excluido.")


##########  VALIDA ESTUDANTES  ##########
def valida_cod_estudante(codigo, dados_estudantes):
    for estudante in dados_estudantes:
        if codigo == estudante['Código']:
            print("Este código já existe, tente novamente")
            return True



##########  FUNÇÃO PARA LISTAGEM DE PROFESSORES  ##########
def listar_professores(dados_professores):
    dados_professores = carrega_dados()
    if len(dados_professores) == 0:
        print("A lista está vazia")

    else:
        print('********** LISTA DE PROFESSORES **********')
        for professor in dados_professores:
            print(professor)


##########  FUNÇÃO PARA ATUALIZAR PROFESSORES ##########
def atualizar_professores(dados_estudantes, dados_professores, dados_disciplinas, dados_turmas, dados_matriculas):
    codigo_att = int(input("Qual o código do professor que deseja alterar?: "))
    novo_nome = input("Insira o nome: ")
    novo_cpf = input("Insira o CPF: ")
    #PERCORRE A LISTA PARA ENCONTRAR O CODIGO INFORMADO
    for professor in dados_professores:
    #SUBSTITUI AS INFORMAÇÕES RESPECTIVAMENTE
        if professor['Código'] == codigo_att:
            professor['Nome'] = novo_nome
            professor['CPF'] = novo_cpf
            registra_dados(dados_estudantes, dados_professores, dados_disciplinas, dados_turmas, dados_matriculas)


##########  FUNÇÃO PARA EXCLUIR PROFESSORES  ##########
def excluir_professores(dados_estudantes, dados_professores, dados_disciplinas, dados_turmas, dados_matriculas):
    #Percorre a lista em busca do código copiado
    codigo_exclusao = int(input("Qual código do estudante que deseja excluir?: "))
    for index, professor in enumerate(dados_professores):
        if professor['Código'] == codigo_exclusao:
            dados_professores.pop(index)
            registra_dados(dados_estudantes, dados_professores, dados_disciplinas, dados_turmas, dados_matriculas)
            print("Professor","*",professor['Nome'],"*","foi excluido.")


##########  VALIDA PROFESSORES  ##########
def valida_cod_professores(codigo, dados_professores):
    for professor in dados_professores:
        if codigo == professor['Código']:
            print("Este código já existe, tente novamente")
            return True
       

##########  FUNÇÃO PARA LISTAGEM DE DISCIPLINAS  ##########
def listar_disciplinas(dados_disciplinas):
    dados_disciplinas = carrega_dados()
    if len(dados_disciplinas) == 0:
        print("A lista está vazia")

    else:
        print('********** LISTA DE PROFESSORES **********')
        for disciplina in dados_disciplinas:
            print(disciplina)


##########  ATUALIZA DISCIPLINAS  ##########
def atualizar_disciplinas(dados_estudantes, dados_professores, dados_disciplinas, dados_turmas, dados_matriculas):
    codigo_att = int(input("Qual o código da disciplina que deseja alterar?: "))
    novo_nome = input("Insira o nome: ")
    #PERCORRE A LISTA PARA ENCONTRAR O CODIGO INFORMADO
    for disciplina in dados_disciplinas:
    #SUBSTITUI AS INFORMAÇÕES RESPECTIVAMENTE
        if disciplina['Código'] == codigo_att:
            disciplina['Nome'] = novo_nome
            registra_dados(dados_estudantes, dados_professores, dados_disciplinas, dados_turmas, dados_matriculas)


##########  FUNÇÃO PARA EXCLUIR DISCIPLINAS  ##########
def excluir_disciplinas(dados_estudantes, dados_professores, dados_disciplinas, dados_turmas, dados_matriculas):
    #Percorre a lista em busca do código copiado
    codigo_exclusao = int(input("Qual código da disciplina que deseja excluir?: "))
    for index, disciplina in enumerate(dados_disciplinas):
        if disciplina['Código'] == codigo_exclusao:
            dados_disciplinas.pop(index)
            registra_dados(dados_estudantes, dados_professores, dados_disciplinas, dados_turmas, dados_matriculas)
            print("Disciplina","*",disciplina['Nome'],"*","foi excluida.")


##########  VALIDA DISCIPLINAS  ##########
def valida_cod_disciplinas(codigo, dados_disciplinas):
    for disciplina in dados_disciplinas:
        if codigo == disciplina['Código']:
            print("Este código já existe, tente novamente")
            return True
        

##########  AVISO DE DESENVOLVIMENTO  ##########
def em_desenvolvimento():
     print("Em desenvolvimento")


##########  MENU DE ESTUDANTES  ##########
def menu_estudantes():
    while True:
        opcoes_menu_operacoes()
        retorno_menu = int(input())
        dados_estudantes = carrega_dados()
        dados_professores = carrega_dados()
        dados_disciplinas = carrega_dados()
        dados_turmas = carrega_dados()
        dados_matriculas = carrega_dados()
        if retorno_menu == 1:
            inserir(op, dados_estudantes, dados_professores, dados_disciplinas, dados_turmas, dados_matriculas)
            registra_dados(dados_estudantes, dados_professores, dados_disciplinas, dados_turmas, dados_matriculas)
            titulo_menu_estudantes()    
        
        elif retorno_menu == 2:
            listar_estudantes(dados_estudantes)
            titulo_menu_estudantes()
                
        elif retorno_menu == 3: 
            titulo_menu_estudantes()
            atualizar_estudante(dados_estudantes, dados_professores, dados_disciplinas, dados_turmas, dados_matriculas)
            
        elif retorno_menu == 4:
            titulo_menu_estudantes()
            excluir_estudante(dados_estudantes, dados_professores, dados_disciplinas, dados_turmas, dados_matriculas)
            
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
        dados_estudantes = carrega_dados()
        dados_professores = carrega_dados()
        dados_disciplinas = carrega_dados()
        dados_turmas = carrega_dados()
        dados_matriculas = carrega_dados()
        if retorno_menu == 1:
            inserir(op, dados_estudantes, dados_professores, dados_disciplinas, dados_turmas, dados_matriculas)
            registra_dados(dados_estudantes, dados_professores, dados_disciplinas, dados_turmas, dados_matriculas)
            titulo_menu_professores()    
        
        elif retorno_menu == 2:
            dados_professores = carrega_dados()
            listar_professores(dados_professores)
            titulo_menu_professores()
                
        elif retorno_menu == 3: 
            titulo_menu_professores()
            atualizar_professores(dados_estudantes, dados_professores, dados_disciplinas, dados_turmas, dados_matriculas)
            
        elif retorno_menu == 4:
            titulo_menu_professores()
            excluir_professores(dados_estudantes, dados_professores, dados_disciplinas, dados_turmas, dados_matriculas)
            
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
            dados_estudantes = carrega_dados()
            dados_professores = carrega_dados()
            dados_disciplinas = carrega_dados()
            dados_turmas = carrega_dados()
            dados_matriculas = carrega_dados()
            if retorno_menu == 1:
                inserir(op, dados_estudantes, dados_professores, dados_disciplinas, dados_turmas, dados_matriculas)
                registra_dados(dados_estudantes,dados_professores, dados_disciplinas, dados_turmas, dados_matriculas)
                titulo_menu_disciplinas()    
            
            elif retorno_menu == 2:
                dados_disciplinas = carrega_dados()
                listar_disciplinas(dados_disciplinas)
                titulo_menu_disciplinas()
                    
            elif retorno_menu == 3: 
                titulo_menu_disciplinas()
                atualizar_disciplinas(dados_estudantes,dados_professores, dados_disciplinas, dados_turmas, dados_matriculas)
                
            elif retorno_menu == 4:
                titulo_menu_disciplinas()
                excluir_disciplinas(dados_estudantes,dados_professores, dados_disciplinas, dados_turmas, dados_matriculas)
                
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
         print("***** [TURMA] MENU DE OPERAÇÕES *****")

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
            em_desenvolvimento()
            break

        elif op == 5:
            titulo_menu_matriculas()
            em_desenvolvimento()
            break
        
        else:
            print("SAINDO...")
            exit()
                

##########  PROGRAMA PRINCIPAL  ##########
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
         