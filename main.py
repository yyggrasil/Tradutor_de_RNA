from random import randint
#banco de dados
import dados

TAM = dados.LENGHT




#create DNA file
def Criar():
    
    f = open("txt/RNA.txt", "a")
    
    for i in range(0,TAM):
        number = randint(0,3)
        f.write(dados.nucleotides[number])

#ESCREVE AS INFORMAÇÕES DO RNA EM TXT
def info():

    inf = open("txt/info_RNA.txt", "a")
    RNA = open("txt/RNA.txt", "r")

    inf.write(f"""------ INFORMAÇÕES DO RNA ----- 
    Tamanho: { len(RNA.read()) }""")

    
#call function to erase DNA
def erase():
    
    open("txt/RNA.txt", "w").write("")
    open("txt/info_RNA.txt", "w").write("")    
    
def traduzir():
    RNA = open('txt/RNA.txt', 'r')
    RNA = RNA.read()
    INFO = open('txt/info_RNA.txt', 'a')
    INFO.write("\n\n                           Proteinas:  \n")
    
    Proteina = ''
    for n in range(3, len(RNA), 3):

        # pega uma secção de 3 nucleotideos
        Código_Genético = RNA[n-3:n]

        for amina, codigo in dados.aminoacido.items():
            if Código_Genético in codigo:
                
                if amina == 'Stop':
                    if Proteina != '':
                        INFO.write(f'{Proteina}\n\n')
                else:
                    Proteina += f'{amina} '


#main

erase()
Criar()
info()
traduzir()