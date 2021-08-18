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
    already_visited = set()

    for i in nums:
        difference = goal - i

        if difference in already_visited:
            return (difference, i)

        already_visited.add(i)

    return ()



    # already_visited = set()
    # print(f"25:already_visited ---> {already_visited}")
    # for i in nums:
    #     print(f"27:i ---> {i}")
    #     print(f"28:goal ---> {goal}")
    #     difference = goal - i
    #     print(f"31:differnece ---> {difference}")
    #     if difference in already_visited:
    #         print(f"32:differnece ---> {difference}")
    #         print(f"33:already_visited ---> {already_visited}")
    #         return (difference, i)

    #     already_visited.add(i)
    #     print(f"37:already_visited ---> {already_visited}")
    # return ()




# I would like to discuss  this 
