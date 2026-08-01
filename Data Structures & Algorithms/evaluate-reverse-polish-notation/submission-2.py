class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:

            
            if token != "+" and token != "-" and token != "*" and token != "/":
                stack.append(int(token))

            else:
                # Pop operands
                right = stack.pop()
                left = stack.pop()

                # Perform operation
                if token == "+":
                    result = left + right
                elif token == "-":
                    result = left - right
                elif token == "*":
                    result = left * right
                else:
                    result = int(left / right)

                # Push result back
                stack.append(result)

        return stack.pop()