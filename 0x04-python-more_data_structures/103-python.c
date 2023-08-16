#include <stdio.h>
#include <Python.h>

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("[ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    char *string = PyBytes_AsString(p);
    Py_ssize_t limit = (size >= 10) ? 10 : size + 1;

    printf("[.] bytes object info\n");
    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", string);
    printf("  first %zd bytes:", limit);

    for (Py_ssize_t i = 0; i < limit; i++) {
        unsigned char byte = string[i];
        printf(" %02x", byte);
    }

    printf("\n");
}

void print_python_list(PyObject *p) {
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", list->allocated);

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *obj = PyList_GetItem(p, i);
        const char *typeName = Py_TYPE(obj)->tp_name;

        printf("Element %zd: %s\n", i, typeName);
        if (PyBytes_Check(obj))
            print_python_bytes(obj);
    }
}
