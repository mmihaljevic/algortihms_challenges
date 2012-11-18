#include<stdio.h>
// Default parameter passing scheme of c is cdecl i.e. argument of 
// function will pass from right to left direction.

void call(int,int,int);
int main(){
  int a=10;
  call(a,a++,++a); 
  return 0;
}

void call(int x,int y,int z){
  printf("%d %d %d",x,y,z);
}

