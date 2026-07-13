class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        first=float("inf")
        second=float("inf")
        for i in prices:
            if i< first:
                second=first
                first=i
            elif i< second:
                second=i
        cost=first+second
        if cost<=money:
            return money-cost
        return money

        