class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        val_map = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        for elem in s:
            if elem not in val_map:
                # 是左括号，入栈
                stack.append(elem)
            else:
                # 是右括号
                if len(stack) == 0:
                    # 栈是空的，不合法
                    return False
                else:
                    if not (val_map[elem] == stack.pop()):
                        # 栈顶不是和它匹配的又括号，不合法
                        return False
        if len(stack) == 0:
            return True
        else:
            return False
