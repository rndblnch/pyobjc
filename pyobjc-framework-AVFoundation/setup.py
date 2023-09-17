"""
Wrappers for the "AVFoundation" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os

import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import Extension, setup  # noqa: E402

VERSION = "10.0"

setup(
    name="pyobjc-framework-AVFoundation",
    description="Wrappers for the framework AVFoundation on macOS",
    min_os_level="10.7",
    packages=["AVFoundation"],
    ext_modules=[
        Extension(
            "AVFoundation._inlines",
            ["Modules/_AVFoundation_inlines.m"],
            extra_link_args=["-framework", "AVFoundation"],
            py_limited_api=True,
        ),
        Extension(
            "AVFoundation._AVFoundation",
            ["Modules/_AVFoundation.m"],
            extra_link_args=["-framework", "AVFoundation"],
            py_limited_api=True,
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_AVFoundation")
            ],
        ),
    ],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-CoreMedia>=" + VERSION,
        "pyobjc-framework-CoreAudio>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
        "pyobjc-framework-Quartz>=" + VERSION,
    ],
    long_description=__doc__,
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
