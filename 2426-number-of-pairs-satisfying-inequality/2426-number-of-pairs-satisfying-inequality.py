class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = [ x - y for x,y in zip(nums1,nums2)]
        count = 0
        
        def count_pairs(left_half, right_half):
            nonlocal count
            
            size_l = len(left_half)
            size_r = len(right_half)
            l = 0
            r = 0
            
            while l < size_l and r < size_r:
                if left_half[l] <= right_half[r] + diff:
                    count += size_r - r
                    l += 1
                else:
                    r += 1
                    
            return
        
        def merge(left_half, right_half):
            size_l = len(left_half)
            size_r = len(right_half)
            l = 0
            r = 0
            
            res = []
            
            while l < size_l and r < size_r:
                if left_half[l] <= right_half[r]:
                    res.append(left_half[l])
                    l += 1
                else:
                    res.append(right_half[r])
                    r += 1
            
            res.extend(left_half[l:])
            res.extend(right_half[r:])
            return res
                    
        
        def merge_sort(left,right):
            if left == right:
                return [arr[left]]
            
            mid = left + (right - left) // 2
            left_half = merge_sort(left, mid)
            right_half = merge_sort(mid+1, right)
            
            count_pairs(left_half, right_half)
            return merge(left_half,right_half)
        
        merge_sort(0, len(arr) - 1)
        return count
        