#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: a pointer to the listint_t
 *
 * Return: 0 if no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slwp = list;
	listint_t *fstp = list;
	
	while (fstp != NULL && fstp->next != NULL)
	{
		slwp = slwp->next;
		fstp = fstp->next->next;
		
		if (slwp == fstp)
			return (1);
	}
	return (0);
}
