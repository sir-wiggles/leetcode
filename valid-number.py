import unittest

from collections import defaultdict

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #define DFA state transition tables
        states = [{},
                 # State (1) - initial state (scan ahead thru blanks)
                 {'blank': 1, 'sign': 2, 'digit':3, '.':4},

                 # State (2) - found sign (expect digit/dot)
                 {'digit':3, '.':4},

                 # State (3) - digit consumer (loop until non-digit)
                 {'digit':3, '.':5, 'e':6, 'blank':9},

                 # State (4) - found dot (only a digit is valid)
                 {'digit':5},

                 # State (5) - after dot (expect digits, e, or end of valid input)
                 {'digit':5, 'e':6, 'blank':9},

                 # State (6) - found 'e' (only a sign or digit valid)
                 {'sign':7, 'digit':8},
                 
                 # State (7) - sign after 'e' (only digit)
                 {'digit':8},

                 # State (8) - digit after 'e' (expect digits or end of valid input) 
                 {'digit':8, 'blank':9},

                 # State (9) - Terminal state (fail if non-blank found)
                 {'blank':9}]

        currentState = 1
        digits = set('0123456789')
        blanks = set(' \t\n')
        signs  = set('+-')
        for c in s:
            # If char c is of a known class set it to the class name
            if c in digits:
                c = 'digit'
            elif c in blanks:
                c = 'blank'
            elif c in signs:
                c = 'sign'
            # If char/class is not in our state transition table it is invalid input
            if c not in states[currentState]:
                return False
            # State transition
            currentState = states[currentState][c]
        # The only valid terminal states are end on digit, after dot, digit after e, or white space after valid input    
        if currentState not in [3,5,8,9]:
            return False
        return True




class Test(unittest.TestCase):

    def test(self):

        cases  = [
            ["-.", False],
            ["-1e-.", False],
            ["+.", False],
            ["0" , True],
            ["39E" , False],
            ["4e+" , False],
            ["+e1" , False],
            [".e1" , False],
            ["6+1" , False],
            ["1e." , False],
            ["1e6+1" , False],
            [".e." , False],
            ["." , False],
            ["1." , True],
            [".1" , True],
            [" 0.1 " , True],
            [" 0.1.2 " , False],
            ["abc" , False],
            ["1 a" , False],
            ["2e10" , True],
            [" -90e3   " , True],
            [" -90ee3   " , False],
            [" -90ee3e1   " , False],
            [" 1e" , False],
            ["e3" , False],
            [" 6e-1" , True],
            [" 99e2.5 " , False],
            ["53.5e93" , True],
            ["-53.5e93" , True],
            [" --6 " , False],
            ["-+3" , False],
            ["95a54e53" , False],
            ["+0e-" , False],
            ["+0e-1" , True],
            ["+0e" , False],
            ["0e" , False],
        ]
        for case, res in cases:
            self.assertEqual(Solution().isNumber(case), res, case)

unittest.main(exit=False)
