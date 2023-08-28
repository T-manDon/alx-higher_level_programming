/*
 * File: 103-python.c
 * Auth: authentification info
 */

#include <Python.h>

// Function prototypes
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - give basic info
 * @p: Pyobject variable
 */
void print_python_list(PyObject *p)
{
    // Extract list size and allocation info
    Py_ssize_t size, alloc, i;
    const char *type;
    PyListObject *list = (PyListObject *)p;
    PyVarObject *var = (PyVarObject *)p;

    size = var->ob_size;
    alloc = list->allocated;

    fflush(stdout);

    printf("[*] Python list info\n");
    if (strcmp(p->ob_type->tp_name, "list") != 0)
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", alloc);

    // Loop through list elements and print their types
    for (i = 0; i < size; i++)
    {
        type = list->ob_item[i]->ob_type->tp_name;
        printf("Element %ld: %s\n", i, type);

        // Call appropriate functions based on type
        if (strcmp(type, "bytes") == 0)
            print_python_bytes(list->ob_item[i]);
        else if (strcmp(type, "float") == 0)
            print_python_float(list->ob_item[i]);
    }
}

/**
 * print_python_bytes - funct to print basic inf
 * @p: pyObject variable
 */
void print_python_bytes(PyObject *p)
{
    // Extract byte object size and data
    Py_ssize_t size, i;
    PyBytesObject *bytes = (PyBytesObject *)p;

    fflush(stdout);

    printf("[.] bytes object info\n");
    if (strcmp(p->ob_type->tp_name, "bytes") != 0)
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
    printf("  trying string: %s\n", bytes->ob_sval);

    // Determine the number of bytes to print
    if (((PyVarObject *)p)->ob_size >= 10)
        size = 10;
    else
        size = ((PyVarObject *)p)->ob_size + 1;

    // Print the first few bytes of the data in hexadecimal
    printf("  first %ld bytes: ", size);
    for (i = 0; i < size; i++)
    {
        printf("%02hhx", bytes->ob_sval[i]);
        if (i == (size - 1))
            printf("\n");
        else
            printf(" ");
    }
}

/**
 * print_python_float - print info about float objects
 * @p: pyObject float variable
 */
void print_python_float(PyObject *p)
{
    // Buffer to hold float value as string
    char *buffer = NULL;

    PyFloatObject *float_obj = (PyFloatObject *)p;

    fflush(stdout);

    printf("[.] float object info\n");
    if (strcmp(p->ob_type->tp_name, "float") != 0)
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    // Convert the float value to a string and print it
    buffer = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
        Py_DTSF_ADD_DOT_0, NULL);
    printf("  value: %s\n", buffer);
    PyMem_Free(buffer);  // Free the allocated buffer
}
