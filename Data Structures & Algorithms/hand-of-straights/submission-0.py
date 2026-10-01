class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        groupCount = len(hand) // groupSize 
        hand.sort()

        hs = {}

        for nr in hand:
            if nr in hs:
                hs[nr] += 1
            else :
                hs[nr] = 1

        currentGroupCount = 0

        for nr in hand:
            if hs[nr] == 0:
                continue
            end = nr + groupSize
            for i in range(nr, end):
                if i not in hs:
                    return False 
                hs[i] -= 1

        return True


        