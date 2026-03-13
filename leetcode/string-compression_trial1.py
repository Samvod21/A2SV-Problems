class Solution(object):
    def compress(self, chars):
        read = 0
        written = 0

        while read < len(chars):
            char = chars[read]
            c = 0

            while read < len(chars) and chars[read] == char:
                read += 1
                c += 1
            
            chars[written] = char
            written += 1

            if c > 1:
                for dig in str(c):
                    chars[written] = dig
                    written += 1
        return written
        