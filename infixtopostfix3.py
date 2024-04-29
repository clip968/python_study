from Arraystack import *

def precedence(e):
    if (e == '(' or e == ')'): return 0
    elif (e == '+' or e == '-'): return 1
    elif (e == '*' or e == '/'): return 2
    
def infixtopostfix(expr):
    s = Arraystack(100)
    postfix = []
    
    for temp in expr:
        if temp in '(':
            s.push('(')
        elif temp in ')':
            while not s.isEmpty():
                e = s.pop() 
                if e == '(':
                    break
                else:
                    postfix.append(e)
        elif temp in '+-/*':
            while not s.isEmpty():
                e = s.peek()
                if (precedence(e) >= precedence(temp)):
                    postfix.append(e)
                    s.pop()
                else:
                    break
                
            s.push(temp)
            
        else:
            postfix.append(temp)
            
    while not s.isEmpty():
        postfix.append(s.pop())
        
    return postfix

if __name__ =='__main__':
    infix = input('Input Infix Expr : ')
    expr = infix.split()
    postfix = infixtopostfix(expr)
    
    print(postfix)