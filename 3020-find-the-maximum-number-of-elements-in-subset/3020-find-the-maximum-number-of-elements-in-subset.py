class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        freq = Counter(nums)
        maxi = freq[1] if freq[1] % 2 == 1 else freq[1] - 1

        for num in nums:
            if num in freq:
                curr = num
                del freq[curr]
                count = 1

                while True:
                    temp = sqrt(curr)

                    if temp == floor(temp) and freq[temp] >= 2:
                        count += 2
                        del freq[temp]
                        curr = temp
                    else:
                        break
                
                maxi = max(maxi,count)

        return maxi