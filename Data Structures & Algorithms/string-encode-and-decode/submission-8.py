class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = "".join(word + "~" for word in strs)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = s.split("~")
        last = decoded_strs.pop()
        return decoded_strs
