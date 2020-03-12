# Write a program that outputs the string representation of numbers from 1 to n.

# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

# Example:

# n = 15,

# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]



class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizzbuzz_list = []
        
        for i in range(1, n+1):
            if i%3 == 0 and i%5 == 0:
                fizzbuzz_list.append("FizzBuzz")
            elif i%3 == 0:
                fizzbuzz_list.append("Fizz")
            elif i%5 == 0:
                fizzbuzz_list.append("Buzz")
            else:
                fizzbuzz_list.append(str(i))
        return fizzbuzz_list


#####################################
######### Fancy one-liner ###########
#####################################


# def fizzBuzz(self, n):
#     return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]


# def fizzBuzz(self, n):
#     return['FizzBuzz'[i%-3&-4:i%-5&8^12]or`i`for i in range(1,n+1)]