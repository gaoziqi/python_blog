# pandas nunique

    import pandas as pd
    df = pd.DataFrame([
        [1,1], [1,2], [1,3], 
        [2,1], [2,1], [2,2]
        ], columns=['a', 'b'])
    
    df["b"].groupby(df["a"]).nunique()
    #   a
    #   1    3
    #   2    2
    df["b"].groupby(df["a"]).unique()
    #   a
    #   1    [1, 2, 3]
    #   2    [1, 2]