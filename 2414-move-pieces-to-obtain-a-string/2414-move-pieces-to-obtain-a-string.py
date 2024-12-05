class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start_length = len(start)
        start_index, target_index = (0, 0)

        while start_index < start_length or target_index < start_length:
            
            while start_index < start_length and start[start_index] == "_":
                start_index += 1

            while target_index < start_length and target[target_index] == "_":
                target_index += 1

            if start_index == start_length or target_index == start_length:
                return (
                    start_index == start_length and target_index == start_length
                )

            if (
                start[start_index] != target[target_index]
                or (start[start_index] == "L" and start_index < target_index)
                or (start[start_index] == "R" and start_index > target_index)
            ):
                return False

            start_index += 1
            target_index += 1

        return True