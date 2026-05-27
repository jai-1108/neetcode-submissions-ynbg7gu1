class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        no_of_boats = 0
        """
        p = [1,2,2,3,3], limit = 3
        l = 0, 1
        r = 4, 3
        weight = 4
        no_of_boats = 1
        r-=1
        weight = 4
        no_of_boats = 2
        r-=1
        l = 0,1 r=2,2
        weight = 3
        no_of_baot



        
        """
        people.sort()
        l = 0
        r = len(people) - 1
        while l<r:
            weight = people[l] + people[r]
            if weight > limit:
                r-=1
                no_of_boats += 1
            else:
                l+=1
                r-=1
                no_of_boats += 1
            if l==r:
                no_of_boats += 1
        return no_of_boats
            

