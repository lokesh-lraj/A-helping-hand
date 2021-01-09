def specialNumber(A):
    if A == 1:
        return '1'
    if A == 2:
        return '11'
    ans = '11'
    while A > 2:
        temp = []
        n = len(ans)
        l, r = 0, 0
        while r < n:
            if ans[l] == ans[r]:
                pass
            else:
                temp.append(str(r-l))
                temp.append(ans[l])
                l = r
            r += 1
        ans = ''.join(temp) + str(r-l) + (ans[l])
        A -= 1
    return ans

def sumOfTheDigits(q):
    d = {}
    ans = [0]*len(q)
    for i, elem in enumerate(q):
        if elem not in d:
            special_num = specialNumber(elem)
            d[elem] = sum(list(map(int, special_num)))
        ans[i] = d[elem]
    return ans
