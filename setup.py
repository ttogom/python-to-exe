from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize

ext_modules = [
    Extension("hi", ["hi.pyx"])
]
setup(name='Cython test',
      cmdclass={'build_ext': build_ext},
      ext_modules=cythonize(ext_modules),
      compiler_directives={'language_level': 3},
      zip_safe=False
)
