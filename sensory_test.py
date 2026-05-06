"""

Module: SensoryListenerTesting
Author: Harshit Singh

__

General Function: 

- Tester file for SensoryListener Module
- Only source types tests for V1:

1. Text (SIZE: >= 1 and/or <= 1)
2. Invalid Inputs (None)
3. Floating Point numbers
4. Integers 
5. Structured Input (EDGE CASE) --> Main Function of Preprocessing (not allowed as input in this stage)
__ 

Note:

- Source types expand for later versions for further testing


"""

from sensory_listener import SensoryListener

test_cases = [
    # Valid
    "hello nova",
    "this is a test",

    # Warning
    "a",
    "",
    " ",
    "   ",

    # Invalid
    None,
    123,
    3.14,

    # Edge types
    [],
    {},
    ["text"],
    {"msg": "hi"},

    # Boundary
    "ab",
    " a ",
    "  hi  "
]

for case in test_cases:
    listener = SensoryListener(case)
    packet = listener._generate_packet()

    print("\n==============================")
    print("INPUT:", repr(case))
    print("OUTPUT:", packet)