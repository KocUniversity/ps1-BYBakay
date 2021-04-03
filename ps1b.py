n, B = list(map(int, input().strip().split()))
T = 0

# your code here

def sequence_generator(n):
  '''
  Same as the one in ps1a. I explained this method in detail in that part.
  '''
  seq = []
  for i in range(1, n + 1): # I start at 1 as instructed.
      if i % 2 == 0:
          seq.append((2**i) + 1) # (2^i + 1 for even numbers)
      else:
          seq.append((3**i) + 1) # (3^i + 1 for odd numbers)
  return seq

def bisection_searcher(n, B, break_value=None, total=0):
  '''
  The way I generated and calculated the equation is the same as brute_force, I explained it in detail in ps1a. 
  As instructed, I stored the minimum value that satified the equation in min_value. It's updated if a smaller one was found. (line 36)
  break_value is used to store the previous guess. If guess is the same as Break_value, that means program has entered to a loop, so it's forced to stop. I was going to name it last_guess, but break_value sounded cooler to me. It's first value is None and it doesn't have an integer value until we find an unsatisfactory guess. It's not necessary to give it a new value when we find a satisfactory guess. (line 18)
  The way bisection works in this case is, we make our first guess, then if we find a satisfying value, first we update high so our next guess will be smaller. If it's not satisfying, it updates low so our next guess will be bigger.(pretty much all lines below.)
  When consecuttive guesses are the same, the program breaks and returns min_value, which is the smallest integer that satisfies the equation.(line 32)

  '''
  seq = sequence_generator(n)
  low = 0
  high = 10000
  guess = (high + low) // 2
  min_value = None
  while guess != break_value:
    for i in range(len(seq)):
      total += (seq[i] ** ((n - 1) - i)) * guess
    if total > B:
      high = guess
      min_value = guess
      total = 0
    else:
      low = guess
      break_value = guess
      total = 0
    guess = (high + low) // 2
  if min_value == None:
    return -1
  return min_value

T = bisection_searcher(n, B)
# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)