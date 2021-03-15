def check_duplicates(lst: list) -> list:
    dup = []
    for elem in lst:
        if elem not in dup and lst.count(elem) > 1:
            dup.append(elem)
    return dup
