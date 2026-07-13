class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        students.sort()
        seats.sort()
        move=0
        for i in range(len(students)):
            move+=abs(seats[i]-students[i])
        return move
        