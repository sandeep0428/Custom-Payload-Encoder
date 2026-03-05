from encoder import *
from obfuscator import *
from evasion_test import *

def menu():
    print("\n==== Custom Payload Encoder Framework ====")
    print("1. Base64 Encode")
    print("2. XOR Encode")
    print("3. ROT13 Encode")
    print("4. Random Obfuscation")
    print("5. Split & Concatenate")
    print("6. Escape Sequence")
    print("7. Run Detection Test")
    print("8. Exit")

def main():

    payload = input("\nEnter payload: ")

    while True:
        menu()

        choice = input("\nSelect option: ")

        if choice == "1":
            print("\nBase64 Encoded:\n", base64_encode(payload))

        elif choice == "2":
            key = int(input("Enter XOR key (number): "))
            print("\nXOR Encoded:\n", xor_encode(payload, key))

        elif choice == "3":
            print("\nROT13 Encoded:\n", rot13_encode(payload))

        elif choice == "4":
            print("\nRandom Obfuscated:\n", random_insertion(payload))

        elif choice == "5":
            print("\nSplit & Concat:\n", split_and_concat(payload))

        elif choice == "6":
            print("\nEscape Sequence:\n", escape_sequence(payload))

        elif choice == "7":
            print("\nDetection Result:", signature_detection(payload))

        elif choice == "8":
            print("Exiting...")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
