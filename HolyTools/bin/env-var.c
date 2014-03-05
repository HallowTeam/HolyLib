#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ADDR_SIZE sizeof(void *)

int main(int argc, char ** argv)
{
	int i = 0;
	int x = 0;
	union {
		void *        a;
		unsigned char c[ADDR_SIZE];
	} addr;

	if (argc <= 1)
	{
		printf("Usage: %s @var [...]\n", argv[0]);
		return 1;
	}

	for (i = 1; i < argc; i++)
	{
		if ((addr.a = getenv(argv[i])) == NULL)
		{
			printf("[-] %s is not defined", argv[i]);
			continue;
		}

		printf("%s ADDR: %p\n", argv[i], addr.a);
		printf("%s LSB : ", argv[i]);
		for (x = 0; x < ADDR_SIZE; x++)
		{
			printf("\\x%02x", addr.c[ADDR_SIZE - 1 - x]);
		}
		printf("\n");

		printf("%s MSB : ", argv[i]);
		for (x = 0; x < ADDR_SIZE; x++)
		{
			printf("\\x%02x", addr.c[x]);
		}
		printf("\n");
	}

	return 0;
}
