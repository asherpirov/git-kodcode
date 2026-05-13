def is_even(n):
    if n % 2 == 0:
        return True
    return False

def factorial(n):
    factory = 1
    for i in range(1, n+1):
       factory *= i
    return factory

def digital_root(n):
    pass

def is_palindrome(s):
    word = s
    for i in range(len(s)):
        if word[i] != word[-i-1]:
            return False
    return True

def sum_digits(n):
    pass

def count_digit_num(n: int):
    count = 0
    while n > 0:
        new_num = n // 10
        n = new_num
        count += 1
    return count

def reversed_number(n):
    if n == 0:
        return 0
    is_negative = n < 0
    n = abs(n)
    reversed_num = 0
    while n > 0:
        last_digit = n % 10
        reversed_num = (reversed_num * 10) + last_digit
        n = n // 10

    if is_negative:
        reversed_num = -reversed_num
    return reversed_num


def move_zero_end(nums: list):
   i = 0
   zero_count = 0

   while i < len(nums):
       if nums[i] == 0:
          zero_count += 1
          nums.pop(i)
       else:
           i += 1
   nums += [0] * zero_count
   return nums

print(move_zero_end ([1,5,0,0,7,0,5]))