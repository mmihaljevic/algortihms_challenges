#include<stdio.h>
// size of pointer depends on an OS - 64 bit -> 8 byte
// 32 bitni -> 4 byte-a
// uname -a 
// 32 bitni -> 4g memorije ->  2^32


main()
{
    int x = 5;
    char c = 'c';
    
    printf("sizeof int: %u \n", sizeof(x));
    printf("sizeof char: %u \n" , sizeof(c));
    printf("sizeof pointer: %u \n", sizeof(char *));
}
