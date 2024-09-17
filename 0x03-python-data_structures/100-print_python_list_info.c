#include <Python.h>
void print_python_list_info(pyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("Invalid List object\n");
		return;
	}
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the python list = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject * item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_Type(item)->tp_name);
	}
}
