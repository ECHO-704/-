#!/usr/bin/env python3

def decode():
    data = [ord(c) ^ 19 for c in "26L20"]
    return "".join(chr(n) for n in data)

def main():
    print("NOVA VAULT // INTEGRITY CHECK")
    print("-" * 34)
    print("Calculate the result:")
    print("    (5 * 4) - 3")
    print()

    answer = input("Integrity code: ").strip()

    if answer == "17":
        print("\nIntegrity verified.")
        print("Recovered data:", '17_23')
    else:
        print("\nIntegrity check failed.")

if __name__ == "__main__":
    main()
