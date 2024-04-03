from Arraystack import Arraystack

def precedence(op):
    if(op == '(' or op == ')'): return 0
    elif(op == '+' or op == '-'): return 1
    elif(op == '*' or op == '/'): return 2
    
    else:
        return -1

def infixToPostfix(expr):
    s = Arraystack(100)
    postfix = []
    
    for term in expr:
        if term in '(':
            s.push('(')
        elif term in ')':
            while not s.isEmpty():
                op = s.pop()
                if op == '(':
                    break
                else:
                    postfix.append(op)
        elif term in '+-*/':
            while not s.isEmpty():
                op = s.peek()
                if(precedence(term) <= precedence(op)):
                    postfix.append(op)
                    s.pop()
                else: break
                
            s.push(term)
        else:
            postfix.append(term)
            
    while not s.isEmpty():
        postfix.append(s.pop())
        
    return postfix

if __name__ =='__main__':
    infix = input('Input Infix Expr : ')
    expr = infix.split()
    postfix = infixToPostfix(expr)
    
    print(postfix)