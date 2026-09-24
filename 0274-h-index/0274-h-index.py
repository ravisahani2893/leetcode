class Solution:
    def hIndex(self, citations: list[int]) -> int:
        totalPaper = len(citations)

        citations.sort(reverse=True)
        
        

       

        while(totalPaper > 0):
            count=0
            for i in range(len(citations)):

                if citations[i] < totalPaper:
                    break

                if citations[i] >= totalPaper:
                    count=count+1
                

            if count >= totalPaper:
                return totalPaper

            totalPaper=totalPaper-1



           

        return 0
        