import grammar

def create_table(n):
    table = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append("")
        table.append(temp)
    return table

def concat(x, y):
    z = []
    for i in x:
        for j in y:
            z.append("{}{}".format(i, j))
    return z

def table_filling_process(array):
    table = create_table(len(array))
    for i in range(len(array)):
        table[i][i] = grammar.check_production([array[i]])
    for i in range(1, len(array)):
        for j in range(i, len(array)):
            temp = []
            for k in range(j-i, j):
                temp = temp + concat(table[j-i][k], table[k+1][j])
            table[j-i][j] = grammar.check_production(temp)
    return grammar.check_symbol(table[0][len(array)-1])
