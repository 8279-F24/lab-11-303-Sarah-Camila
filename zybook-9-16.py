numbers = list(map(int, input().split()))

negatives_descending = sorted([num for num in numbers if num < 0], reverse=True)

print(" ".join(map(str, negatives_descending)), end=" ")