all: hello_args

CC=gcc
CFLAGS=-std=c99

%: %.c
	$(CC) $(CFLAGS) -o $@ $<

