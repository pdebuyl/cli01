#include <stdlib.h>
#include <stdio.h>

int main(void) {

  char *env_variable;

  env_variable = getenv("USER");

  if (NULL!=env_variable) printf("USER: %s\n", env_variable);

  env_variable = getenv("SHELL");

  if (NULL!=env_variable) printf("SHELL: %s\n", env_variable);

  env_variable = getenv("PATH");

  if (NULL!=env_variable) printf("PATH: %s\n", env_variable);

  return 0;
}
