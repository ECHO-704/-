#!/usr/bin/env python3

import base64

_payload = bytes([27, 118, 26])
_key = 41

def _recover():
    raw = bytes(b ^ _key for b in _payload)
    return raw.decode()

def main():
    print("NOVA VAULT // ACCESS TERMINAL")
    print("-" * 32)
    print("Security verification required.")
    print()
    print("Find the integer x satisfying:")
    print("    3x ≡ 6 (mod 7)")
    print("where 1 <= x <= 6.")
    print()

    answer = input("Verification code: ").strip()

    if answer == "2":
        print("\nVerification accepted.")
        print("Recovered data:", _recover())
    else:
        print("\nVerification failed.")
        print("Access denied.")

if __name__ == "__main__":
    main()
