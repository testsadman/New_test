class Solution:
    def topKFrequent(self, nums, k):
        container = [[] for i in range(len(nums)+1)] #doing bucket sort
        real = []
        for i in (set(nums)):
            container[nums.count(i)].append(i) # appending the count of the number to the container

        for i in range(len(nums), -1, -1): # iterating from the end of the container as we want the most frequent numbers
            if container[i] != [] and k > 0:
                real.extend(container[i]) # extending the real array with the numbers in the container
                k -= len(container[i]) # subtracting the length of the container from k because we want the top k frequent numbers
        return real
