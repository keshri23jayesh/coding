def sub_sum(cur_sum, des_sum, arr, sub_arr):
    if not len(arr):
        if cur_sum == des_sum:
            print(sub_arr)
        return
    sub_arr.append(arr[0])
    sub_sum(cur_sum+arr[0], des_sum, arr[1:], sub_arr)
    sub_arr.pop()
    sub_sum(cur_sum, des_sum, arr[1:], sub_arr)


sub_sum(0, 60, [10, 20, 30, 40, 50], [])
