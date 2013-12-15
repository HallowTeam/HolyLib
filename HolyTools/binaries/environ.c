#include <stdio.h>
#include <stdlib.h>

int     main(int argc, char **argv, char **environ)
{
	int   i;

	for (i = 0; environ[i]; i++)
	{
		printf("%s: \\x%02lx\\x%02lx\\x%02lx\\x%02lx (%#08lx)\n", environ[i],
					 (0x000000FF & (long)&environ[i]) >> 0,
					 (0x0000FF00 & (long)&environ[i]) >> 8,
					 (0x00FF0000 & (long)&environ[i]) >> 16,
					 (0xFF000000 & (long)&environ[i]) >> 24, (long)&environ[i]);
	}

	return 0;
}
