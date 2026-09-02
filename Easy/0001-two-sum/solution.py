class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Store numbers already searched along with it's index
        dict_searched = {}

        # Search the input list of numbers
        for i, val in enumerate(nums):
            # Check if this the value we are searching for
            pair_val = target - val

            # Store in the dictionary once searched. If pair found return the value from dictionary
            if pair_val in dict_searched:
                # return the value
                return [
                    dict_searched[pair_val],
                    i,
                ]  # value and it's position in the dictionary

            # if the pair value is not found store it in dictionary
            dict_searched[val] = i

