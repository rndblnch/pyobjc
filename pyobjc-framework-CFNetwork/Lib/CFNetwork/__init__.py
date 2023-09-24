"""
Python mapping for the CFNetwork framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys
    import os

    import CoreFoundation
    import objc
    from . import _metadata, _manual

    frameworkPath = "/System/Library/Frameworks/CFNetwork.framework"
    if not os.path.exists(frameworkPath):
        frameworkPath = "/System/Library/Frameworks/CoreServices.framework"

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="CFNetwork",
        frameworkIdentifier="com.apple.CFNetwork",
        frameworkPath=objc.pathForFramework(frameworkPath),
        globals_dict=globals(),
        inline_list=None,
        parents=(_manual, CoreFoundation),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["CFNetwork._metadata"]


globals().pop("_setup")()


def CFSocketStreamSOCKSGetError(err):
    return err.error & 0xFFFF


def CFSocketStreamSOCKSGetErrorSubdomain(err):
    return (err.error >> 16) & 0xFFFF
