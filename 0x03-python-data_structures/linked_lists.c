#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints the list elements
 * @h: the list pointer
 * Return: nodes
 */

size_t print_listint(const listint_t *h)

{

	    const listint_t *current;

	    unsigned int n; /* the nodes */

	    current = h;

	    n = 0;

	    while (current != NULL)

    {
		printf("%i\n", current->n);

		current = current->next;

		n++;
    }

    return (n);
}

/**
 * add_nodeint_end - function adds another node
 * @head: the head pointer
 * @n: the n pointer
 * Return: success for element addess
 */

listint_t *add_nodeint_end(listint_t **head, const int n)

{
	    listint_t *new;

	    listint_t *current;

	    current = *head;

	    new = malloc(sizeof(listint_t));

	    if (new == NULL)

		return (NULL);

	    new->n = n;

	    new->next = NULL;

	    if (*head == NULL)

		*head = new;
	    else

    {
		while (current->next != NULL)

		    current = current->next;

		current->next = new;
    }

	    return (new);
}

/**
 * free_listint - lets the listing free
 * @head: head pointer
 * Return: 0 succss
 */

void free_listint(listint_t *head)

{
	    listint_t *current;

	    while (head != NULL)

    {
		current = head;

		head = head->next;

		free(current);
    }
}
