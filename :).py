#!/usr/bin/env python3

def recover():
    encoded = "31395F3133"
    return bytes.fromhex(encoded).decode()

def main():
    print("NOVA VAULT // FINAL NODE")
    print("-" * 30)
    print("Solve the sequence:")
    print("    3, 7, 11, 15, ?")
    print()

    answer = input("Node verification: ").strip()

    if answer == "19":
        print("\nNode verified.")
        print("Recovered data:", recover())
    else:
        print("\nVerification failed.")

if __name__ == "__main__":
    main()
