class Animais:

    def __init__(self, name, especie, age):
        self.name = name
        self.especie = especie
        self.age = age

    def exibir_informacoes(self):
        print(f"Nome: {self.name}, Especie: {self.especie}, Idade: {self.age}")


# _________ FUNÇÃO PRINCIPAL ________

def main():
    lista_de_animais = []   # lista para armazenar os animais

    while True:
        print("\nMenu:")
        print("\n1. Adicionar animal na lista")
        print("\n2. Exibir lista de animais")
        print("\n3. Sair")
        
        option = input("Escolha uma opcao acima: ")


        # Cadastro de um novo animal
        if option == "1":
            while True:
                                    
                name = input("Nome do animal: ")
                especie = input("Especie: ")
                age = input("Idade: ")

                animal = Animais(name, especie, age)
                lista_de_animais.append(animal)

                print("Sucesso! Animal adicionado no sistema.")

                # Perguntar se deseja adicionar outro animal:

                print("Deseja adicionar outro animal? ")
                print("1. sim")
                print("2. Voltar ao menu")
                escolha = input("Escolha uma opcao acima: ")
                
                if escolha == "1":
                    continue
                elif escolha == "2":
                    break
                else:
                    print("opcao invalida, voltando para o menu principal.")
                    break


        # listando animais
        elif option == "2":
            
                                      
            if not lista_de_animais:
                print("Nenhum animal cadastrado")

            else:
                print("\nAnimais cadastrados: ")
                for animal in lista_de_animais:
                    animal.exibir_informacoes()
        
        
        #saindo do programa
        elif option == "3":
            

            print("Saindo do sistema")
            break

        else:
            print("Opcao invalida \ntente novamente\n")


if __name__ == "__main__":
    main()



# Próximo passo
# adicionar lógica para alterar dados de algum animal cadastrado




    