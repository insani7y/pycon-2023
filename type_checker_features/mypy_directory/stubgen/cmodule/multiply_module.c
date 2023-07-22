#include <Python.h>

// The function that will be called from Python code
static PyObject* multiply(PyObject* self, PyObject* args) {
    double x, y, result;
    if (!PyArg_ParseTuple(args, "dd", &x, &y)) {  // Parse the Python arguments
        return NULL;
    }
    result = x * y;  // Multiply the two numbers
    return PyFloat_FromDouble(result);  // Return the result as a Python float
}

// An array of the methods provided by this module
static PyMethodDef MultiplyMethods[] = {
    {"multiply",  multiply, METH_VARARGS, "Multiply two numbers."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

// Module definition structure
static struct PyModuleDef multiplymodule = {
   PyModuleDef_HEAD_INIT,
   "multiply_module",   /* name of module */
   NULL, /* module documentation, may be NULL */
   -1,       /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */
   MultiplyMethods
};

PyMODINIT_FUNC
PyInit_multiply_module(void)
{
    return PyModule_Create(&multiplymodule);
}
