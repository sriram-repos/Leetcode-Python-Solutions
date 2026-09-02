# LeetCode 9: Palindrome Number

## Description
Determine if an integer reads the same backward as forward **without** converting it to a string.

## Leetcode Hint
Beware of overflow when you reverse the integer.

---

## Approach (Reversing the Second Half)
To avoid integer overflow, we only reverse the **right half** of the number and compare it to the left half.

1. **Filter Edge Cases:** Negative numbers and numbers ending in `0` (except `0` itself) cannot be palindromes.
2. **Meet in the Middle:** Chop digits off the back of the number using `% 10` and build a reversed number. Stop when the reversed number becomes greater than or equal to the remaining number.
3. **Compare:** 
   * Even length: Check if `left_half == right_half`.
   * Odd length: Discard the middle digit using `right_half // 10` before comparing.

