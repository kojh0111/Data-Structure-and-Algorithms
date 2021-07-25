def isPalindrome(num):
    num = str(num)
    if num == num[::-1]:
        return True
    else:
        return False


def prime(n):
    n_sqrt = int(n ** 0.5) + 1
    prime_tf = [True] * (n + 1)
    for i in range(2, n_sqrt):
        if prime_tf[i]:
            for j in range(i * 2, n + 1, i):
                prime_tf[j] = False
    prime_num = [i for i in range(2, n + 1) if prime_tf[i]]
    prime_palindrome = [i for i in prime_num if isPalindrome(i)]
    return prime_palindrome


n = int(input())
under_million = prime(1003001)
for i in under_million:
    if n <= i:
        print(i)
        break
