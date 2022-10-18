#call function to erase DNA
def erase(RNA, info):
    if RNA:
        open('RNA.txt', 'w').write('')
    if info:
        open('info_RNA.txt', 'w').write('')    

#print len of DNA
print(len(open('RNA.txt', 'r').read()))



erase(True, True)