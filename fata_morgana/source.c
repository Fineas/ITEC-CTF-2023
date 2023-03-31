#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <openssl/md5.h>

#define MD5_DIGEST_LENGTH 16

// Bytecode opcodes
#define OP_PUSH_BYTE 0x01
#define OP_ADD       0x02
#define OP_PRINT     0x03
#define OP_HALT      0x04

// Hardcoded hash = c41dca10e4c04d9e0251b5b99bb597b9
unsigned char hardcoded_hash[MD5_DIGEST_LENGTH] = {0xc4, 0x1d, 0xca, 0x10, 0xe4, 0xc0, 0x4d, 0x9e, 0x02, 0x51, 0xb5, 0xb9, 0x9b, 0xb5, 0x97, 0xb9};

// Xored flag
unsigned char xored_flag[] = {0x2f, 0x60, 0x31, 0x77, 0x16, 0x39, 0x75, 0x31, 0x2e, 0x60, 0x2b, 0x22, 0x16, 0x36, 0x24, 0x74, 0x7a, 0x0b, 0x26, 0x22, 0x24, 0x24, 0x74, 0x72, 0x16, 0x17, 0x30, 0x1c, 0x3c, 0x3a, 0x1a, 0x13, 0x06, 0x1f, 0x00, 0x0e, 0x06, 0x1a};


// Global bytecode data
unsigned char bytecode[] = {
    0x13,37
};

void functie(char *cheie) {
    int a = 1337;
    for(int i = 0; i < 38; i++) {
        xored_flag[i] ^= cheie[i%4];
    }
}

int main(int argc, char** argv) {

    // Get user input
    char user_input[256];
    printf("Enter a string: ");
    fgets(user_input, sizeof(user_input), stdin);

    // Hash the user input with MD5
    unsigned char hash[MD5_DIGEST_LENGTH];
    MD5((unsigned char*) user_input, strlen(user_input) - 1, hash);

    // Compare the hash to the hardcoded hash
    if (memcmp(hash, hardcoded_hash, MD5_DIGEST_LENGTH) == 0) {
        printf("Hashes match!\n");
    } else {
        printf("Hashes do not match.\n");
        return 0;
    }

    // Allocate executable memory region
    void* addr = (void*) 0x331337;
    void* code = mmap(addr, sizeof(bytecode), PROT_EXEC | PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);

    // Check for mmap failure
    if (code == MAP_FAILED) {
        perror("mmap");
        exit(EXIT_FAILURE);
    }

    // Copy bytecode to executable memory
    memcpy(code, bytecode, sizeof(bytecode));

    // Execute bytecode with input string on stack
    __asm__(
        "movq %0, %%rax\n"
        "movq $0x0000000000400000, %%rbx\n"
        "jmp %%rbx\n"
        : : "r"(input), "r"(code)
    );

    // Free executable memory region
    munmap(code, sizeof(bytecode));

    // Create input string
    char flag[16] = "ITEC{%s}";

    return 0;
}
