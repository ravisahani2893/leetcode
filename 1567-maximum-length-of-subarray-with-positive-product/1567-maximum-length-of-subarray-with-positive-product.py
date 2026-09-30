class Solution:
    def getMaxLen(self, nums: list[int]) -> int:
        positiveLength=0
        negativeLength=0
        maxLength=0

        for i in range(len(nums)):

            if nums[i] == 0:
                positiveLength=0
                negativeLength=0
            elif nums[i] < 0:
                oldNegativeLength = negativeLength
                oldPositiveLength = positiveLength

                if oldNegativeLength > 0:
                    positiveLength = oldNegativeLength + 1
                else:
                    positiveLength = 0

                negativeLength = oldPositiveLength + 1
                maxLength = max(maxLength, positiveLength)
            else:
                positiveLength=positiveLength+1
                if negativeLength>0:
                    negativeLength=negativeLength+1
                maxLength = max(maxLength, positiveLength)
            

        return maxLength
        