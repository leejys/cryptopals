import binascii
import base64

original = '1c0111001f010100061a024b53535009181c'
compare = '686974207468652062756c6c277320657965'
answer = '746865206b696420646f6e277420706c6179'
#originally in hex. won't be in hex once you xor it, so hex that
xored = hex(int(original, 16) ^ int(compare, 16))

print(xored[2:])
print(answer)
print(xored[2:] == answer)

#sanity check
print(len(original), len(str(xored)))
