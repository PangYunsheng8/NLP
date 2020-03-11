# Edit Distance
# 1)state
# 2)state transition equation
# 3)initialization and boundary
# 4)computation order

class EditDistance:
    def compute_distance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        edit = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if min(i, j) == 0:
                    edit[i][j] = max(i, j)
                else:
                    flag = 0 if word1[i-1] == word2[j-1] else 1
                    edit[i][j] = min(edit[i-1][j] + 1, edit[i][j-1] + 1, edit[i-1][j-1] + flag)
        return edit[-1][-1]


if __name__ == '__main__':
    ed = EditDistance()
    ed_value = ed.compute_distance('horse', 'ros')
    print(ed_value)