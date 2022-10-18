r = open('RNA.txt', 'r')
RNA = r.read()
INFO = open('info_RNA.txt', 'a')
protein = ''


aminoacid = {
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


start_protein = False
for n in range(3, len(RNA), 3):
    #reset protein if haven't started
    if start_protein==False:
        protein = ''

    genetic_code = RNA[n-3:n]

    for amina, code in aminoacid.items():
        if genetic_code in code:
            if amina == 'Metionina':
                start_protein = True
            elif amina == 'Stop':
                start_protein = False
                if protein != '':
                    INFO.write(f'{protein}\n\n')
            else:
                protein += f'{amina} '
            
            

            
    


r.close()