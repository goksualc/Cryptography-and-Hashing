class SimpleHash:
    def __init__(self):
        # Initial state (arbitrary values)
        self.h0 = 0x6a09e667
        self.h1 = 0xbb67ae85
        self.h2 = 0x3c6ef372
        self.h3 = 0xa54ff53a
        self.h4 = 0x510e527f
        self.h5 = 0x9b05688c
        self.h6 = 0x1f83d9ab
        self.h7 = 0x5be0cd19

    def _rotr(self, n, x):
        return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF

    def _ch(self, x, y, z):
        return (x & y) ^ (~x & z)

    def _maj(self, x, y, z):
        return (x & y) ^ (x & z) ^ (y & z)

    def _sigma0(self, x):
        return self._rotr(2, x) ^ self._rotr(13, x) ^ self._rotr(22, x)

    def _sigma1(self, x):
        return self._rotr(6, x) ^ self._rotr(11, x) ^ self._rotr(25, x)

    def _choose(self, x, y, z):
        return (x & y) ^ (~x & z)

    def _sha256_round(self, a, b, c, d, e, f, g, h, w, k):
        t1 = h + self._sigma1(e) + self._ch(e, f, g) + k + w
        t2 = self._sigma0(a) + self._maj(a, b, c)
        return (h + t1) & 0xFFFFFFFF, (t1 + t2) & 0xFFFFFFFF

    def hash(self, message):
        # Padding the message
        message = bytearray(message, 'utf-8')
        length = len(message) * 8
        message.append(0x80)
        while len(message) % 64 != 56:
            message.append(0x00)
        message += length.to_bytes(8, byteorder='big')

        # Process each block
        for i in range(0, len(message), 64):
            block = message[i:i+64]
            words = [int.from_bytes(block[j:j+4], byteorder='big') for j in range(0, 64, 4)]

            a, b, c, d, e, f, g, h = self.h0, self.h1, self.h2, self.h3, self.h4, self.h5, self.h6, self.h7

            for t in range(64):
                if t >= 16:
                    words.append((self._sigma1(words[t-2]) + words[t-7] + self._sigma0(words[t-15]) + words[t-16]) & 0xFFFFFFFF)

                a, h = self._sha256_round(a, b, c, d, e, f, g, h, words[t], k=t)

            self.h0 = (self.h0 + a) & 0xFFFFFFFF
            self.h1 = (self.h1 + b) & 0xFFFFFFFF
            self.h2 = (self.h2 + c) & 0xFFFFFFFF
            self.h3 = (self.h3 + d) & 0xFFFFFFFF
            self.h4 = (self.h4 + e) & 0xFFFFFFFF
            self.h5 = (self.h5 + f) & 0xFFFFFFFF
            self.h6 = (self.h6 + g) & 0xFFFFFFFF
            self.h7 = (self.h7 + h) & 0xFFFFFFFF

        # Return the hash value as a hex string
        return f"{self.h0:08x}{self.h1:08x}{self.h2:08x}{self.h3:08x}{self.h4:08x}{self.h5:08x}{self.h6:08x}{self.h7:08x}"

# Example usage:
my_hash_object = SimpleHash()
hashed_value = my_hash_object.hash("Hello, World!")
print("Hashed Value:", hashed_value)
