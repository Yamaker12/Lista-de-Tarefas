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
        print("Pendente: ", Lista_Pendente)
        print("Concluida: ", Lista_Concluida)
    
#Remover o produto
    elif Pergunta == "2":
        Pergunta_Removedora_Categorica = input("qual categoria você quer remover, [p]Pendente ou [c]Concluida? ")
        #Se for a pessoa quiser remover a Pendente
        if Pergunta_Removedora_Categorica.lower() in ("p", "pendente"):
            Pergunta_Removedora_Pendente = input("insira o nome do objetivo que quer remover: ")
            Lista_Pendente.remove(Pergunta_Removedora_Pendente)

            print("Pendente: ", Lista_Pendente)
            print("Concluida: ", Lista_Concluida)

        #Se a pessoa quiser remover a Concluida
        elif Pergunta_Removedora_Categorica.lower() in ("c", "concluida","concluido"):
            Pergunta_Removedora_Concluida = input("insira o nome do objetivo que quer remover: ")
            Lista_Pendente.remove(Pergunta_Removedora_Concluida)

            print("Pendente: ", Lista_Pendente)
            print("Concluida: ", Lista_Concluida)

#Avaliar se foi concluida ou Não
    elif Pergunta == "3":
        Pergunta_Avaliadora = input("Insira o NOME do objetivo que concluiu: ")
        Lista_Pendente.remove(Pergunta_Avaliadora)
        Lista_Concluida.append(Pergunta_Avaliadora)

        print("Pendente: ", Lista_Pendente)
        print("Concluida: ", Lista_Concluida)
    
    elif Pergunta == "4":

        print("Pendente: ",Lista_Pendente,"\nConcluida: ",Lista_Concluida)
        Check = False
