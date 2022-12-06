import requests as req
import inspect
from os import path
from typing import List

class get_input():
    """ 
        Purpose: encapsulate all AoC input logic 
    """
    def __init__(self, trim:bool):

        # Wanted to dedicate a function to get the caller file's name, but calling that function from here would change the stack.
        caller = path.split(inspect.stack()[1].filename) 
        self.dirname = caller[0]
        self.filename = caller[1]
        self.input_file = self._input_file()
        self.raw_text = self._raw_text(trim)
    
    def _input_file(self):
        return self.dirname + '\\input\\' + self.filename.split('.')[0] + '.txt'

    def _raw_text(self, trim)->List[str]:
        with open(self.input_file, 'r') as f:
            if trim:
                inp = [str(line).strip() for line in f]
            else:
                inp = [str(line).strip('\n') for line in f]
        return inp