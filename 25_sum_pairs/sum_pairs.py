def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    first_match = None
    second_match = None
    for num in nums:
        if second_match:
            break   
        for n in nums:    
            if num + n == goal:
                if second_match:
                    break
                if first_match == None:
                    first_match = (num, n) 
                elif (second_match == None and first_match[0] != num):
                    second_match = (num, n)
    
    if second_match != None:
        # print("IF second_match if hit")
        # return first_match if nums.index(first_match[0]) < nums.index(second_match[0]) and nums.index(first_match[1]) < nums.index(second_match[1]) else second_match
        return first_match if nums.index(first_match[1]) < nums.index(second_match[1]) else second_match
    elif first_match != None:
        # print("ELIF first _match if hit")
        return first_match
    else:
        # print("ELSE hit")
        return ()
# sum_pairs([5, 1, 4, 8, 3, 2], 7)