def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    for num in nums:
        if num == 7:
            return True

    # for loop completed -- no 7s were found. return False.
    return False
    

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

