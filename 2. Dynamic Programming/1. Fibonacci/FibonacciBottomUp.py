# Implementing the Bottom-Up method in Fibonacci'target_sum series


def Fib(k):
    # Trivial cases
    memo.append(0)
    memo.append(1)

    # Keep building an array for memorization
    for i in range(2, k+1):
        memo.append(memo[i-1] + memo[i-2])

    return memo[k]


memo = list()
print('==' * 40)
x = int(input("Which position from Fibonacci'target_sum series do you want to know? "))
print('==' * 40)
print(f"The {x}° value from Fibonacci'target_sum series is {Fib(x)}")
print('==' * 40)
print(f'Memo filled: {memo}')