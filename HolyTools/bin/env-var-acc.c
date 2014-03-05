#define _BSD_SOURCE

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <sys/stat.h>
#include <sys/types.h>

int     main(int argc, char **argv)
{
	int           offset;
	char          *addr;
	struct stat   stats;

	if (argc < 3)
	{
		printf("Usage: %s <VAR> <PROC>\n", argv[0]);
		return 0;
	}

	if ((addr = getenv(argv[1])) == NULL)
	{
		printf("%s is not defined\n", argv[1]);
		return 0;
	}

	if (stat(argv[2], &stats) == -1)
	{
		printf("%s doesn't exist or is not readable\n", argv[2]);
		return 0;
	}

	offset = strlen(realpath(argv[0], NULL)) - strlen(realpath(argv[2], NULL));

	printf("Path argv[0]    : %s\n", realpath(argv[0], NULL));
	printf("Path argv[2]    : %s\n", realpath(argv[2], NULL));
	printf("Offset          : %d\n", offset);
	printf("Address argv[0] : \\x%02lx\\x%02lx\\x%02lx\\x%02lx (%#08lx)\n",
				 (0x000000FF & (long)addr) >> 0,
				 (0x0000FF00 & (long)addr) >> 8,
				 (0x00FF0000 & (long)addr) >> 16,
				 (0xFF000000 & (long)addr) >> 24, (long)addr);
	printf("Address argv[2] : \\x%02lx\\x%02lx\\x%02lx\\x%02lx (%#08lx)\n",
				 (0x000000FF & (long)(addr + offset)) >> 0,
				 (0x0000FF00 & (long)(addr + offset)) >> 8,
				 (0x00FF0000 & (long)(addr + offset)) >> 16,
				 (0xFF000000 & (long)(addr + offset)) >> 24, (long)(addr + offset));

	return 0;
}
