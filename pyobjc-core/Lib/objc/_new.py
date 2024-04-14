"""
Implementation of `__new__` for arbitrary Cocoa classes
"""

# TODO:
# - Document-
# - Maybe: somehow add __doc__ to classes that reflect the
#   __new__ API.
# - Determine how to interact with the new classes
#   that already have an __new__
# - Update _transform to add entries to NEW_MAP
#   (baesd on init methods)
# - Update support code for framework bindings
# - Update framework binding tooling (and then the
#   bindings themselves)
# - Add tests

__all__ = ()

NEW_MAP = {}
UNSET = object()


class _function:
    """
    Wrapper for the __new__ function to generate the
    docstring dynamically.
    """

    __slots__ = ("_function", "_cls")

    def __init__(self, function, cls):
        self._function = function
        self._cls = cls

    @property
    def __class__(self):
        return self._function.__class__

    @property
    def __doc__(self):
        result = {}
        for c in reversed(self._cls.__mro__):
            new_map = NEW_MAP.get(c, UNSET)
            if new_map is UNSET:
                continue

            for kwds, selector in new_map.items():
                if selector is None:
                    result.pop(kwds, None)

                if not kwds:
                    result[kwds] = f"{self._cls.__name__}(): "
                else:
                    result[kwds] = f"{self._cls.__name__}(*, " + ", ".join(kwds) + "): "
                if selector.startswith("init"):
                    result[kwds] += f"   returns 'cls.alloc().{selector}()'\n\n"
                else:
                    result[kwds] += f"   returns 'cls.{selector}()'\n\n"
        return "".join(sorted(result.values()))[:-1]

    def __getattr__(self, name):
        return getattr(self._function, name)

    def __setattr__(self, name, value):
        if name in ("_function", "_cls"):
            object.__setattr__(self, name, value)
        return setattr(self._function, name, value)


def _make_new(cls):
    def __new__(cls, **kwds):
        """
        Generic implementation for Objective-C `__new__`.
        """
        # XXX: should this sort the keywords?
        key = tuple(kwds.keys())

        for c in cls.__mro__:
            new_map = NEW_MAP.get(c, UNSET)
            if new_map is UNSET:
                continue

            name = new_map.get(key, UNSET)
            if name is UNSET:
                continue

            if name is None:
                if key:
                    raise TypeError(
                        f"{cls.__name__}() does not support keyword arguments {', '.join(repr(k) for k in key)}"
                    )
                else:
                    raise TypeError(f"{cls.__name__}() requires keyword arguments")

            if name.startswith("init") and len(name) == 4 or name[4].isupper():
                return getattr(cls.alloc(), name)(**kwds)

            else:
                return getattr(cls, name)(**kwds)

        if key:
            raise TypeError(
                f"{cls.__name__}() does not support keyword arguments {', '.join(repr(k) for k in key)}"
            )
        else:
            raise TypeError(f"{cls.__name__}() requires keyword arguments")

    # XXX: Settings these helps, but does not yet result in the correct
    #      output from help()
    __new__.__name__ = cls.__name__ + ".__new__"
    __new__.__qualname__ = cls.__name__ + ".__new__"
    __new__.__module__ = cls.__module__
    return _function(__new__, cls)
