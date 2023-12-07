"""
Wrappers for the "CoreML" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import Extension, setup  # noqa: E402

VERSION = "10.1"

setup(
    name="pyobjc-framework-CoreML",
    description="Wrappers for the framework CoreML on macOS",
    min_os_level="10.13",
    packages=["CoreML"],
    ext_modules=[
        Extension(
            "CoreML._CoreML",
            ["Modules/_CoreML.m"],
            extra_link_args=["-framework", "CoreML"],
            py_limited_api=True,
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_CoreML")
            ],
        )
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
