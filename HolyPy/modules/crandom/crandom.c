#include <Python.h>

static PyObject * crandom_srand(PyObject * self, PyObject * args)
{
	int seed;

	PyArg_ParseTuple(args, "i", &seed);

	srand(seed);

	Py_RETURN_NONE;
}

static PyObject * crandom_rand(PyObject * self, PyObject * args)
{
	return Py_BuildValue("i", rand());
}

static PyMethodDef crandom_methods[] =
{
	{"rand"  , crandom_rand , METH_VARARGS},
	{"srand" , crandom_srand, METH_VARARGS},
	{NULL    , NULL}
};

void initcrandom()
{
	(void) Py_InitModule("crandom", crandom_methods);
}
