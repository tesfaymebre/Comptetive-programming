class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def prime_sieve(n):
            is_prime: list[bool] = [True for _ in range(n + 1)]
            is_prime[0] = is_prime[1] = False

            i = 2

            while i * i <= n:
                if is_prime[i]:
                    j = i * i
                    while j <= n:
                        is_prime[j] = False
                        j += i
                i += 1

            return [num for num in range(n+1) if is_prime[num]]

        primes = prime_sieve(max(nums))

        for i in range(len(nums)-2,-1,-1):
            if nums[i] >= nums[i+1]:
                flag = False

                for j in primes:
                    if j < nums[i] and nums[i] - j < nums[i+1]:
                        nums[i] -= j
                        flag = True
                        break
                    elif j >= nums[i]:
                        break

                if not flag:
                    return False

        return True