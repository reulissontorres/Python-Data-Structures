from stackLL import Stack


def check_expression(exp):
    """
    Verifica se os delimitadores de uma expressão matemática estão corretamente dispostos

    Args:
        exp (str): expressão matemática

    Returns:
        bool: é uma expressão matemátiva válida
    """
    s = Stack()
    fullEmp = Stack()
    for char in exp:
        fullEmp.push(char)

        if char in '([{':
            s.push(char)
        elif char == ')':
            if s.peek() == '(':
                s.pop()
            else:
                return False
        elif char == ']':
            if s.peek() == '[':
                s.pop()
            else:
                return False
        elif char == '}':
            if s.peek() == '{':
                s.pop()
            else:
                return False
        elif char in '+-*/':
            top = fullEmp.pop()
            if fullEmp.peek() in '([{+-*/':
                return False
            fullEmp.push(top)
    
    if not s.is_empty(): 
        return False
    
    return True

def infix_to_posfix(exp):
    """Converte uma expressão matemática infixa para posfixa

    Args:
        exp (str): expressão matemática infixa

    Returns:
        str: expressão posfixa
    """
    stack = Stack()
    posfix = ''
    for char in exp:
        if char not in '()+*-/':
            posfix += char
        
        if char in '+-*/':
            if char in '+-' and stack.peek() in '+-*/':
                posfix += stack.pop()
                stack.push(char)
            else:
                stack.push(char)
              
        if char == '(':
            stack.push(char)

        if char == ')':
            while stack.peek() != '(':
                posfix += stack.pop()
            stack.pop()

    while not stack.isEmpty():
        posfix += stack.pop()
    return posfix
