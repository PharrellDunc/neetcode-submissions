class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:
            if char in pairs:
                if not stack:
                    return False

                if stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)

        return not stack