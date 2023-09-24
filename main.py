tree = {}

print("Loading dataset...")

# french dataset file is here (60 Go): http://data.statmt.org/cc-100/fr.txt.xz
with open("fr.txt", "r", encoding="UTF-8") as f:
    for i ,line in enumerate(f):
        # load first 1000000 lines, change it if is very slow :)
        if i > 1_000_000:
            break
        cleared_line = line.replace("\n", "").split(" ")
        for idx in range(len(cleared_line) - 1):
            actual = cleared_line[idx].lower()
            future = cleared_line[idx + 1].lower()
            if actual not in tree: tree[actual] = {future: 1}
            elif future not in tree[actual]: tree[actual][future] = 1
            else: tree[actual][future] += 1
        i += 1

print("Dataset loaded!")

while True:
    word = input("-> ").split(" ")[-1].lower()
    if word in tree:
        next_words = tree[word]
        print(*sorted(next_words, key=next_words.get, reverse=True)[:3], sep="  |  ")
