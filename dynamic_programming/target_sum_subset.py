# https://www.youtube.com/watch?v=tRpkluGqINc&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=11
# RE DO
arr = [4,2,7,1,3]
tar = 10


dp_arr = [[ False ] * (tar + 1) for _ in range(len(arr)+1)]
# print(dp_arr)

dp_arr[0][0] = 0

for i in range(1, tar+1):
    dp_arr[0][i] = False

for i in range(0, len(arr)+1):
    dp_arr[i][0] = True


for i in range(1, len(arr)+1):
    for j in range(1, tar+1):
        possible = False
        if (dp_arr[i-1][j]) or (j - arr[i-1] >= 0 and dp_arr[i-1][j - arr[i-1]] == True):
            possible = True
        dp_arr[i][j] = possible

i = 0
for row in dp_arr:
    print(i,"-",row)
    i+=1

#----------------

def solution(arr, tar):
    dp_arr = [[False] * (len(tar) + 1) for _ in range(len(arr))]
    for i in range(len(dp_arr)):
        for j in range(len(dp_arr[0])):
            if i == 0 and j == 0:
                dp_arr[i][j] = 0
            elif i == 0:
                dp_arr[i][j] = False
            elif j == 0:
                dp_arr[i][j] = True
            else:
                if dp_arr[i-1][j]:
                    dp_arr[i][j] = True
                else:
                    val = arr[i-1]
                    if j >= val and dp_arr[i-1][j-val]:
                        dp_arr[i][j] = True