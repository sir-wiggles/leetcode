class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return ''.join(self.int_to_string(len(s)) + s for s in strs)

    def int_to_string(self, size):
        return ''.join([chr(size >> (i * 8) & 0xff) for i in range(4)][::-1])

    def string_to_int(self, string):
        result = 0
        for c in string:
            result = result * 256 + ord(c)
        return result

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        while i < len(s):
            length = self.string_to_int(s[i:i+4])
            i += 4
            res.append(s[i:i+length])
            i += length
        return res


t = Codec().encode(['foo', 'bar', 'baz', 'ninini'])
print(t)
t = Codec().decode(t)
print(t)

