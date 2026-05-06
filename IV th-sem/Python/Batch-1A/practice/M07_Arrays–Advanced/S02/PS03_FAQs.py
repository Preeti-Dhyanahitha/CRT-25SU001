#Pascal's traingle
def generate(numRows):
    res = []
    for i in range(numRows):
        row = [1] * (i+1)
        for j in range(1,i):
            row[j] = res[i-1][j] + res[i-1][j-1]
        res.append(row)
    return res
print(generate(5))

#Spiral matrix
def spiralOrder(self, matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    top = 0
    bottom = rows - 1
    left = 0
    right = cols - 1

    ans = []

    while top <= bottom and left <= right:

        # left -> right
        for col in range(left, right + 1):
            ans.append(matrix[top][col])
        top += 1

        # top -> bottom
        for row in range(top, bottom + 1):
            ans.append(matrix[row][right])
        right -= 1

        # right -> left
        if top <= bottom:
            for col in range(right, left - 1, -1):
                ans.append(matrix[bottom][col])
            bottom -= 1

        # bottom -> top
        if left <= right:
            for row in range(bottom, top - 1, -1):
                ans.append(matrix[row][left])
            left += 1

    return ans