LENGHT = 1000
LENGHT = (LENGHT//3)*3 # numero certo de nucleotideos para conversão

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