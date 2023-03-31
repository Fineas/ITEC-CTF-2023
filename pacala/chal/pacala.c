#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>

void functie_secreta() {
    system("/bin/sh");
}

void genereaza_securitatea(unsigned char *canary) {
    srand(time(0));
    for (int i = 0; i < 8; i++) {
        canary[i] = rand() % 256;
    }
}

int autentificare() {
    char lungime_maxima = 16;
    char lungime_canary = 8;
    long int lungime_username = 0;
    unsigned char username[lungime_maxima + lungime_canary];
    unsigned char canary[8];

    genereaza_securitatea(canary);

    memset(username, 0, lungime_maxima + lungime_canary);
    memcpy(username + lungime_maxima, canary, 8);

    printf("[*] Introduceti lungimea username-ului: ");
    scanf("%hhd", &lungime_username);

    if ((char)lungime_username >= lungime_maxima) {
        puts("[!] Valoare prea mare!");
        return 0;
    }

    printf("[*] Introduceti Username-ul: ");
    read(0, username, lungime_username);

    for (int i = 0; i < 8; i++) {
        if (username[lungime_maxima + i] != canary[i]) {
            puts("[!] Securitatea a fost compromisa.\n");
            return 0;
        }
    }

    if (strcmp(username, "pacala_mare_bos") == 0) {
        return 1;
    }
    else {
        return 0;
    }
}

int main() {

    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);

    puts("Pacala 2.0!");
    puts("Cel mai pacalicios sistem tehnologic de pe intreg internetul.\n");

    if ( autentificare() ) {
        puts("[*] Autentificare cu succes!");
    }
    else {
        puts("[!] Autentificare esuata!");
    }

    return 0;
}
