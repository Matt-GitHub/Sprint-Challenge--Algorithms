#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) a = 0
while (a < n _ n _ n):
a = a + n \* n

      Answer: Will run in O(n) time. N * N * N is a constant number. A grows at a rate of N * N + the previous products.

b) sum = 0
for i in range(n):
j = 1
while j < n:
j \*= 2
sum += 1

        Answer: Will run in O(n * m) where n is the paramter passed in and m represents the amount of iterations it takes to get j > n

def bunnyEars(bunnies):
if bunnies == 0:
return 0

      return 2 + bunnyEars(bunnies-1)

      Answer: Will run in O(n) time. Basically we take n and subtract 1 from it everytime until we get to 0. This is a classic iteration counting down

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Answer: This is a classic search algorithm. The first pass solution would be to use a linear search and test each egg at each floor. if it breaks then we found our floor. The issue is this solution runs at a worst case of O(n). Meaning the egg is on the last floor. To improve this search we can use a binary search and test the dropping of our egg at the middle floor. Each time we drop our egg at the middle floor we can determine if we are too high or too low. Thus, we can remove half of the remaining floors with each drop. This will significenly improve our runtime effeciency and lead us with a time complexity of O(log n)
