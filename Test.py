from EvalPostFix import evalPostfix
from InfixToPostfix import infixToPostfix

infix = input('Input Infix Expr : ')
expr = infix.split()

print(expr, '=', evalPostfix(infixToPostfix(expr)))


