import random

PRIME = 908209935089
P_A = 295087577400
P_B = 372093881987
M = 9931
RADIX = 256


def string2number(key: str) -> int:
    p = 0
    for i in key:
        p = (p * RADIX + ord(i)) % PRIME

    return p


def calculateFirstHash(key: int) -> int:
    return ((P_A * key) % PRIME + P_B) % M


def calculateSecondHash(key: int, a: int, b: int, m: int) -> int:
    return ((a * key) % PRIME + b) % m
