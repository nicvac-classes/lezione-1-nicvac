#!/usr/bin/env python3
# NOTE: it is recommended to use this even if you don't understand the following code.

import sys

sys.stdin = open('keybardshift_input2.txt')
sys.stdout = open('output.txt', 'w')

# input data
N = int(input().strip())
S = input().strip()

tastiera = {
    "q": "w",
    "w": "e",
    "e": "r",
    "a": "s",
    "b": "n"
    # ...
}

stringa_corretta = ""
for i in range(0, len(S)):
    errato = S[i]
    corretto = tastiera[errato]
    stringa_corretta += corretto


print(stringa_corretta)  # print the result
