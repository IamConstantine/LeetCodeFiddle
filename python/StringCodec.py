# https://leetcode.com/problems/encode-and-decode-strings
# Medium
# T = O(N) - no of strs in array
# S = O(1) - excluding output array

class StringCodec:

    def len_to_str(self, length):
        """encodes the length to 4 byte string
        """

        bytes = [chr(length >> (i * 8) & 0xff) for i in range(4)]
        bytes.reverse()
        return ''.join(bytes)

    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return ''.join(self.len_to_str(len(s)) + s for s in strs)

    def str_to_len(self, bytes_str):
        """decodes the length of string from bytes_str
        """
        result = 0
        for i in range(4):
            result = result * 256 + ord(bytes_str[i])  # 256 - as its a 1 byte encoded string
        return result

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        i, n = 0, len(s)
        output = []
        while i < n:
            length = self.str_to_len(s[i:i + 4])
            i += 4
            output.append(s[i:i + length])
            i += length
        return output
