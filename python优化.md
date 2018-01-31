# python优化

 **1. 避免使用字符串 + 运算**
    

 - 使用join

----------

    s = ""
    for substring in list:
        s += substring
替换为

    s = "".join(list)
    
 - 使用%s

----------

    out = "<html>" + head + prologue + query + tail + "</html>"
替换为

    out = "<html>%s%s%s%s</html>" % (head, prologue, query, tail)
更好的是

    out = "<html>%(head)s%(prologue)s%(query)s%(tail)s</html>" % locals()
    
**2. 避免在循环中使用 . 运算**
    
----------

    d = {}
    for i in list:
        d[i] = d.get(i, 0) + 1
替换为
    
    d = {}
    get = d.get
    for i in list:
        d[i] = get(i, 0) + 1
    


