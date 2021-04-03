n, B = list(map(int, input().strip().split()))
T = 0


# your code here
def sequence_generator(n):
    '''

    Creates the sequence according to the instructions.
    First I create an empty list (a.k.a. the sequence) (line 14)
    Second, I generate the elements of the sequence and append them to the list. (line 15-19)
    Then I return the sequence so the other method can use it. (line 20)
    '''
    seq = []
    for i in range(1, n + 1): # I start at 1 as instructed.
        if i % 2 == 0:
            seq.append((2**i) + 1) # (2^i + 1 for even numbers)
        else:
            seq.append((3**i) + 1) # (3^i + 1 for odd numbers)
    return seq


def brute_force(n, B, total=0):
    """

    First I call sequence_generator to form the sequence using the given input. (line 36)
    I also initialize a total variable which is 0 at start. (line 23)
    The first for loop makes sure t is incremented within the proper range. (line 37)
    The while loop is there so when I use break, I return to the first for loop (line 38)
    The second for loop increments total by adding the terms of the equation formed by the sequence and t. (line 39-45)
    If total < b when its over, i reset total to 0 to try the next t. (line 42)
    Then I use break to return to the first for loop. (line 43)
    Or, if total > b, it means I have found the satisfying t, so I return it. (line 45) If there isn't a t that satisfies the problem I return -1 (line 46)
    """

    seq = sequence_generator(n) 
    for t in range(1, 10001):
        while total < B: # I added the while loop so 'break' didn't terminate the outer for loop. Since total is reseted below, this will be True UNTIL i find t.
            for i in range(len(seq)):
                total += (seq[i]**((n - 1) - i)) * t
            if total < B:
                total = 0
                break
            else:
                return t
    return -1 


"""
Below I assign T it's new value. I didn't know if I was allowed to delete the one in line 2 so I just redeclared it.
"""
T = brute_force(n, B)

# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)
