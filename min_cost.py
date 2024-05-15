import heapq

def min_cost_to_connect_cables(cable_lengths):
    total_cost = 0
    heapq.heapify(cable_lengths)  # перетворюємо список в пріоритетну чергу

    while len(cable_lengths) > 1:
        # беремо два кабелі з найменшою довжиною
        min1 = heapq.heappop(cable_lengths)
        min2 = heapq.heappop(cable_lengths)
        # обчислюємо вартість їх з'єднання та додаємо до загальної вартості
        cost = min1 + min2
        total_cost += cost
        # додаємо нову суму до пріоритетної черги
        heapq.heappush(cable_lengths, cost)

    return total_cost

# Приклад використання
cable_lengths = [8, 4, 6, 12, 10, 14]
min_cost = min_cost_to_connect_cables(cable_lengths)
print("Мінімальна вартість з'єднання кабелів:", min_cost)
