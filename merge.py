import heapq

def merge_k_lists(lists):
    merged = []
    heap = []

    # Додаємо перший елемент з кожного списку до купи
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    # Злиття купи
    while heap:
        val, lst_index, val_index = heapq.heappop(heap)
        merged.append(val)
        if val_index + 1 < len(lists[lst_index]):
            next_val = lists[lst_index][val_index + 1]
            heapq.heappush(heap, (next_val, lst_index, val_index + 1))

    return merged

# Приклад використання
lists = [
    [1, 4, 5], 
    [1, 3, 4], 
    [2, 6]
]
merged_list = merge_k_lists(lists)
print("Об'єднаний відсортований список:", merged_list)
