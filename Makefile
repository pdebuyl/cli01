all: hello_args

CC=gcc
CFLAGS=-std=c99 -Wall

%: %.c
	$(CC) $(CFLAGS) -o $@ $<

clean:
	rm -f hello_args print_env_variable
