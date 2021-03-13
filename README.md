# Pyoctave

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/ferreirad08/pyoctave/blob/main/LICENSE)
[![Linkedin](https://img.shields.io/badge/LinkedIn-%230077B5.svg?&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/david-f-3a918ba5)

Run Octave functions and scripts in the Python interpreter

Requirements

    Install Octave in advance (https://www.gnu.org/software/octave/index)

Examples
        
    from pyoctave import Pyoctave
    import numpy as np

    # Create the Pyoctave object and explicitly add the path to octave-gui.exe
    octave = Pyoctave(octave_path='C:/Octave/Octave-5.2.0/mingw64/bin/octave-gui.exe')

    A = np.array([[ 2, 0, 1],
                  [-1, 1, 0],
                  [-1, 1, 0],
                  [-3, 3, 0]])

    # Start Testing
    m, n = octave.run(nargout=2, target='size', args=(A,))
    print(m, n)

    # Inserting expressions directly
    X = octave.run(nargout=1, target='ones(4, 3) * 255;')
    print(X)
