#include<stdio.h>
void main()
{
printf("Hello World\n");
printf("Hi World\n");
fork();
fork();
fork();
printf("Hello World\n");
printf("Hi World\n");
}

/*
universe@809g:~$ ./a.out
Hello World
Hi World
Hello World
Hi World
Hello World
Hi World
Hello World
Hello World
Hi World
Hello World
Hi World
Hello World
Hi World
Hi World
universe@809g:~$ Hello World
Hi World
Hello World
Hi World
*/

