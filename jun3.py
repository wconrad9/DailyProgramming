

def balancedParens(s) -> bool:

    braces = {'(': ')', '{': '}', '[':']'}

    stack = []

    for char in s:

        #if opening
        if char in braces.keys():
            stack.append(char)

        #if not an opening brace, it should close an existing brace or return False
        elif char in braces.values():

            if len(stack) == 0:
                return False

            currentBrace = stack.pop()

            if braces.get(currentBrace) == char:
                continue
            else:
                return False
    
    if len(stack) == 0:
        return True
    else:
        return False

def balancedParens2(s):

    stack = []

    open = ['(', '[', '{']
    closed = [')', ']', '}']

    for char in s:
        
        #has to start with open paren
        if char in open:
            stack.append(char)
        
        elif char in closed:
            if len(stack) == 0:
                return False
            
            else:

                if open.index(stack[len(stack) - 1]) == closed.index(char):
                    stack.pop()
                    continue
                else:
                    return False
    
    if len(stack) == 0:
        return True
    else:
        return False



print(balancedParens2('([])()[]()['))
