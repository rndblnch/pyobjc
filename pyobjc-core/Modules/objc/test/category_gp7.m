
/*
 *     *** GENERATED FILE ***
 *
 * This file is generated by Tools/generate-category-tests.py
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
__attribute__((__visibility__("default")))
@interface OC_Category_GP7 : NSObject {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_P7 : OC_Category_GP7 {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_C7 : OC_Category_P7 {
}
@end

@implementation
OC_Category_GP7 (Cat)
- (id)gpMethod1
{
    return @"GP7 - gpMethod1 - GP7(Cat)";
}
- (id)gpMethod5
{
    return @"GP7 - gpMethod5 - GP7(Cat)";
}
- (id)pMethod1
{
    return @"GP7 - pMethod1 - GP7(Cat)";
}
- (id)pMethod3
{
    return @"GP7 - pMethod3 - GP7(Cat)";
}
- (id)method1
{
    return @"GP7 - method1 - GP7(Cat)";
}
- (id)method2
{
    return @"GP7 - method2 - GP7(Cat)";
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "category_gp7", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_category_gp7(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_category_gp7(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    return m;
}
