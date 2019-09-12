def col_index(column_name):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    index = 0
    for i in range(1,len(column_name)+1):
        index += (alpha.index(column_name[-i].lower())+1 )* (26 ** (i-1))
        return index
print(col_index('AA'))