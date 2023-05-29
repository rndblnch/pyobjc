"""
Wrappers for the "MetalPerformanceShadersGraph" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import setup  # noqa: E402

VERSION = "9.2"

setup(
    name="pyobjc-framework-MetalPerformanceShadersGraph",
    description="Wrappers for the framework MetalPerformanceShadersGraph on macOS",
    min_os_level="10.16",
    packages=["MetalPerformanceShadersGraph"],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-MetalPerformanceShaders>=" + VERSION,
    ],
    long_description=__doc__,
)
