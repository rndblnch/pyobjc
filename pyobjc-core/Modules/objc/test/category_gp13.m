
/*
 *     *** GENERATED FILE ***
 *
 * This file is generated by Tools/generate-category-tests.py
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
__attribute__((__visibility__("default")))
@interface OC_Category_GP13 : NSObject {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_P13 : OC_Category_GP13 {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_C13 : OC_Category_P13 {
}
@end

@implementation
OC_Category_GP13 (Cat)
- (id)gpMethod1
{
    return @"GP13 - gpMethod1 - GP13(Cat)";
}
- (id)gpMethod5
{
    return @"GP13 - gpMethod5 - GP13(Cat)";
}
- (id)pMethod1
{
    return @"GP13 - pMethod1 - GP13(Cat)";
}
- (id)pMethod3
{
    return @"GP13 - pMethod3 - GP13(Cat)";
}
- (id)method1
{
    return @"GP13 - method1 - GP13(Cat)";
}
- (id)method2
{
    return @"GP13 - method2 - GP13(Cat)";
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "category_gp13", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_category_gp13(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_category_gp13(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    return m;
}
