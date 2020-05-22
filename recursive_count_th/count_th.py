'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# first pass


def count_th(word):
    # * set count and target
    count = 0
    target = 'th'
    # * set base case to stop recursion
    if len(word) <= 1:
        return count
    # * case where the first 2 letters in list equal target
    if word[0:2] == target:
        # * add one to count
        count += 1
        # * since we know the next 2 letters equal our target we can skip going to the next character and just analyze the next pair
        return count + count_th(word[2:])
    # * the current pair is not target therefore we return our count + recursively call our function with our list without the first char
    return count + count_th(word[1:])

    # ! Runtime will be O(n) as we traverse the entire len of the list until len is less than or equal to 1
    # ! Space complexity will be O(n)
