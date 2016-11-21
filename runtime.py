def string_compare(s1, s2):
    """Given two strings, figure out if they are exactly the same (without using ==).

    Put runtime here:
    -----------------
    Runtime O(n)


    """
    # The expression below is O(1) and therefore does not add to runtime.
    if len(s1) != len(s2):
        return False

    # Runtime of this step would be O(n) because this loop is iterating over the
    # number of total items in the string.
    for i in range(len(s1)):
        # This expression also does not contribute to the runtime.
        if s1[i] != s2[i]:
            return False

    return True


def has_exotic_animals(animals):
    """Determine whether a list of animals contains exotic animals.

    Put runtime here:
    -----------------
    Runtime of O(n)

    """
    # This is a hidden loop, where the string "hippo" or "platypus" would need
    # to be compared to each element in animals. And worse case scenario
    # both would need to be compared to all other items in animals, but could
    # be carried out one after another, not nested. Therefore 2*O(n) --> O(n).
    if "hippo" in animals or "platpypus" in animals:
        return True
    else:
        return False


def sum_zero_1(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    Runtime would be O(n2)

    """

    result = []

    # Hint: the following line, "s = set(numbers)", is O(n) ---
    # we'll learn exactly why later
    s = set(numbers)

    # iterating through each item in the set is O(n)
    for x in s:
        # This is a hidden loop, but is still looking at each element in a list
        # and therefore has runtime O(n).
        if -x in s:
            # Appending an item is O(1)
            result.append([-x, x])

    return result
    # The final runtime would be O(n) for the first step followed by O(n2) for
    # the for loop. The O(n2) time would be the limiting factor and therefore
    # the runtime of this function would be O(n2).

def sum_zero_2(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    Runtime is O(n2)

    """

    result = []

    # Iterating through all numbers in a list is O(n) runtime
    for x in numbers:
        # A nested interation through the loop again would be O(n)
        for y in numbers:
            # This expression does not contribute to the runtime.
            if x == -y:
                # Appending is constant O(1) runtime
                result.append((x, y))
    return result
    # The final runtime would be O(n) * O(n) --> O(n2)


def sum_zero_3(numbers):
    """Find pairs of integers that sum to zero.

    This version gets rid of duplicates (it won't add (1, -1) if (-1, 1) already there.

    Put runtime here:
    -----------------
    Runtime is O(n3)

    """

    result = []

    # Iterating through all numbers in a list is O(n) runtime
    for x in numbers:
        # A nested interation through the loop again would be O(n)
        for y in numbers:
            # The first half of the expression for evaluation, if x == -y would
            # not add to the runtime, but the second half, checking if a value is
            # in result requires iterating thru. It would add O(n) to the runtime.
            if x == -y and (y, x) not in result:
                result.append((x, y))
    return result
    #The final runtime of this one has three nested loops, O(n) * O(n) * O(n) --> O(n3)
