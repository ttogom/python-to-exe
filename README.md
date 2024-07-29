
## Converting a Python Script to an Executable

This guide outlines the process of converting a simple Python script to C source code, PYD file, and ultimately into an executable.

### Prerequisites

Install the following modules:
- Cython
- Pyinstaller
- NumPy (as it's used in the script)

### The Script: hi.py

We'll be converting the following script:

```python
import numpy as np

def main():
    print("Hello World")
    print(np.array([1,2,3,]).shape)

if __name__ == '__main__':
    main()
```
### Step 1: Prepare Your Project Files

1.  Create a new project.
2.  Copy `hi.py` into this folder.
3.  Rename `hi.py` to `hi.pyx`.

### Step 2: Create setup.py
Run the following command: ```pip install cython```\
Create a file named `setup.py` in the same folder with the following content:
```python
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize

ext_modules = [
    Extension("hi", ["hi.pyx"]),
]

setup(name='Hi Cython App',
      cmdclass={'build_ext': build_ext},
      ext_modules=cythonize(ext_modules),
      compiler_directives={'language_level': 3},
      zip_safe=False
)
```

### Step 3: Compile to C and PYD
Open a command prompt in the folder and run:\
```python setup.py build_ext --inplace```\
This will generate C source code and a PYD file.

### Step 4: Create main.py
Create a file named `main.py` with the following content:
```python
import hi
hi.main()
```

### Step 5: Install Pyinstaller and Create Initial Spec File
Install pyinstaller\
```pip install pyinstaller```\
Run the following command:\
```pyinstaller main.py```

### Step 6: Modify the Spec File

Open the generated `main.spec` file and modify the `Analysis` function:

1.  Add your C and PYD files to the `datas` list:
```python
datas=[
    ("hi.c", "."),
    ("hi.cp39-win_amd64.pyd", "."),
],
```
2. Add your imported modules to `hiddenimports`:
```python
hiddenimports=['numpy'],
```

### Step 7: Create the Executable

Run the following command:\
```pyinstaller main.spec```
Navigate to the dist\main\ directory in your project folder. You'll find all the files for your app here, including the main executable (main.exe). Your application is now ready to run as a standalone executable!

