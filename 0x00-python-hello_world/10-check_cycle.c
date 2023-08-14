#include "lists.h"

/**
 * check_cycle - determines if there is a circle
 * @list: the provided linked list
 * Return:1 for success or 0 for fail
 */

int check_cycle(listint_t *list)

{
listint_t *slow = list;
listint_t *fast = list;

if (!list)
return (0);

while (slow && fast && fast->next)
{
slow = slow->next;
fast = fast->next->next;
if (slow == fast)
return (1);
}
return (0);
}
