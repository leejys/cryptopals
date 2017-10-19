#Set 1.3, single byte XOR cipher
import binascii

#ASCII range: 65-90 A-Z, 97 - 122 a-z

#freqanalysis 
freq_chars = {'A':0.082, 'B':0.015, 'C':0.028, 'D':0.043, 'E':0.127, 'F':0.022, 'G': 0.02, 'H':0.061, 'I':0.07, 'J':0.002, 'K':0.008, 'L':0.04, 'M':0.024, 'N':0.067, 'O':0.075, 'P':0.019, 'Q':0.001, 'R':0.06, 'S':0.063, 'T':0.091, 'U':0.028, 'V':0.01, 'W':0.024, 'X':0.002, 'Y':0.02, 'Z':0.001}


encrypted = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

test_char = '122'

xored = (hex(int(encrypted, 16) ^ int(test_char, 16)))
print(type(xored))
#to only get the relevant part
print(xored)

#sanity check
print("length check", len(encrypted), len(str(xored)))

decoded = binascii.b2a_hex(xored)

print(decoded)
