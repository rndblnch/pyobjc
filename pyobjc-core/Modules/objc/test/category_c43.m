
/*
 *     *** GENERATED FILE ***
 *
 * This file is generated by Tools/generate-category-tests.py
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
__attribute__((__visibility__("default")))
@interface OC_Category_GP43 : NSObject {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_P43 : OC_Category_GP43 {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_C43 : OC_Category_P43 {
}
@end

@implementation
OC_Category_C43 (Cat)
- (id)gpMethod1
{
    return @"C43 - gpMethod1 - C43(Cat)";
}
- (id)gpMethod5
{
    return @"C43 - gpMethod5 - C43(Cat)";
}
- (id)pMethod1
{
    return @"C43 - pMethod1 - C43(Cat)";
}
- (id)pMethod3
{
    return @"C43 - pMethod3 - C43(Cat)";
}
- (id)method1
{
    return @"C43 - method1 - C43(Cat)";
}
- (id)method2
{
    return @"C43 - method2 - C43(Cat)";
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "category_c43", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_category_c43(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_category_c43(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    return m;
}
