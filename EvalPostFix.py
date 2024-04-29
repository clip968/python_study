from Arraystack import Arraystack

def evalPostfix(expr):
    S  = Arraystack(100)
    
    for token in expr:
        if token in '+-*/':
            val2 = S.pop()
            val1 = S.pop()
            if token == '+': S.push(val1 + val2)
            elif token == '-': S.push(val1 - val2)
            elif token == '*': S.push(val1 * val2)
            elif token == '/': S.push(val1 / val2)
            
        else:
            S.push(float(token))
                
    return S.pop()

if __name__ == '__main__':
    str = '8 2 3 / - 3 2 * +'
    expr = str.split()  
    
    print(expr, '-->', evalPostfix(expr)) 