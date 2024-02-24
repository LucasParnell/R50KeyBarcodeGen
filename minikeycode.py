# Made by Lucas Parnell 02/04/2024
import sys


def generate_codes(args):
    ini_code = ""
    reg_code = "G"
    if(len(args[1])==6):
        ini_code = str(args[1].upper())
        if len(args) == 3:
            match args[2].upper():
                case 'EUR':
                    reg_code = "G"
                    pass
                case 'NA':
                    reg_code = "J"
                    pass
                case 'SA':
                    reg_code = "H"
    else:
        print(f"Correct format: {args[0]} InitialCode" + " {Region} (default EUR)")
        print("Initial code length is 6 digits")
        print("Supported regions are 'EUR', 'NA' and 'SA' (Europe, North America, South Africa)")
        quit()

    ini_code_m1 = str(hex(int(ini_code,16) - 1))[2:].upper()

    barcode_1 = reg_code + str(ini_code) + ini_code_m1 + "FF0"


    # Security code is 15 bytes long, last digit is $
    security_code = "FFFFFFFFFF"

    # Cipher XOR PAD 0xFFFFFF
    xorpad = [int(c, 16) for c in "FFFFFFF"]

    for i in range(1, len(xorpad)):
        xor_char = int(barcode_1[i], 16) ^ xorpad[i]
        security_code += hex(xor_char)[2:].upper()

    print()
    print(f"Barcode 1: *{barcode_1}*")
    print(f"Barcode 2: *{security_code[2:]}$*")
    print()
    print("--CODES FOR KEY PROGRAMMING--")
    print()
    print(f"Initial Code: {ini_code}")
    print(f"Mod Initial Code: {ini_code_m1}")
    print(f"Security Code: {security_code}")


if __name__ == "__main__":
    generate_codes(sys.argv)
