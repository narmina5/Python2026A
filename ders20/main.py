# kitabxanasiz
"""
print()
input()

int()
float()
str()
bool()
list()
set()
frozenset()
dict()
tuple()

len()
sum()
min()
max()
abs()

any()
all()
hasattr()
isinstance()
id()
"""


"""
import os
import sys
import math
import datetime
import flask
import django
import pandas
"""
import os
import sys
import math
import pandas as pd
import numpy as np

from datetime import datetime

start = datetime.now()
print(math.factorial(5))
print(math.pi)
print(math.exp(5))
print(math.ceil(5.1))
print(math.e)


print(datetime.now() - start)

"""
Package:
install - pip install <pkg>
    specific version
uninstall - pip uninstall <pkg>
upgrade - pip install --upgrade <pkg>
show - pip show <pkg>
"""



"""
PYTHON


Proyekt A (Youtubea video yukleyen)  - numpy 1.0.0  pandas 1.5.2 youtube 5.0.2      PythonVenv1
Proyekt B  - numpy 5.0.0  tiktok 5.2.0 open-xlsx 2.0                                PythonVenv2
Proyekt C  - numpy 3.0.0  open-gpt 3.0.0                                            PythonVenv3
"""


"""
Virtual Environments

activate - deactivate

Win:
.venv\Scripts\activate          - aktivleshdirmek
deactivate                     - deaktivleshdirmek

Unix (Linux, MacOS):
source .venv/bin/activate
deactivate
"""

"""
requirements.txt
"""



"""
Other:

pip list
pip freeze
pip --help
pip --version
"""

"""
pip freeze > requirements.txt
"""

"""
pip list --outdated
"""

"""
Maraqli kitabxanalar
"""

"""
pip install pyfiglet
"""

import pyfiglet
import math
ascii_art = pyfiglet.figlet_format("Salam Xosh Geldiniz")
print(ascii_art)


"""
pip install randfacts
"""

import randfacts
print(randfacts.get_fact())


"""
pip install faker
"""

from faker import Faker
fake = Faker()
print(fake.name())
print(fake.email())


"""
import
as
*
from
venv
requirements.txt
"""
import math
from math import pi, sin, cos
import pandas as pd


from math import factorial

"""
match case
"""