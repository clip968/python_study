from Arraystack import *

def checkbracket(str):
    s = Arraystack(100)
    
    for c in str:
        if c == '[' or c == '(' or c == '{':
            s.push(c)
            
        elif c == ']' or c == ')' or c == '}':
            if s.isEmpty():
                return False
            
            else:
                left = s.pop()
                
                if(c == ']' and left != '[') or (c == ')' and left != '(') or (c == '}' and left != '{'):
                    return False
                
    return s.isEmpty()

if __name__ == '__main__':
    s1 = '{ A[(i+1)] = 0}'
    s2 = 'if((i == 0) && (j == 0)'
    s3 = 'A([i+1)] = 0'
    
    print(s1, '-->', checkbracket(s1))
    print(s2, '-->', checkbracket(s2))
    print(s3, '-->', checkbracket(s3))