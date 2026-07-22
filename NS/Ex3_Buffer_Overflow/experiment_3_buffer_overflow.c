/* 
 * Program: Vulnerable Buffer Overflow Demo
 * ----------------------------------------
 * This program demonstrates how buffer overflow can
 * overwrite variables in memory.
 * 
 * Compile: gcc -o overflow experiment_3_buffer_overflow.c -fno-stack-protector -z execstack
 * Run: ./overflow
 */
#include <stdio.h>
#include <string.h>

#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif

// Explicit declaration of gets to prevent compilation errors in modern C standards (C11+)
char *gets(char *str);

int main() {
    char buffer[10];    // small buffer
    int secret = 0;     // a variable we try to protect

    printf("=== Buffer Overflow Demonstration ===\n");
    printf("Enter some text: ");
    
    // gets() is dangerous and deprecated because it doesn't limit the input size.
    // It will overwrite adjacent memory if the input exceeds the buffer boundary.
    #pragma warning(suppress : 4996) // Suppress MSVC deprecation warning for gets
    gets(buffer);       // vulnerable function (unsafe)

    printf("\nYou entered: %s\n", buffer);
    printf("Secret value: %d\n", secret);

    if (secret == 12345) {
        printf("[OK] Buffer Overflow Successful! Secret value changed!\n");
    } else {
        printf("[INFO] Normal Execution. Secret not changed.\n");
    }

    return 0;
}
