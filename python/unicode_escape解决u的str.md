# unicode_escape解决\u的str

    s = '\\u751F\\u5316\\u5371\\u673A'
    s.encode().decode('unicode_escape') # 生化危机