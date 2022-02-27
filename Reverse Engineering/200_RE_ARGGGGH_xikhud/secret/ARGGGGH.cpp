#include "obfuscate.h"
#include "base64.h"
#include <stdio.h>
#include <string.h>

#define N (256)   // 2^8

void swap(unsigned char *a, unsigned char *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

int KSA(char *key, unsigned char *S) {

    int len = strlen(key);
    int j = 0;

    for(int i = 0; i < N; i++)
        S[i] = i;

    for(int i = 0; i < N; i++) {
        j = (j + S[i] + key[i % len]) % N;

        swap(&S[i], &S[j]);
    }

    return 0;
}

int PRGA(unsigned char *S, char *plaintext, unsigned char *ciphertext) {

    int i = 0;
    int j = 0;

    for(size_t n = 0, len = strlen(plaintext); n < len; n++) {
        i = (i + 1) % N;
        j = (j + S[i]) % N;

        swap(&S[i], &S[j]);
        int rnd = S[(S[i] + S[j]) % N];

        ciphertext[n] = rnd ^ plaintext[n];

    }

    return 0;
}

int RC4(char *key, char *plaintext, unsigned char *ciphertext) {

    unsigned char S[N];
    KSA(key, S);

    PRGA(S, plaintext, ciphertext);

    return 0;
}
//f0rtn1ght{arc4_And_base64_boizzz}
int main(int argc, char* argv[])
{
    char password[256];
    printf(AY_OBFUSCATE("Please enter the password: "));
    fgets(password, sizeof(password), stdin);
    password[strlen(password)-1] = 0;
    char* encode = base64_encode(password);
    char* e2 = (char*)calloc(strlen(encode)+1, sizeof(char));
    // for (int i = 0; i < strlen(encode); ++i)
    // {
    //     printf("%02x ", (unsigned char)encode[i]);
    // }
    // puts("");
    RC4(AY_OBFUSCATE("YEKDx2ZoxDcCFZzjnhx8Vx8y9mp7DySPhKipmz0s"), encode, (unsigned char*)e2);
    if (strcmp(e2, AY_OBFUSCATE("\xc5\xf4\xce\x03\x2a\xd2\xff\x38\x1e\xbd\x67\x49\xe4\x10\xe6\x86\x11\xe8\x3b\x10\x18\x86\xdf\xef\xa8\xa7\x98\x38\x69\xab\xc4\xee\xe1\x5a\x4a\x54\x8b\xe1\x03\x21\x5c\xaf\x13\x6e")) == 0)
        printf(AY_OBFUSCATE("Good, flag is %s\n"), password);
    else
        printf(AY_OBFUSCATE("Wrong\n"));
    free(e2);
    free(encode);
    return 0;
}