def linear_search(lst, target):
    """
    Линейный поиск: возвращает индекс первого вхождения target в lst
    или -1, если элемент не найден.
    """
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1