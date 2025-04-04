# https://www.youtube.com/watch?v=qyfekrNni90&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=13


piles = [3,6,7,11]

def able_to_eat(mid):
    hours = 0
    for banana in piles:
        if banana <=  mid:
            hours += 1
        else:
            hours += (banana//mid) +  (1 if (banana % mid) else 0)
    return hours


def find_min_banana_per_hour(hours):
    low = 1
    high = sum(piles)
    final_ans = high
    while low <= high:
        mid = (low + high)//2
        ans = able_to_eat(mid)
        if ans <= hours:
            final_ans = mid
            high = mid - 1
        elif ans > 0:
            low = mid + 1
    return final_ans


print(find_min_banana_per_hour(8))
