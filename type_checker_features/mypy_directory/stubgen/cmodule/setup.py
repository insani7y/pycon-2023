from distutils.core import Extension, setup

module1 = Extension("multiply_module", sources=["multiply_module.c"])

setup(name="MultiplyPackage", version="1.0", description="This is a package for multiplication", ext_modules=[module1])
