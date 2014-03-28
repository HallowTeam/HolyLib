from distutils.core import setup, Extension

setup(name = "crandom", version = "1.0",  ext_modules = [Extension('crandom', ['crandom.c'])])
