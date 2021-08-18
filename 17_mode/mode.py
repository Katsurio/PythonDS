def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    num_dict = {}
    
    for num in nums:
        if num_dict.get(num):
            num_dict[num] += 1
        else:
            num_dict[num] = 1
        
    # print(num_dict)
    
    max_val = max(num_dict)
    # print(max_val)
    mode = [k for k,v in num_dict.items() if v == max_val]
    print(mode[0])
    