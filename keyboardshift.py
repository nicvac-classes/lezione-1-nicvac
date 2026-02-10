#!/usr/bin/env python3
# NOTE: it is recommended to use this even if you don't understand the following code.

import sys

sys.stdin = open('keybardshift_input2.txt')
sys.stdout = open('output.txt', 'w')

# input data
N = int(input().strip())
S = input().strip()

tastiFila1 = "qwertyuiop"
tastiFila2 = "asdfghjkl"
tastiFila3 = "zxcvbnm"

tastiera = {}
def aggiungi_tasti(tastiera, tastiFila):
    for i in range(0, len(tastiFila)-1):
        digitato = tastiFila[i]
        corretto = tastiFila[i+1]
        tastiera[digitato] = corretto

aggiungi_tasti(tastiera, tastiFila1)
aggiungi_tasti(tastiera, tastiFila2)
aggiungi_tasti(tastiera, tastiFila3)

stringa_corretta = ""
for i in range(0, len(S)):
    errato = S[i]
    corretto = tastiera[errato]
    stringa_corretta += corretto


print(stringa_corretta)  # print the result
