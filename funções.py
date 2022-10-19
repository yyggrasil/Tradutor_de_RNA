from operator import truediv
from random import randint



# VARIAVEIS GLOBAIS


TAM = 1000
TAM = (TAM//3)*3 # numero certo de nucleotideos para conversão

nucleotides = ["G", "C", "A", "U"]

aminoacido = {
    'Alanina': ['GCU', 'GCG', 'GCC', 'GCA'],
    'Arginina': ['GCU', 'CGG', 'CGC', 'CGA', 'AGG', 'AGA'],
    'Acido aspartico': ['GAU', 'GAC'],
    'Aspargina': ['AUU', 'ACC'],
    'Cisteina': ['UGU', 'UGC'],
    'Acido glutamico': ['GAG', 'GAA'],
    'Glutanina': ['CAG', 'CAA'],
    'Glicina': ['GGU', 'GGG', 'GGC', 'GGA'],
    'Histidina': ['CAU', 'CAC'],
    'Isoleucina': ['AUU', 'AUC', 'AUA'],
    'Leucina': ['CUU', 'CUG', 'CUC', 'CUA', 'UUG', 'UUA'],
    'Lisina': ['AAG', 'AAA'],
    'Metionina': ['AUG'],
    'Fenilalanina': ['UUU', 'UUC'],
    'Prolina': ['CCU', 'CCG', 'CCC', 'CCA'],
    'Serina': ['UCU', 'UCG', 'UCC', 'UCA', 'AGU', 'AGC'],
    'Treonina': ['ACU', 'ACG', 'ACC', 'ACA'],
    'Triptofano':['UGG'],
    'Tirosina': ['UAU', 'UAC'],
    'Valina': ['GUU', 'GUG', 'GUC','GUA'],
    'Stop': ['UGA', 'UAG', 'UAA']
}

# FUNÇÕES A SEREM USADOS NO MAIN

#create DNA file
def Criar():
    
    f = open("txt/RNA.txt", "a")
    
    for i in range(0,TAM):
        number = randint(0,3)
        f.write(nucleotides[number])

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

