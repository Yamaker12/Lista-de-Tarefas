#Lista de tarefa
#[1] Adicionar - adiciona algo da lista
#[2] Remover - remove algo da lista
#[3] Marcar - vai falar se ta feito ou não
#[4] Concluir - terminar a lista


Lista_Pendente= []
Lista_Concluida = []

Pergunta = input("Adicione um produto: ")
Lista_Pendente.append(Pergunta)

Adicionar = input("Quer adicionar mais? ")

if Adicionar == "Y" or Adicionar == "y":
    Pergunta2 = input("Adicione um produto: ")    
    Lista_Pendente.append(Pergunta2)
    print("Pendente:", Lista_Pendente)
    print("Concluido:", Lista_Concluida)  

elif Adicionar == "N" or Adicionar == "n":
    print("Pendente:", Lista_Pendente)
    print("Concluido:", Lista_Concluida)  
