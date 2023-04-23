#NOME: Gabriel Soares de Menezes
#RA: 112023100378
#Curso: Análise e desenvolvimento de sistemas
#GITHUB: https://github.com/GabrielMenezes98/ATP-Raciocinio_Comp
#Em Desenvolvimento

#VARIAVEIS GLOBAIS
lista_estudantes = []



#Inclui estudantes (done)
def inserir_estudantes():
    qntd_estudantes = int(input("Quantos estudantes você deseja inserir?: "))
    for _ in range(qntd_estudantes):
        codigo = input("Insira o código do estudante: ")
        nome = input("Insira o nome do estudante: ") 
        cpf = input("Insira o CPF: ")
        infoestudante = (codigo, nome, cpf)
        lista_estudantes.append(infoestudante)
        

#FUNÇÃO PARA LISTAGEM
def listar_estudantes():
    if len(lista_estudantes) == 0:
            print("A lista está vazia")
    
    else:
    
        for i in range (len(lista_estudantes)):
            listaestudante = lista_estudantes[i]
            print(f"Código: {listaestudante[0]}, Nome: {listaestudante[1]}, CPF: {listaestudante[2]} ")

#FUNÇÃO PARA ATUALIZAR (DONE)
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


#FUNÇÃO PARA EXCLUIR (DONE)
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
               

#AVISO DE DESENVOLVIMENTO
def em_desenvolvimento():
     print("Em desenvolvimento")

#OPÇÕES DO MENU DE OPERAÇÕES
def opcoes_menu_operacoes():
    print("(1) Incluir.")  
    print("(2) Listar.")
    print("(3) Atualizar.")
    print("(4) Excluir.")
    print("(5) Voltar ao menu principal.")


#MENU DE OPERAÇÕES
def menu_estudantes():
    subop = int
    while subop != 5:
        opcoes_menu_operacoes()
        retorno_menu = int(input())
        
        if retorno_menu == 1:
            inserir_estudantes()
            titulo_menu_estudantes()    
        elif retorno_menu == 2:
            listar_estudantes()
            titulo_menu_estudantes()
                
        elif retorno_menu == 3: 
            titulo_menu_estudantes()
            codigo_atualizacao = input("Qual o código do estudante que deseja atualizar? ")
            nome = input("Insira o nome: ")
            cpf = input("Insira o CPF: ")
            novo_estudante = codigo_atualizacao, nome, cpf
            atualizar_estudante(lista_estudantes, codigo_atualizacao, novo_estudante)
            

        elif retorno_menu == 4:
            titulo_menu_estudantes()
            codigo_exclusao = (input("Qual o código do estudante que deseja excluir? "))
            excluir_estudante(lista_estudantes, codigo_exclusao)
        
            
        elif retorno_menu == 5:  
            subop = 5
            
        
#TITULOS
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
            em_desenvolvimento()
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



