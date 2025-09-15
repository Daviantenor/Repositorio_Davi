def ir_direto_para_escola():
    print(f"\nVocê anda um caminho razoável até a escola.")
def jogar_ping_pong_com_os_amigos():
    print(f"\nVocê vai para o terraço da fábrica de programadores e joga ping pong com os manos.")
def jogar_video_game():
    print(f"\nVocê fica ali na fábrica de programadores e começa a jogar o seu joguinho favorito.")

opção=int(input("Voçê acaba de sair da Fábrica de programadores,o que voçê deseja fazer? \n1-ir direto para a escola \n2-jogar ping pong com os amigos \n3-Jogar seu jogo favorito no seu celular. "))


if opção == 1:
    ir_direto_para_escola()
    opção2=int(input("\n você chega na escola mas ela está trancada o que voçê faz? \n1-sentar no banco da praça. \n2-Ficar andando por aí. \n3-ficar esperando a escola abrir em pé."))
    
   
        
    def sentar_no_banco():
                    print(f"Voçê senta no banco da praça e adormece.")
    def ficar_andando():
                    print(f"Voçê anda pela praça para se distrair um pouco.")
    def espera_a_escola_abrir_em_pé():
                    print(f"Voçê espera ali em pé , mas seu tédio começa a te matar.")
    if opção2 == 1:
                sentar_no_banco()
    elif opção2 ==2:
                ficar_andando()
    else:
                espera_a_escola_abrir_em_pé()

elif opção == 2:
    jogar_ping_pong_com_os_amigos()
    opção3=int(input("\n Você joga ping pong , porém um amigo seu esta quieto num canto do terraço , ele parece triste , o que voçê irá fazer? \n1-Falar com ele \n2-ignora-lo. \n3-Chegar nele e abraça-lo."))

    def falar():
                    print(f"Voçê está bem cara?")
    def ignorar():
                    print(f"Você só ignora e volta a jogar ping pong.")
    def abraçar():
                    print(f"Por quê voçê fez isso? , pergunta o seu amigo.")

    if opção3 == 1:
                falar()
    elif opção3 ==2:
                ignorar()
    else:
                abraçar()

else:
    jogar_video_game()



    
    
    
