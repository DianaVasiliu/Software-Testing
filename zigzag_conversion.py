def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s

    allList = [""] * numRows
    sign = 1
    k = 0

    for i in range(len(s)):
        if k == numRows - 1:
            sign = -1
        if k == 0:
            sign = 1

        allList[k] += s[i]
        k += sign

    ans = ""
    for i in range(len(allList)):
        ans += allList[i]

    return ans


def zigzag() -> str:
    file = open("zigzag.txt")
    data = file.readline()
    data = data.split()
    try:
        initialText = data[0]
        num = int(data[1])
        return convert(initialText, num)
    except ValueError:
        return "Error: Invalid input"
