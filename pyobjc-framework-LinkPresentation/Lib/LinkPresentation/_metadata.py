# This file is generated by objective.metadata
#
# Last update: Sat Jul  1 14:11:29 2023
#
# flake8: noqa

import objc, sys
from typing import NewType

if sys.maxsize > 2**32:

    def sel32or64(a, b):
        return b

else:

    def sel32or64(a, b):
        return a


if objc.arch == "arm64":

    def selAorI(a, b):
        return a

else:

    def selAorI(a, b):
        return b


misc = {}
constants = """$LPErrorDomain$"""
enums = """$LPErrorMetadataFetchCancelled@3$LPErrorMetadataFetchFailed@2$LPErrorMetadataFetchNotAllowed@5$LPErrorMetadataFetchTimedOut@4$LPErrorUnknown@1$"""
misc.update({"LPErrorCode": NewType("LPErrorCode", int)})
misc.update({})
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"LPMetadataProvider",
        b"setShouldFetchSubresources:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"LPMetadataProvider", b"shouldFetchSubresources", {"retval": {"type": b"Z"}})
    r(
        b"LPMetadataProvider",
        b"startFetchingMetadataForRequest:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"LPMetadataProvider",
        b"startFetchingMetadataForURL:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
