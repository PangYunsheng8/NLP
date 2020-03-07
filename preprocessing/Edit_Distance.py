# Edit Distance
# 1)state
# 2)state transition equation
# 3)initialization and boundary
# 4)computation order

class EditDistance:
    def compute_distance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        edit = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if min(i, j) == 0:
                    edit[i][j] = max(i, j)
                else:
                    flag = 0 if word1[i] == word2[j] else 1
                    edit[i][j] = min(edit[i-1][j] + 1, edit[i][j-1] + 1, edit[i-1][j-1] + flag)
        return edit[-1][-1]


if __name__ == '__main__':
    ed = EditDistance()
    ed_value = ed.compute_distance('bitch', 'batches')
    print(ed_value)