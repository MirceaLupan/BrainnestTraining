# A permutation is an ordered arrangement of objects. For example, 3124
# is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically,
# we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
# 012 021 102 120 201 210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


def permutations(arr):
    """generate all the permutations in lexicographic order"""
    while True:
        yield list(arr)

        # classic algorithm to generate permutations in lexicographic order
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                break
        if i < 0:
            return

        for j in range(len(arr) - 1, i, -1):
            if arr[i] < arr[j]:
                break

        arr[i], arr[j] = arr[j], arr[i]

        i += 1
        j = len(arr) - 1
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1


i = 0
for perm in permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
    i += 1
    if i == 1_000_000:
        print(perm)
        break

# 2783915460
