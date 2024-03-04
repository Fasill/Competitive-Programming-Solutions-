class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        """
            First, I count the number of distinct elements in the entire array:
                n = len(set(nums))

            Then, I initiate an empty set:
                distinctArrays = set()

            Next, I initiate a counter variable to count complete subarrays:
                completeSubarrayCounter = 0

            I traverse through the entire array, adding each element to the distinctArrays set. 
            Then, I calculate the length of the distinctArrays set, and if it equals 'n', I increment 
            the completeSubarrayCounter by one.

            Time Complexity:
            Since I'm iterating through the array for every single element, it's going to be O(n^2).

            Space Complexity:
            Since I'm using a set to store the distinct elements, it will be O(n).
        
        """
        
        leng = len(nums)
        n = len(set(nums))
        completeSubarrayCounter = 0

        for i in range(leng):
            distnitArrays = set()

            for j in range(i,leng):
                distnitArrays.add(nums[j])
                ln = len(distnitArrays)
                if ln == n:
                    completeSubarrayCounter+=1

        return completeSubarrayCounter