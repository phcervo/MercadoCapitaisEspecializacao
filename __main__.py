# Importação de módulos

import pacotes
# Foi importada as funções contidas no arquivo pacotes.py

# Criando a função principal
def main():
    # Chamar com pacote.função
    dados=pacotes.entrada()

    #print(dados)

    resultado=pacotes.subtrai_and_quad(dados[0],dados[1])
    print(f'A subtração, com o quadrado adicionado é {resultado}')

# Chamando a função principal

#Esse bloco if abaixo serve para garantir a execução apenas se a variavel chamr-se 'main'
if __name__=="__main__":
    main()
