# def fibonacci(a):
#     if a <= 0:
#         return 0
#     elif a == 1:
#         return 0
#     elif a == 2:
#         return 1
#     else:
#         return fibonacci(a-1) + fibonacci(a-2)

# b = int(input("Enter number of terms: "))

# print("Fibonacci Series:")
# for i in range(1, b + 1):
#     print(fibonacci(i),end=" ")



def power_set(s, index=0, current=[]):
    if index == len(s):
        print(current)
        return
    
    power_set(s, index + 1, current)
    
    power_set(s, index + 1, current + [s[index]])

elements = list(map(int, input("Enter elements separated by space: ").split()))

print("Power Set:")
power_set(elements)



