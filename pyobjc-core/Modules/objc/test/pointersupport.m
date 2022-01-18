/*
 * Helper methods opaque-pointer tests (objc.test.test_opaque)
 */
#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

struct objc_class;

static CFStringRef aString = CFSTR("a static string");

@interface OC_PointerSupport : NSObject {
}
@end

@implementation OC_PointerSupport
+ (Py_ssize_t)getObjectLen:(PyObject*)value
{
    return PyObject_Length(value);
}

+ (PyObject*)getNone
{
    Py_INCREF(Py_None);
    return Py_None;
}

+ (struct objc_class*)getClass
{
    return (struct objc_class*)[OC_PointerSupport class];
}

+ (id)className:(struct objc_class*)class
{
    if (class == Nil) {
        return @"No class given";
    }
    return [NSString
        stringWithUTF8String:(const char* _Nonnull)class_getName((Class) class)];
}

+ (CFStringRef)getString
{
    return aString;
}

+ (CFStringRef)getContext
{
    return (CFStringRef)kCFAllocatorUseContext;
}

@end

static PyObject*
make_opaque_capsule(PyObject* mod __attribute__((__unused__)))
{
    return PyCapsule_New((void*)1234, "objc.__opaque__", NULL);
}

static PyObject*
make_object_capsule(PyObject* mod __attribute__((__unused__)))
{
    NSObject* object = [[[NSObject alloc] init] autorelease];
    return PyCapsule_New(object, "objc.__object__", NULL);
}

static PyMethodDef mod_methods[] = {{
                                        "opaque_capsule",
                                        (PyCFunction)make_opaque_capsule,
                                        METH_NOARGS,
                                        0,
                                    },
                                    {
                                        "object_capsule",
                                        (PyCFunction)make_object_capsule,
                                        METH_NOARGS,
                                        0,
                                    },
                                    {0, 0, 0, 0}};

static struct PyModuleDef mod_module = {PyModuleDef_HEAD_INIT,
                                        "pointersupport",
                                        NULL,
                                        0,
                                        mod_methods,
                                        NULL,
                                        NULL,
                                        NULL,
                                        NULL};

PyObject* PyInit_pointersupport(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_pointersupport(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) < 0) {
        return NULL;
    }

    if (PyModule_AddObject(m, "OC_PointerSupport",
                           PyObjC_IdToPython([OC_PointerSupport class]))
        < 0) {
        return NULL;
    }

    return m;
}
