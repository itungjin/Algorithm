N = int(input())

primes = []
is_prime = [True] * (N + 1)
for n in range(2, N + 1):
    if is_prime[n]:
        primes.append(n)
        m = n * n
        while m <= N:
            is_prime[m] = False
            m += n

answer = 0
left = 0
right = 0

if N == 1:
    print(0)
    exit(0)

subtotal = primes[0]
while True:
    if left == len(primes):
        break
    if subtotal == N:
        answer += 1
        right += 1
        if right == len(primes):
            break
        subtotal += primes[right] - primes[left]
        left += 1
    elif subtotal > N:
        subtotal -= primes[left]
        left += 1
    else:
        right += 1
        if right == len(primes):
            break
        subtotal += primes[right]
print(answer)
