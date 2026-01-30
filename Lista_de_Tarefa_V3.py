#Lista de tarefa
#[1] Adicionar - adiciona algo da lista
#[2] Remover - remove algo da lista
#[3] Marcar - vai falar se ta feito ou não
#[4] Concluir - terminar a lista


Lista_Pendente= []
Lista_Concluida = []

Check = True

#Loop pra quando a pessoa terminar a lista o Check ficar falso pra terminar o loop :D
while Check == True:

    Pergunta = input("Bem Vindo a sua lista escolha um numero!\n [1]Adicionar" \
    "\n [2]remover\n [3]Avaliar\n [4]Concluir\n")

#Adicionar o produto seila
    if Pergunta == "1":
        Adicionar = input("Adicione o que você quer na lista: ")
        Lista_Pendente.append(Adicionar)
        print("Lista Pendente: ")
        for Numero , item_pendente in enumerate(Lista_Pendente):
            print(f'Pendente {Numero}: {item_pendente}') 
        print("Lista Concluida:")
        for numeral, item_concluido in enumerate(Lista_Concluida):
            print(f'Concluida {numeral}: {item_concluido}')
        
    
#Remover o produto
    elif Pergunta == "2":
        Pergunta_Removedora_Categorica = input("qual categoria você quer remover, [p]Pendente ou [c]Concluida? ")
        #Se for a pessoa quiser remover a Pendente
        if Pergunta_Removedora_Categorica.lower() in ("p", "pendente"):
            print("Lista Pendente: ")
            for Numero , item_pendente in enumerate(Lista_Pendente):
                print(f'Pendente {Numero}: {item_pendente}')

            Pergunta_Removedora_Pendente = int(input("insira o numero do objetivo que quer remover: "))
            Lista_Pendente.pop(Pergunta_Removedora_Pendente)
            print("Lista Concluida: ")
            for Numero , item_pendente in enumerate(Lista_Pendente):
                print(f'Concluida {Numero}: {item_pendente}')

            

        #Se a pessoa quiser remover a Concluida
        elif Pergunta_Removedora_Categorica.lower() in ("c", "concluida","concluido"):
            print("Lista Pendente: ")
            for Numero , item_concluido in enumerate(Lista_Concluida):
                print(f'Pendente {Numero}: {item_concluido}')

            Pergunta_Removedora_Concluida = int(input("insira o numero do objetivo que quer remover: "))
            Lista_Concluida.pop(Pergunta_Removedora_Concluida)
            print("Lista Concluida")
            for Numero , item_concluido in enumerate(Lista_Concluida):
                print(f'Concluido {Numero}: {item_concluido}')




#Avaliar se foi concluida ou Não
    elif Pergunta == "3":
        print("Lista Pendente: ")
        for Numero , item_pendente in enumerate(Lista_Pendente):
            print(f'Pendente {Numero}: {item_pendente}') 

        Pergunta_Avaliadora = int(input("Insira o Numero da lista pendente: "))
        Item_removido = Lista_Pendente.pop(Pergunta_Avaliadora)
        Lista_Concluida.append(Item_removido)

        print("Lista Pendente: ")

        for Numero , item_pendente in enumerate(Lista_Pendente):
            print(f'Pendente {Numero}: {item_pendente}') 

        print("Lista Concluida: ")

        for numeral, item_concluido in enumerate(Lista_Concluida):
            print(f'Concluida {numeral}: {item_concluido}')
        

       
    
    elif Pergunta == "4":
        print("Lista Pendente: ")
        for Numero , item_pendente in enumerate(Lista_Pendente):
            print(f'Pendente {Numero}: {item_pendente}') 
        print("Lista Concluida: ")
        for numeral, item_concluido in enumerate(Lista_Concluida):
            print(f'Concluida {numeral}: {item_concluido}')
        Check = False



