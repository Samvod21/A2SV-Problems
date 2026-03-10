class Solution(object):
    def findRelativeRanks(self, score):
        size = len(score)
        st = sorted(score, reverse=True)
        x = 3

        for i in range(size):
            rank = st.index(score[i]) + 1

            if rank == 1:
                score[i] = "Gold Medal"
            
            elif rank == 2:
                score[i] = "Silver Medal"
            
            elif rank == 3:
                score[i] = "Bronze Medal"

            else:
                score[i] = str(rank)

        return score



        