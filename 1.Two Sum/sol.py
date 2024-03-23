class TwoSum:
    def __init__(self) -> None:
        pass

    def brute_force(self, nums: list[int], target: int) -> list[int]:
        """Brute force method, O(n2) time complexity

        Args:
            nums (list[int]): input list
            target (int): target number

        Returns:
            list[int]: result
        """
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i!=j and nums[i]+nums[j]==target:
                    return [i,j]
        return []
    
    def two_pass(self, nums: list[int], target: int) -> list[int]:
        """Two pass method using hash map, O(n) solution

        Args:
            nums (list[int]): input list
            target (int): target number

        Returns:
            list[int]: result
        """
        num_map = {}

        for i, num in enumerate(nums):
            num_map[num] = i

        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in num_map and num_map[compliment] != i:
                return [i,num_map[compliment]]
        return []
    
    def one_pass(self, nums: list[int], target: int) -> list[int]:
        """One pass method using hash map, O(n) solution

        Args:
            nums (list[int]): input list
            target (int): target number

        Returns:
            list[int]: result
        """
        num_map = {}
        for i, num in enumerate(nums):
            compliment =  target - num
            if compliment in num_map:
                return i, num_map[compliment]
            num_map[num]= i
        return []
   
    
if __name__ == '__main__':
   obj = TwoSum()
   print(obj.brute_force([3,3],6))
   print(obj.two_pass([3,3],6))
   print(obj.one_pass([3,3],6))