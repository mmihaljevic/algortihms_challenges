#include<stdio.h>
// gcc will complain
// example5.c: In function ‘main’:
// example5.c:6:3: warning: format ‘%d’ expects a matching ‘int’ argument [-Wformat]
// example5.c:6:3: warning: format ‘%d’ expects a matching ‘int’ argument [-Wformat]
// example5.c:6:3: warning: format ‘%d’ expects a matching ‘int’ argument [-Wformat]
// - will print garbage

int main()
{
  int x=5,y=10,z=15;
  printf("%d %d %d"); 
  return 0;
}

