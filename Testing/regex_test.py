"""Testing regex expressions"""

import re

TEST_STRING = "Khent Alba"

if not re.match(r"[a-zA-Z]+", TEST_STRING):
    print("match")
else:
    print("not match")
