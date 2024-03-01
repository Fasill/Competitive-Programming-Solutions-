class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        """
            First, I'll create an array that holds the partition length:
            lengthOfPartitions = []

            Next, I'll calculate the frequency for every single element:
            allCounter = Counter(s)

            Then, I'll create an empty dictionary to create a reference counter:
            referenceCounter = Counter()

            I'll also create one more empty counter to count the frequency of each number in a specific interval:
            runningCounter = Counter()

            I'll iterate through the string and add the string frequency in all strings to referenceCounter. 
            I'll increment the frequency of the element by one in the runningCounter, 
            and if runningCounter is equal to the referenceCounter, I'll add the length to lengthOfPartitions. If not, I'll add the right pointer.

        """
        lengthOfPartitions = []

        allCounter = Counter(s)
        referenceCounter = Counter()
        runningCounter = Counter()

        leftPt = 0
        lenS = len(s)

        for rightPt in range(lenS):

            referenceCounter[s[rightPt]] = allCounter[s[rightPt]]
            runningCounter[s[rightPt]] += 1

            if runningCounter == referenceCounter:
                lengthOfSubString = rightPt-leftPt+1
                lengthOfPartitions.append(lengthOfSubString)
                referenceCounter = Counter()
                runningCounter = Counter()
                leftPt = rightPt + 1

        return lengthOfPartitions