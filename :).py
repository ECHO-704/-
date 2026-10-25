#!/usr/bin/env python3

def recover():
    encoded = "22_27"
    return "".join(
        chr(ord(c) - 1) if c.isdigit() else c
        for c in encoded
    )

def main():
    print("NOVA VAULT // SECONDARY AUTHORIZATION")
    print("-" * 40)
    print("Solve for x:")
    print("    4x + 3 = 47")
    print()

    answer = input("Authorization code: ").strip()

    if answer == "11":
        print("\nAuthorization accepted.")
        print("Recovered data:", '!!_!^')
    else:
        print("\nAuthorization rejected.")

if __name__ == "__main__":
    main()
