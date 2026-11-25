t = [42, 23, 2, 3, 50]
print([2*v for v in t])
[v for v in t if v >= 10]
[i for i in range(len(t)) if (t[i] % 2) == 1]
[ch[0] for ch in ["Ada", "Alice", "Bob", "Eve"]]
[i % 10 for i in range(9, 12)]
[i % 10 for i in range(55) if (i // 50) == 1]
[i for i in range(len(t)) if t[i] == i]