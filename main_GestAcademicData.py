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
            json.dump(dados_estudantes,f,indent=4, ensure_ascii=False)
    
def registra_dados_professores(dados_professores):
        with open('dados_professores.json','w',encoding='utf8') as f:
            json.dump(dados_professores,f,indent=4, ensure_ascii=False)

def registra_dados_disciplinas(dados_disciplinas):
        with open('dados_disciplinas.json','w',encoding='utf8') as f:
            json.dump(dados_disciplinas,f,indent=4, ensure_ascii=False)

def registra_dados_turmas(dados_turmas):
        with open('dados_turmas.json','w',encoding='utf8') as f:
            json.dump(dados_turmas,f,indent=4, ensure_ascii=False)

def registra_dados_matriculas(dados_matriculas):
        with open('dados_matriculas.json','w',encoding='utf8') as f:
            json.dump(dados_matriculas,f,indent=4, ensure_ascii=False)


##########  INSERE DADOS NO ARQUIVO  ##########
def inserir(op,dados_estudantes,dados_professores, dados_disciplinas, dados_turmas, dados_matriculas):
    if op == 1:
        while True:
            try:
                codigo = int(input("Insira o código do estudante: "))
            except:
                print("Código inválido, insira um valor númerico.")
                continue
            if valida_cod_estudante(codigo, dados_estudantes) == True:
                print("Este código já existe, tente novamente")
                continue
            nome = input("Insira o nome do estudante: ") 
            cpf = input("Insira o CPF: ")
            infoestudante = {"Código":codigo,"Nome":nome,"CPF":cpf}
            dados_estudantes.append(infoestudante)
            if input("Deseja inserir outro estudante?(s/n): ") == "n":
                break

    elif op == 2:
        while True:
            try:
                codigo = int(input("Insira o código do professor: "))
            except:
                print("Código inválido, insira um valor númerico.")
                continue
            if valida_cod_professores(codigo, dados_professores) == True:
                print("Este código já existe, tente novamente")
                continue
            nome = input("Insira o nome do professor: ")
            cpf =input("Insira o CPF: ")
            infoprofessor = {"Código":codigo,"Nome":nome,"CPF":cpf}
            dados_professores.append(infoprofessor)
            if input("Deseja inserir outro professor?(s/n) ") == "n":
                break
    
    elif op == 3:
        while True:
            try:
                codigo = int(input("Insira o código da disciplina: "))
            
            except:
                print("Código inválido, insira um valor númerico.")
                continue
            if valida_cod_disciplinas(codigo, dados_disciplinas):
                print("Este código já existe, tente novamente")
                continue
            nome = input("Insira o nome da disciplina: ")
            infodisciplina = {"Código":codigo,"Nome":nome}
            dados_disciplinas.append(infodisciplina)
            if input("Deseja inserir outra disciplina?(s/n) ") == "n":
                break

    elif op == 4:
        while True:
            try:
                n_turma = int(input("Insira o código da turma: "))
            
            except:
                print("Código inválido, insira um valor númerico.")
                continue
            if valida_cod_turmas(n_turma, dados_turmas):
                print("Este código já existe, tente novamente")
                continue
            insere_professores_em_turmas(n_turma, dados_turmas, dados_professores, dados_disciplinas)
            
            if input("Deseja inserir outra turma?(s/n) ") == "n":
                break

    elif op == 5:
        while True:
            try:
                indice_matricula = int(input("Insira o número da matrícula: "))
            
            except:
                print("Código inválido, insira um valor númerico.")
                continue
            if valida_cod_matriculas(indice_matricula, dados_matriculas) == True:
                print("Matrícula já existente, insira outro número.")
                continue
            insere_estudantes_e_turmas(dados_matriculas, dados_estudantes, dados_turmas, indice_matricula)
            registra_dados_matriculas(dados_matriculas)
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
    while True:
        try:
            codigo_att = int(input("Qual o código do estudante que deseja alterar?: "))
        
        except:
            print("Código inválido, insira um vaor numérico")
            continue

        if valida_cod_estudante(codigo_att, dados_estudantes) == True:
            novo_nome = input("Insira o nome: ")
            novo_cpf = input("Insira o CPF: ")
            #PERCORRE A LISTA PARA ENCONTRAR O CODIGO INFORMADO
            for estudante in dados_estudantes:
            #SUBSTITUI AS INFORMAÇÕES RESPECTIVAMENTE
                if estudante['Código'] == codigo_att:
                    estudante['Nome'] = novo_nome
                    estudante['CPF'] = novo_cpf
                    registra_dados_estudantes(dados_estudantes)
                    print("Estudante","*",estudante['Nome'],"*","foi atualizado.")
      
        else:
            print("Este estudante não existe, tente novamente.")
        break

##########  FUNÇÃO PARA EXCLUIR ESTUDANTES  ##########
def excluir_estudante(dados_estudantes):
    while True:
        try:
            codigo_exclusao = int(input("Qual código do estudante que deseja excluir?: "))
        except:
            print("Este código não existe, tente novamente.")
        if valida_cod_estudante(codigo_exclusao, dados_estudantes) == True:  
            for index, estudante in enumerate(dados_estudantes):
                if estudante['Código'] == codigo_exclusao:
                    dados_estudantes.pop(index)
                    registra_dados_estudantes(dados_estudantes)
                    print("Estudante","*",estudante['Nome'],"*","foi excluido.")
        else:
            print("Esse estudante não existe, tente novamente.")
            continue
        break
        


##########  VALIDA ESTUDANTES  ##########
def valida_cod_estudante(codigo, dados_estudantes):
    for estudante in dados_estudantes:
        if codigo == estudante['Código']:
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
    while True:
        try:
            codigo_att = int(input("Qual o código do professor que deseja alterar?: "))
        except:
            print("Código inválido, insira um valor numérico.")
            continue
        if valida_cod_professores(codigo_att, dados_professores) == True:
            novo_nome = input("Insira o nome: ")
            novo_cpf = input("Insira o CPF: ")
            #PERCORRE A LISTA PARA ENCONTRAR O CODIGO INFORMADO
            for professor in dados_professores:
            #SUBSTITUI AS INFORMAÇÕES RESPECTIVAMENTE
                if professor['Código'] == codigo_att:
                    professor['Nome'] = novo_nome
                    professor['CPF'] = novo_cpf
                    registra_dados_professores(dados_professores)
                    print("Professor","*",professor['Nome'],"*","foi atualizado.")
        else:
            print("Esse professor não existe, tente novamente.")
            continue
        break


##########  FUNÇÃO PARA EXCLUIR PROFESSORES  ##########
def excluir_professores(dados_professores):
    while True:
        try:
            codigo_exclusao = int(input("Qual código do estudante que deseja excluir?: "))
        except:
            print("Código inválido, insira um valor numérico.")
            continue
        if valida_cod_professores(codigo_exclusao, dados_professores) == True:
            for index, professor in enumerate(dados_professores):
                if professor['Código'] == codigo_exclusao:
                    dados_professores.pop(index)
                    registra_dados_professores(dados_professores)
                    print("Professor","*",professor['Nome'],"*","foi excluido.")
        else:
            print("Esse professor não existe, tente novamente.")
            continue
        break

##########  VALIDA PROFESSORES  ##########
def valida_cod_professores(codigo, dados_professores):
    for professor in dados_professores:
        if codigo == professor['Código']:
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
    while True:
        try:
            codigo_att = int(input("Qual o código da disciplina que deseja alterar?: "))
        except:
            print("Código inválido, insira um valor numérico.")
        if valida_cod_disciplinas(codigo_att,dados_disciplinas) == True:
            novo_nome = input("Insira o nome: ")
            #PERCORRE A LISTA PARA ENCONTRAR O CODIGO INFORMADO
            for disciplina in dados_disciplinas:
            #SUBSTITUI AS INFORMAÇÕES RESPECTIVAMENTE
                if disciplina['Código'] == codigo_att:
                    disciplina['Nome'] = novo_nome
                    registra_dados_disciplinas(dados_disciplinas)
                    print(f"A disciplina {disciplina['Nome']} foi atualizada.")
        else:
            print("Essa disciplina não existe, tente novamente.")
            continue
        break

##########  FUNÇÃO PARA EXCLUIR DISCIPLINAS  ##########
def excluir_disciplinas(dados_disciplinas):
    while True:
        try:
            codigo_exclusao = int(input("Qual o código da disciplina que deseja excluir: "))
        except:
            print("Código inválido, insira um valor numérico.")
        if valida_cod_disciplinas(codigo_exclusao,dados_disciplinas) == True:
            for index, disciplina in enumerate(dados_disciplinas):
                if disciplina['Código'] == codigo_exclusao:
                    dados_disciplinas.pop(index)
                    registra_dados_disciplinas(dados_disciplinas)
                    print("Disciplina","*",disciplina['Nome'],"*","foi excluida.")
        else:
            print("Essa disciplina não existe, tente novamente.")
            continue
        break


##########  VALIDA DISCIPLINAS  ##########
def valida_cod_disciplinas(codigo, dados_disciplinas):
    for disciplina in dados_disciplinas:
        if codigo == disciplina['Código']:
            return True
        

########## INSERIR TURMAS ##########
def insere_professores_em_turmas(n_turma, dados_turmas, dados_professores, dados_disciplinas):
    while True:
        try:
            cod_professor = int(input("Insira o código do professor: "))
        except:
            print("Código inválido, tente novamente.")
            continue
        if valida_cod_professores(cod_professor, dados_professores) == True:
            for professor in dados_professores:
                if professor['Código'] == cod_professor:
                    infoprof = professor
            break
        else:
            print("Este professor não existe, tente novamente.")
            continue
    
    while True:
        try:
            cod_disciplina = int(input("Insira o código da disciplina: "))
        except:
            print("Código inválido, tente novamente.")
            continue

        if valida_cod_disciplinas(cod_disciplina, dados_disciplinas) == True:
            for disciplina in dados_disciplinas:
                if disciplina['Código'] == cod_disciplina:
                    infodisc = disciplina
            break
        else:
            print("Esta disciplina não existe, tente novamente.")
            continue
             
    infoturmas = {"Turma":n_turma,"Professor":infoprof,"Disciplina":infodisc}
    dados_turmas.append(infoturmas)


##########  LISTA TURMAS  ##########
def listar_turmas(dados_turmas):
    if len(dados_turmas) == 0:
        print("A lista está vazia")

    else:
        print('********** LISTA DE TURMAS **********')
        for turma in dados_turmas:
            print(turma)


########## ATUALIZA TURMAS  ##########
def atualizar_turmas(dados_turmas, dados_professores, dados_disciplinas):
    dados_disciplinas = carrega_dados_disciplinas()
    while True:  
        try:
            n_turma = int(input("Insira o número da turma que deseja atualizar: "))
        except:
            print("Código inválido, insira um valor numérico.")
            continue
        if valida_cod_turmas(n_turma, dados_turmas) == True:
            for index, turma in enumerate(dados_turmas):
                if n_turma == turma['Turma']:
                    dados_turmas.pop(index)
                    registra_dados_turmas(dados_turmas)
        
        else:
            print("Essa turma não existe, tente novamente.")
            continue
        break
    
    while True:
        try:
            cod_professor = int(input("Insira o código do professor: "))  
        except:
            print("Código inválido, tente novamente.")  
            continue
        if valida_cod_professores(cod_professor, dados_professores) == True:
            for professor in dados_professores:
                if professor['Código'] == cod_professor:
                    infoprof = professor
        else:
            print("Esse professor não existe, tente novamente.")
            continue
        break
    while True:
        try:    
            cod_disciplina = int(input("Insira o código da disciplina: "))
        except:
            print("Código inválido, insira um valor numérico.")
            continue
        if valida_cod_disciplinas(cod_disciplina, dados_disciplinas) == True:   
            for disciplina in dados_disciplinas:
                if disciplina['Código'] == cod_disciplina:
                    infodisc = disciplina
        else:
            print("Essa disciplina não existe, tente novamente.")
            continue
        break 

    infoturmas = {"Turma":n_turma,"Professor":infoprof,"Disciplina":infodisc}
    dados_turmas.append(infoturmas)
    registra_dados_turmas(dados_turmas)
    print(f"A turma *{turma['Turma']}* foi atualizada.")
        
        
##########  EXCLUI TURMAS  #########
def excluir_turmas(dados_turmas):
    while True:
        try:
            n_turma = int(input("Insira o número da turma que deseja excluir: "))
        except:
            print("Código inválido, tente novamente.")
            continue
        if valida_cod_turmas(n_turma, dados_turmas) == True:
            for turma in dados_turmas:
                for index, turma in enumerate(dados_turmas):
                    if n_turma == turma['Turma']:
                        dados_turmas.pop(index)
                        registra_dados_turmas(dados_turmas)
                        print(f"A turma *{turma}* foi excluída.")
        else:
            print("Essa turma não existe, tente novamente.")
            continue
                 
            

##########  VALIDA CODIGO DA TURMA  ##########
def valida_cod_turmas(n_turma, dados_turmas):
    for turma in dados_turmas:
        if n_turma == turma['Turma']:
            return True
        

##########  INSERIR MATRICULAS  ##########
def insere_estudantes_e_turmas(dados_matriculas,dados_estudantes, dados_turmas, indice_matricula):
    while True:
        try:
            cod_estudante = int(input("Insira o código do estudante: "))
        except:
            print("Código inválido, tente novamente.")
            continue
        if valida_cod_estudante(cod_estudante, dados_estudantes) == True:
            for estudante in dados_estudantes:
                if estudante['Código'] == cod_estudante:
                    infoestud = estudante
            break
        else:
            print("Este estudante não existe, tente novamente.")
            continue
    
    while True:
        try:
            cod_turma = int(input("Insira o código da turma: "))
        except:
            print("Código inválido, tente novamente.")
            continue
        if valida_cod_turmas(cod_turma, dados_turmas) == True:
            for turma in dados_turmas:
                if turma['Turma'] == cod_turma:
                    infoturma = turma
            break
        else:
            print("Esta turma não existe, tente novamente.")
            continue        
    infomatriculas = {"Matricula":indice_matricula,'':infoturma,"Estudante":infoestud} 
    dados_matriculas.append(infomatriculas)


##########  LISTAR MATRICULAS  ##########
def listar_matriculas(dados_matriculas):
    if len(dados_matriculas) == 0:
        print("A lista está vazia")

    else:
        print('********** LISTA DE MATRICULAS **********')
        for matricula in dados_matriculas:
            print(matricula)


########## ATUALIZA MATRICULAS ##########
def atualizar_matriculas(dados_matriculas, dados_estudantes, dados_turmas):
    while True:
        try:
            n_matricula = int(input("Insira o número da matricula que deseja atualizar: "))
        except:
            print("Código inválido, insira um valor numérico.")
            continue
        if valida_cod_matriculas(n_matricula, dados_matriculas) == True:
            for index, matricula in enumerate(dados_matriculas):
                if n_matricula == matricula['Matricula']:
                    dados_matriculas.pop(index)
                    registra_dados_matriculas(dados_matriculas)
        else:
            print("Essa matrícula não existe, tente novamente.")
            continue
        break
    
    while True:
        try:
            cod_estudantes = int(input("Insira o código do estudante: "))        
        
        except:
            print("Código inválido, tente novamente.")
            continue
        if valida_cod_estudante(cod_estudantes, dados_estudantes) == True:
            for estudante in dados_estudantes:
                if estudante['Código'] == cod_estudantes:
                    infoestud = estudante
        else:
            print("Esse estudante não existe, tente novamente")
            continue
        break
    
    while True:
        try:     
            cod_turmas = int(input("Insira o código da turma: "))
        except:
            print("Código inválido, tente novamente.")
            continue
        if valida_cod_turmas(cod_turmas, dados_turmas) == True:
            for turma in dados_turmas:
                if turma['Turma'] == cod_turmas:
                    infoturma = turma
        else:
            print("Essa turma não existe, tente novamente.")
            continue
        break

    infomatricula = {"Matricula":n_matricula,"Estudante":infoestud,"Turma":infoturma}
    dados_matriculas.append(infomatricula)
    registra_dados_matriculas(dados_matriculas)
    print(f"A matrícula {matricula['Matricula']} foi atualizada.")


##########  EXCLUI MATRÍCULA  ##########
def excluir_matriculas(dados_matriculas):
    while True:
        try:
            n_matricula = int(input("Insira o número da matrícula que deseja excluir: "))
        
        except:
            print("Esse código não existe, tente novamente.")
            continue

        if valida_cod_matriculas(n_matricula,dados_matriculas) == True:
            for matricula in dados_matriculas:
                for index, matricula in enumerate(dados_matriculas):
                    if n_matricula == matricula['Matricula']:
                        dados_matriculas.pop(index)
                        registra_dados_matriculas(dados_matriculas)
                        print(f"A Matrícula {matricula} foi excluída.")
        else:
            print("Essa matrícula não existe, tente novamente.")
            continue
        break


##########  VALIDA CODIGO DA MATRÍCULA  ##########
def valida_cod_matriculas(indice_matricula, dados_matriculas):
    for matricula in dados_matriculas:
        if indice_matricula == matricula['Matricula']:
            return True

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
            registra_dados_professores(dados_professores)
            
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
            dados_professores = carrega_dados_professores()
            dados_disciplinas = carrega_dados_disciplinas()

            if retorno_menu == 1:
                inserir(op,dados_estudantes, dados_professores, dados_disciplinas, dados_turmas, dados_matriculas)
                registra_dados_turmas(dados_turmas)
                titulo_menu_turmas()    
            
            elif retorno_menu == 2:
                listar_turmas(dados_turmas)
                titulo_menu_turmas()
                    
            elif retorno_menu == 3: 
                titulo_menu_turmas()
                atualizar_turmas(dados_turmas, dados_professores, dados_disciplinas)
                
                
            elif retorno_menu == 4:
                titulo_menu_turmas()
                excluir_turmas(dados_turmas)
                
            elif retorno_menu == 5:  
                break

            else:
                print("Opção inválida, tente novamente!")
                continue

##########  MENU MATRICULAS  ##########
def menu_matriculas():
    while True:
            opcoes_menu_operacoes()
            retorno_menu = int(input())
            dados_turmas = carrega_dados_turmas()
            dados_estudantes = carrega_dados_estudantes()

            if retorno_menu == 1:
                inserir(op,dados_estudantes, dados_professores, dados_disciplinas, dados_turmas, dados_matriculas)
                registra_dados_matriculas(dados_matriculas)
                titulo_menu_matriculas()    
            
            elif retorno_menu == 2:
                listar_matriculas(dados_matriculas)
                titulo_menu_matriculas()
                    
            elif retorno_menu == 3: 
                titulo_menu_matriculas()
                atualizar_matriculas(dados_matriculas, dados_estudantes, dados_turmas)
                
                
            elif retorno_menu == 4:
                titulo_menu_matriculas()
                excluir_matriculas(dados_matriculas)
                
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
            menu_matriculas()
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
         