def brackets(n, lbrackets=0, rbrackets=0, brackets_string=""):
    if(lbrackets + rbrackets == 2*n):
        yield(brackets_string)
    if(lbrackets < n):
        yield from brackets(n, lbrackets + 1, rbrackets, brackets_string + '(')
    if lbrackets > rbrackets:
        yield from brackets(n, lbrackets, rbrackets + 1, brackets_string + ')')


if __name__ == '__main__':
    n = int(input())
    print(*brackets(n), sep='\n')
