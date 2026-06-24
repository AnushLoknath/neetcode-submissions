class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car=[]
        for i in range(len(position)):
            time=(target-position[i])/speed[i]
            car.append([position[i],time])
        car.sort(reverse=True)
        fleet=0
        slow=0
        for position, time in car:
            if time>slow:
                fleet+=1
                slow=time
        return fleet
       

       

        