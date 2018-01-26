# pandas raplace 正则替换

    df.replace(regex={'^="': '', '"$': ''})

等价于

    df.replace(r'="(.*)"', '\g<1>', regex=True)

**pandas的replace 相当于 re.sub 替换**