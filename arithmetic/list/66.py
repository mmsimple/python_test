
def plusOne(digits):
    # print(digits)
    # s = ''.join(str(i) for i in digits)
    # s = int(s) + 1
    # s = str(s)
    # arr = []
    # for i in s:
    #     arr.append(int(i))

    # print(arr)

  

    digits = list(map(int,(str(int("".join(list(map(str,digits))))+1))))

    return 1 



plusOne([1,2,3,4])

