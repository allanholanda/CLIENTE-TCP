import socket #Relaciona a placa de rede com o sistema operacional e com o programa
import sys #Fornece o acesso a algumas variáveis e funções que tem forte interação com o interpretador

def main ():
    try: #Tenta uma conexão TCP-IP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) #socket.AF_INET passa que vamos utilizar o protocolo ip; #socket.SOCK_STREAM passa que vamos utilizar TCP; #0 passa o protocolo tcp que iremos fazer a comunicação com o servidor

    except socket.error as e:

        print("A conexão falhou !")
        print("Erro: {}" .format (e))
        sys.exit() #Fecha o programa

    print("Socket criado com sucesso")


    HostAlvo = input("Digite o Host ou Ip a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo))) #Conecta o HOST solicitado na porta solicitada; #Temos que converter a string porta para inteiro para funcionar, pois o .connect aceita somente (string, int)
        print("Cliente TCP Host: " + HostAlvo + " e na Porta: " + PortaAlvo)
        s.shutdown(2) #Vai aguardar dois segundos para finalizar a conexão

    except socket.error as e:
        print("Não foi possível conectar no Host: " + HostAlvo + " - Porta: " + PortaAlvo)
        print("Erro: {}" .format(e))
        sys.exit()


if __name__ == "__main__": #Se o nome da função for "main" chame a função main
    main()