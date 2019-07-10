from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(['primes_cython.pyx',        # Cython code file with primes() function
                           'primes_cythonize.py'],  # Python code file with primes_python_compiled() function
                          annotate=True),        # enables generation of the html annotation file
)