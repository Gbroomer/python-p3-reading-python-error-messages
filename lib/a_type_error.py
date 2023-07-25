#!/usr/bin/env python3
number = 321


try: 
    wrong_type = f"{number}" + 123
except TypeError:
    wrong_type = 321 + 123
