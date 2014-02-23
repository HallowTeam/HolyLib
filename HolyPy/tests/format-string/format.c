#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void exploit()
{
	system("/bin/sh");
}

int main(void)
{
	void (* func)();
	char buff[1024];

	printf("%p\n", exploit);
	printf("%p\n", &func);

	fgets(buff, sizeof(buff), stdin);
	printf(buff);
	printf("%lx\n", func);

	func();

	return 0;
}
