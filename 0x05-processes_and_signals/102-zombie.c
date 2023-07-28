#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

/**
 * infinite_while - A function for an infinite loop
 *
 * Return: success (0)
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Entry point
 *
 * Return: success (0)
 */
int main(void)
{
	pid_t pid;
	int i = 0, j = 0;

	for (i; i < 5; i++)
	{
		pid = fork();
		if (pid > j)
			printf("Zombie process created, PID: %d\n", pid);
		else if (pid == j)
			exit(0);
	}
	infinite_while();

	return (0);
}
