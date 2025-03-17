string = "1110001111001100"
# string = "110000"


def max_consecutive():
    left, right, k = 0, 0, 4
    strlen = len(string)
    num_zero = 0
    ans_len = 0
    while right < strlen:
        if string[right] == '0' and num_zero <= k:
            num_zero += 1
        while num_zero > k:
            if string[left] == '0':
                num_zero -= 1
            left += 1
        ans_len = max(ans_len, right-left+1)
        right += 1
    print(ans_len)

max_consecutive()