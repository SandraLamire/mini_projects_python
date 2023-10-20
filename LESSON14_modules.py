import math
import sys
import random
from enum import Enum
import LESSON14_kansas
# Call rps without LESSON14_rps_v7.rock_paper_scissors() notation, 
# just call it with rock_paper_scissors() 
from LESSON14_rps_v7 import rock_paper_scissors


print(math.pi)
# 3.141592653589793
# OR just import pi :
# from math import pi
# print(pi)


random.choice("123")
# OR create an alias
import random as rdm
print(rdm.choice("123"))
# 1 or 2 or 3


# List of methods
print(dir(rdm))
# ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', 
# '_ONE', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', 
# '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', 
# '_cos', '_e', '_exp', '_floor', '_index', '_inst', '_isfinite', '_log', '_os', '_pi', '_random', 
# '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator',  '_urandom', '_warn', 'betavariate',
# 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss',  'getrandbits', 'getstate', 
# 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint',  'random', 'randrange', 
# 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']

# OR
for item in dir(rdm):
    print(item)
# print each item in the previous list in a single line

print(LESSON14_kansas.capital)
# Topeka
LESSON14_kansas.randomfunfact()
# A considerable portion of Kansas City is actually in Missouri.

# LESSON14_kansas() print
# TypeError: 'module' object is not callable
# because of if __name__ == "__main__": randomfunfact() in LESSON14_kansas.py is false

print(__name__)
# __main__ = name of module used when we launch this code

print(LESSON14_kansas.__name__)
# LESSON14_kansas

# Launch the game rock_paper_scissors thanks to import the module
rock_paper_scissors()
