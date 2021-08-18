def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    n1 = sorted(f"{num1}")
    n2 = sorted(f"{num2}")
    
    return True if n1 == n2 else False