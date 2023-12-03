def is_balanced(expression):
    stack = []
   
    bracket_mapping = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in bracket_mapping.values():
            
            stack.append(char)
        elif char in bracket_mapping.keys():
       
            if not stack or stack.pop() != bracket_mapping[char]:
                return False
        else:
           
          return not stack


expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  
print(is_balanced(expression2))  
