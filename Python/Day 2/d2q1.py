"""Day 2: Question 1."""

def is_safe(seq):
    """Create fonction to verify if a sequence is safe."""
    safe_increase = True
    safe_decrease = True
    for i in range(len(seq) - 1):
        if not 1<= seq[i] - seq[i + 1] <= 3:
            safe_decrease = False
        if not 1 <= seq[i + 1] - seq[i] <= 3:
            safe_increase = False
    return safe_increase or safe_decrease

data = []

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        numbers = list(map(int, line.split()))
        data.append(numbers)

UNSAFE_COUNT = 0
SAFE_COUNT = 0

for sequence in data:
    if is_safe(sequence):
        SAFE_COUNT += 1
    else:
        UNSAFE_COUNT += 1

print("Unsafe count:", UNSAFE_COUNT)
print("Safe count:", SAFE_COUNT)
