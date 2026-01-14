class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        # Each operation decreases distance by 2 (x decreases by 1, num increases by 1)
        # So maximum x = num + 2*t
        return num + 2 * t