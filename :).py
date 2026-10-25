#!/usr/bin/env python3

import hashlib
import base64

def unlock(value):
    return hashlib.sha256(value.encode()).hexdigest() == (
        "ef797c8118f02dfb649607dd5d3f8c7623048c9c"
        "f9c9c7e8f7b6b6a5c5a5c5a5"
    )

def main():
    print("NOVA VAULT // SESSION VALIDATION")
    print("-" * 36)
    print("A new verification is required.")
    print()
    print("What is the decimal value of binary 1000?")
    answer = input("Response: ").strip()

    if answer == "8":
        fragment = base64.b64decode("OF83").decode()
        print("\nSession accepted.")
        print("Recovered data:", fragment)
    else:
        print("\nSession rejected.")

if __name__ == "__main__":
    main()
