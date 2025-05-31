#include <stdlib.h>
#include <stdio.h>

#include <Python.h>


int fib_rec_c_impl(int n)
{
    if (n < 3)
        return 1;

    return fib_rec_c_impl(n - 1) + fib_rec_c_impl(n - 2);
}


int fib_iter_c_impl(int n)
{
    int a = 0, b = 1;
    for (int i = 0; i < n; ++i)
    {
        int tmp = b;
        b = a + b;
        a = tmp;
    }
    return a;
}


PyObject *fibutils_capi_fib_rec_c(PyObject* self, PyObject* args)
{
    int n;
    if (!PyArg_ParseTuple(args, "i", &n))
        return NULL;

    int res = fib_rec_c_impl(n);
    return PyLong_FromLong(res);
}


PyObject *fibutils_capi_fib_iter_c(PyObject* self, PyObject* args)
{
    int n;
    if (!PyArg_ParseTuple(args, "i", &n))
        return NULL;

    int res = fib_iter_c_impl(n);
    return PyLong_FromLong(res);
}


static PyMethodDef methods[] = {
    {"fib_rec_c", fibutils_capi_fib_rec_c, METH_VARARGS, "recursive fib with C-api"},
    {"fib_iter_c", fibutils_capi_fib_iter_c, METH_VARARGS, "iter fib with C-api"},
    {NULL, NULL, 0, NULL},
};


static struct PyModuleDef module_fibutils_capi = {
    PyModuleDef_HEAD_INIT, "fibutils_capi", NULL, -1, methods
};


PyMODINIT_FUNC PyInit_fibutils_capi()
{
    return PyModule_Create( &module_fibutils_capi );
}
