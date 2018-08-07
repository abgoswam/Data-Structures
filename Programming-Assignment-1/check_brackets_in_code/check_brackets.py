# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    indices = []

    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            indices.append(i)

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                print(i+1)
                exit()

            last_item = opening_brackets_stack[-1]

            if (last_item == '(' and next == ')') or \
                (last_item == '[' and next == ']') or \
                (last_item == '{' and next == '}'):
                del opening_brackets_stack[-1]
                del indices[-1]
            else:
                print(i+1)
                exit()

    if len(opening_brackets_stack) == 0:
        print("Success")
    else:
        print(indices[-1] + 1)

    # Printing answer, write your code here
