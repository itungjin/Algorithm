M = 1000003
a = 1000

MX = 500005
head = [-1] * M
pre = [-1] * MX
nxt = [-1] * MX
key = [""] * MX
val = [0] * MX
unused = 0


def my_hash(s: str) -> int:
    h = 0
    for c in s:
        h = (h * a + ord(c)) % M
    return h


def find(k: str) -> int:
    h = my_hash(k)
    idx = head[h]
    while key[idx] != k and idx != -1:
        idx = nxt[idx]
    return idx


def insert(k: str, v: int) -> None:
    global unused
    idx = find(k)
    if idx == -1:
        h = my_hash(k)
        val[unused] = v
        key[unused] = k
        if head[h] != -1:
            nxt[unused] = head[h]
            pre[head[h]] = unused
        head[h] = unused
        unused += 1
    else:
        val[idx] = v


def erase(k: str) -> None:
    idx = find(k)
    if idx == -1:
        return
    h = my_hash(k)
    if head[h] == idx:
        head[h] = nxt[idx]
        pre[head[h]] = -1
    else:
        if pre[idx] != -1:
            nxt[pre[idx]] = nxt[idx]
        if nxt[idx] != -1:
            pre[nxt[idx]] = pre[idx]


def test():
    insert("orange", 724)
    insert("melon", 20)
    assert val[find("melon")] == 20
    insert("banana", 52)
    insert("cherry", 27)
    insert("orange", 100)
    assert val[find("banana")] == 52
    assert val[find("orange")] == 100
    erase("wrong_fruit")
    erase("orange")
    assert find("orange") == -1
    erase("orange")
    insert("orange", 15)
    assert val[find("orange")] == 15
    insert("apple", 36)
    insert("lemon", 6)
    insert("orange", 701)
    assert val[find("cherry")] == 27
    erase("xxxxxxx")
    assert find("xxxxxxx") == -1
    assert val[find("apple")] == 36
    assert val[find("melon")] == 20
    assert val[find("banana")] == 52
    assert val[find("cherry")] == 27
    assert val[find("orange")] == 701
    assert val[find("lemon")] == 6
    print("good!")


test()
