def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    length = len(parens)
    
    left = '('
    l_count = 0
    right = ')'
    r_count = 0
    
    if parens[0] == right: return False
    for p in parens:
        if p == left:
            l_count += 1
        elif p == right:
            r_count += 1
            
    return True if l_count == r_count else False