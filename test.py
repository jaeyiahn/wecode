def even_num():
    empty = []
    for i in range(1,51):
        if i%2 == 0:
            empty.append(i)
        else:
            i += 1
    return empty