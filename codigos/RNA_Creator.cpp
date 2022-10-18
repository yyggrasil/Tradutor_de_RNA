#include <iostream>
#include <cstdlib>
#include <fstream>

using namespace std;
// tamanho do arquivo
define tam 10**10

int main(){

    ofstream arquivo("txt/RNA.txt");

    // NUMERO ALEATORIO DE 0 A 3
    int random = rand() % 4;

    char nucleotideos[4];
        nucleotideos[0] = 'G';
        nucleotideos[1] = 'C';
        nucleotideos[2] = 'A';
        nucleotideos[3] = 'U';

    for (int i = 0; i < tam; i++)
    {
        /* code */
    }
    

    return 0;
}