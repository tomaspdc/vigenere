class Vigenere(object):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self):
        self.key = None

    def _find_pos(self, char):
        return self.alphabet.find(char)

    def _char_key_pos(self, char, pos):
        char_pos = self._find_pos(char)

        alphabet_char = self.key[pos % len(self.key)]
        key_pos = self._find_pos(alphabet_char)

        return char_pos, key_pos

    def _encode(self, char, pos):
        char_pos, key_pos = self._char_key_pos(char, pos)

        # alphabet pos = (char pos + key pos) mod 26
        mod = (char_pos + key_pos) % len(self.alphabet)

        return self.alphabet[mod]

    def _decode(self, char, pos):
        char_pos, key_pos = self._char_key_pos(char, pos)

        # char pos = (alphabet pos - key pos) mod 26
        mod = (char_pos - key_pos) % len(self.alphabet)

        return self.alphabet[mod]

    def set_key(self, key):
        self.key = key

    def set_alphabet(self, alphabet):
        self.alphabet = alphabet

    def encode(self, message):
        enc_chars = [
            self._encode(c, i) for c, i in zip(
                message, range(0, len(message))
            )
        ]

        return ''.join(enc_chars)

    def decode(self, message):
        dec_chars = [
            self._decode(c, i) for c, i in zip(
                message, range(0, len(message))
            )
        ]

        return ''.join(dec_chars)

v = Vigenere()
v.set_key('REDDIT')

msg = 'TODAYISMYBIRTHDAY'
msg_encoded = v.encode(msg)
msg_decoded = v.decode(msg_encoded)
# print('{} >> {} >> {}'.format(msg, msg_encoded, msg_decoded))

# now for the cracking part
encoded_msg = 'ZEJFOKHTMSRMELCPODWHCGAW'
vv = Vigenere()

# we know the key is composed of 5 letters or less, so we can bruteforce
import itertools
for i in range(0, 5):
    combos = itertools.combinations(Vigenere.alphabet, i+1)
    for c in combos:
        key = ''.join(c)
        vv.set_key(key)
        decoded = vv.decode(encoded_msg)
        # pipe this to brute.txt
        # then try to search for something meaninful
        print('{}, {}'.format(key, decoded))
