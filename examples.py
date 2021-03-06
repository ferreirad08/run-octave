from run_octave import RunOctave
import numpy as np

# Create the Pyoctave object and explicitly add the path to octave-gui.exe
#octave = RunOctave(octave_path='C:/Program Files/GNU Octave/Octave-6.2.0/mingw64/bin/octave-gui.exe')
octave = RunOctave(octave_path='C:/Octave/Octave-5.2.0/mingw64/bin/octave-gui.exe')

A = np.array([[ 2, 0, 1],
              [-1, 1, 0],
              [-1, 1, 0],
              [-3, 3, 0]])

# Start Testing
sz = octave.run(nargout=1, target='size', args=(A,))
print(sz)

m, n = octave.run(nargout=2, target='size', args=(A,))
print(m, n)

m = octave.run(nargout=1, target='size', args=(A, 1))
print(m)

N = octave.run(nargout=1, target='vecnorm', args=(A, 2, 2))
print(N)

S = 'Hello World.'
octave.run(target='disp', args=(S,))

# Inserting expressions directly
X = octave.run(nargout=1, target='ones(4, 3) * 255;')
print(X)

octave.run("S = 'Hello World.'; disp(S)")

octave.run('''
A = [1 2; 3 4]
size(A)
B = A + 2
''')

octave.run(target='ones(4, 3) * 255')  # Expression without semicolon
