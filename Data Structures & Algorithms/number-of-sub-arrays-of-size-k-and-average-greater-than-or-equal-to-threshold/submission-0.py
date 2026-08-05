class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total=0
        count=0
        for i in range(k):
            total+=arr[i]
        avg=total//k
        if avg >= threshold:
            count+=1
        for i in range(k,len(arr)):
            total+=arr[i]
            total-=arr[i-k]
            avg=total//k
            if avg >=threshold:
                count+=1
        return count

        