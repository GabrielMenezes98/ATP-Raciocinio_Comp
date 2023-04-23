#NOME: Gabriel Soares de Menezes
#RA: 112023100378
#Curso: Análise e desenvolvimento de sistemas
#Em Desenvolvimento
#GITHUB: https://github.com/GabrielMenezes98/ATP-Raciocinio_Comp

#MENU PRINCIPAL
op = int
while  op != 9:
    subop = 0    
    print("----- MENU PRINCIPAL -----")
    print("1 - Gerenciar estudantes. ")
    print("2 - Gerenciar professores.")
    print("3 - Gerenciar disciplinas.")
    print("4 - Gerenciar turmas.")
    print("5 - Gerenciar matrículas.")
    print("9 - Sair")
    op = int(input())



    

#Menu de gerenciar estudantes
    if op == 1:
        while subop != 9:
            print("***** [ESTUDANTES] MENU DE OPERAÇÕES *****")
            print("(1) Incluir.")
            print("(2) Listar.")
            print("(3) Atualizar.")
            print("(4) Excluir.")
            print("(9) Voltar ao menu principal.")
            subop = int(input())
        
            
#Menu de operações (deverá ser uma função?)
            if subop == 1:
                print ("Você selecionou incluir.")
                
            elif subop == 2:
                print ("Você selecionou listar.")
                
            elif subop == 3:
                print ("Em desenvolvimento")
                
            elif subop == 4:
                print ("Você selecionou excluir.")
                
            elif subop != 9:
                print("Opção inválida")
        
        
            
        
#Menu de gerenciar professores
    elif op == 2:
        while subop != 9:
            print("***** [PROFESSORES] MENU DE OPERAÇÕES *****")
            print("(1) Incluir.")
            print("(2) Listar.")
            print("(3) Atualizar.")
            print("(4) Excluir.")
            print("(9) Voltar ao menu principal.")
            subop = int(input())
    
#Menu de operações (deverá ser uma função?)
            if subop == 1:
                print ("Você selecionou incluir.")
                
            elif subop == 2:
                print ("Você selecionou listar.")
                
            elif subop == 3:
                print ("Você selecionou atualizar.")
                
            elif subop == 4:
                print ("Você selecionou excluir.")
                
            elif subop != 9:
                print("Opção inválida")
               

#Menu de gerenciar disciplinas
    elif op == 3:
        while subop != 9:
            print("***** [DISCIPLINAS] MENU DE OPERAÇÕES *****")
            print("(1) Incluir.")
            print("(2) Listar.")
            print("(3) Atualizar.")
            print("(4) Excluir.")
            print("(9) Voltar ao menu principal.")
            subop = int(input())
    
#Menu de operações (deverá ser uma função?)
            if subop == 1:
                print ("Você selecionou incluir.")
                
            elif subop == 2:
                print ("Você selecionou listar.")
                
            elif subop == 3:
                print ("Você selecionou atualizar.")
                
            elif subop == 4:
                print ("Você selecionou excluir.")
                
            elif subop != 9:
                print("Opção inválida")
                
        
#Menu de gerenciar turmas
    elif op == 4:
        while subop != 9:
            print("***** [TURMA] MENU DE OPERAÇÕES *****")
            print("(1) Incluir.")
            print("(2) Listar.")
            print("(3) Atualizar.")
            print("(4) Excluir.")
            print("(9) Voltar ao menu principal.")
            subop = int(input())
    
#Menu de operações (deverá ser uma função?)
            if subop == 1:
                print ("Você selecionou incluir.")
                
            elif subop == 2:
                print ("Você selecionou listar.")
                
            elif subop == 3:
                print ("Você selecionou atualizar.")
                
            elif subop == 4:
                print ("Você selecionou excluir.")
                
            elif subop != 9:
                print("Opção inválida")
                
        print("TESTE4") 
#Menur de gerenciar Matrículas
    elif op == 5:
        while subop != 9:
            print("***** [MATRÍCULAS] MENU DE OPERAÇÕES *****")
            print("(1) Incluir.")
            print("(2) Listar.")
            print("(3) Atualizar.")
            print("(4) Excluir.")
            print("(9) Voltar ao menu principal.")
            subop = int(input())

#Menu de operações (deverá ser uma função?)
            if subop == 1:
                print ("Você selecionou incluir.")
                
            elif subop == 2:
                print ("Você selecionou listar.")
                
            elif subop == 3:
                print ("Você selecionou atualizar.")
                
            elif subop == 4:
                print ("Você selecionou excluir.")
                
            elif subop != 9:
                print("Opção inválida")
                 

    elif op != 9:
                print("Opção inválida")



