#include<stdio.h>
// output 5 0 0
// Storage class of an array which initializes the element of the array 
// at the time of declaration is static. Default initial value of static integer is zero.

int main()
{
  int array[3]={5};
  int i;
  for(i=0;i<=2;i++)
    printf("%d ",array[i]); 
  return 0;
}
