#Set 1.1
#hex -> binary, binary -> base64

import binascii
import base64

original = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

binary = binascii.unhexlify(original)
b64 = base64.b64encode(binary)

#print(b64)
#need to do this to get rid of the b''
print(b64.decode('utf-8'))
