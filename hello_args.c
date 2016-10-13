#include <stdio.h>

int main(int argc, char *argv[]) {

  printf("Number of arguments: %i\n", argc-1);

  for (int i=1 ; i<argc ; i++) printf("%s ", argv[i]) ;
  printf("\n");

  return 0;
}
