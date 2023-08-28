#include "lists.h"

/**
 * insert_node - Inserts a number.
 * @head: head pointer
 * @number: int variable
 * Return: 0
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *node = *head, *new;

    // Allocate memory for the new node
    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    // Initialize the new node
    new->n = number;

    // If the list is empty or the new node should be inserted at the beginning
    if (node == NULL || node->n >= number)
    {
        new->next = node;
        *head = new;  // Update the head pointer to point to the new node
        return (new);
    }

    // Traverse the list to find the correct position to insert the new node
    while (node && node->next && node->next->n < number)
        node = node->next;

    // Insert the new node into the list
    new->next = node->next;
    node->next = new;

    return (new);
}
