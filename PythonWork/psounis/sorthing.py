def selection_sort(array, reverse=False):
    for i in range(0, len(array)):
        # ypologismos ths thesis, ths elaxisths posothtas
        pos = i
        for j in range(i + 1, len(array)):
            if reverse:
                if array[j] > array[pos]:
                    pos = j
            else:
                if array[j] < array[pos]:
                    pos = j

        array[i], array[pos] = array[pos], array[i]


array = [1, 12, 4, 2, 5, 7]
selection_sort(array, False)

print(array)