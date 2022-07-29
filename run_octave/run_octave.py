from scipy.io import loadmat, savemat
from os import path, system


class RunOctave:

    __version__ = "1.0.3"

    def __init__(self, octave_path):
        self.octave_path = octave_path.replace(" ","' '")
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"

        # Comma-separated letters
        self.CSL = ",".join(self.alphabet)

        # Getting PATH of temp files
        self.lib_path = path.split(path.abspath(__file__))[0].replace("\\","/")
        # print(self.lib_path)
        self.tempdata_path = self.lib_path + "/tempdata.mat"
        self.tempscript_path = self.lib_path + "/tempscript.m"

    def value_formatter(self, value):
        return value[0][0] if value.shape == (1, 1) else value

    def run(self, target, args=None, nargout=0):
        syntax = target
        data_send = {"None": []}

        # Verifying output arguments
        if nargout > 0:
            varargout = self.CSL[:nargout*2-1]
            syntax = "[" + varargout + "]=" + syntax

        # Verifying input arguments
        if isinstance(args, tuple):
            nargin = len(args)
            varargin  = self.CSL[:nargin*2-1]
            syntax += "(" + varargin + ");"
            data_send = dict(zip(self.alphabet[:nargin], args))
        elif all(c not in target for c in "[]=(,) '+-*/:"):
            syntax += "();"

        # Write in the communication channel
        savemat(self.tempdata_path, data_send)

        # Auxiliary script
        with open(self.tempscript_path, "w") as MAT_file:
            print("load('" + self.tempdata_path + "')", file=MAT_file)
            print(syntax, file=MAT_file)
            print("save('-mat-binary','" + self.tempdata_path + "')", file=MAT_file)

        # Executes the auxiliary script
        system(self.octave_path + " " + self.tempscript_path)

        # Read the communication channel
        data = loadmat(self.tempdata_path)

        # Output formatter
        if nargout == 1:
            return self.value_formatter(data["a"])
        return [self.value_formatter(data[key]) for key in self.alphabet[:nargout]]
