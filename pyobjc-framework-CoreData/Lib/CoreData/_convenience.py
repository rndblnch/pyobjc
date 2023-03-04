"""
This adds some useful conveniences to NSManagedObject and subclasses thereof

These conveniences try to enable KVO by default on NSManagedObject instances,
this no longer works on Leopard due to the way NSManagedObject is implemented
there (it generates accessor methods at runtime, which interferes with the
implementation in this file).
"""
__all__ = ()
import os

from Foundation import NSObject
from objc import addConvenienceForClass, super

# XXX: This is fairly crude, need further research.
#      This code basically tries to outsmart tricks that
#      CoreData plays, and that's asking for problems.
if os.uname()[2] < "13.":

    def _first_python(cls):
        if "__objc_python_subclass__" in cls.__dict__:
            return cls
        return None

else:

    def _first_python(cls):
        for cls in cls.mro():  # noqa: B020
            if "__objc_python_subclass__" in cls.__dict__:
                return cls
        return None


def NSMOsetValue_ForKey_(self, name, value):
    try:
        first = _first_python(self.__class__)
        if first is not None:
            super(first, self).setValue_forKey_(value, name)
        else:
            self.setValue_forKey_(value, name)

    except KeyError:
        NSObject.__setattr__(self, name, value)


def NSMOgetValueForKey_(self, name):
    try:
        first = _first_python(self.__class__)
        if first is not None:
            return super(first, self).valueForKey_(name)
        else:
            return self.valueForKey_(name)

    except KeyError:
        raise AttributeError(name)


if os.uname()[2] < "13.":
    addConvenienceForClass(
        "NSManagedObject",
        (("__setattr__", NSMOsetValue_ForKey_), ("__getattr__", NSMOgetValueForKey_)),
    )
