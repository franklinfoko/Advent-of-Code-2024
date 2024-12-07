"""Day 2: Question 2."""

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

def is_safe_by_removing_one(seq):
    """Check if removing one level can make the sequence safe."""
    for i in range(len(seq)):
        new_seq = seq[:i] + seq[i+1:]
        if is_safe(new_seq):
            return True
    return False

data = []

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        numbers = list(map(int, line.split()))
        data.append(numbers)

UNSAFE_COUNT = 0
SAFE_COUNT = 0

for sequence in data:
    if is_safe(sequence) or is_safe_by_removing_one(sequence):
        SAFE_COUNT += 1
    else:
        UNSAFE_COUNT += 1

print("Unsafe count:", UNSAFE_COUNT)
print("Safe count:", SAFE_COUNT)
