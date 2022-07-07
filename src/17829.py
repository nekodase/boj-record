N = int(input())
image = [list(map(int, input().split())) for _ in N]

def MPresult(image, N):
    if N == 1:
        return image[0][0]
    arr = []
    for i in range(0, N, 2):
        row = []
        for j in range(0, N, 2):
            row.append(sorted((image[i][j], image[i][j+1], image[i+1][j], image[i+1][j+1]))[-2])
        kernel.append(row)
    return MPresult(arr, N//2)

print(MPresult(image, N))