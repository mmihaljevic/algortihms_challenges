#include<stdio.h>
// sizeof - 4 na 64 bitnoj masini 
// Hence sizeof operator will return 4 because size of float data type in c is 4 byte.
// Value of any variable doesn’t modify inside sizeof operator. Hence value of variable a will remain 5.


int main()
{
  int a=5;
  float b; // garbage
  printf("%d",sizeof(++a+b));
  printf(" %d\n", a); 
  return 0;
}

