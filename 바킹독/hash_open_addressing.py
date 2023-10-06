M = 1000003
a = 1000
EMPTY = -1
OCCUPY = 0
DUMMY = 1

status = [-1] * M
key = [""] * M
val = [0] * M


def my_hash(s: str) -> int:
    h = 0
    for c in s:
        h = (h * a + ord(c)) % M
    return h


def find(k: str) -> int:
    idx = my_hash(k)
    while status[idx] != -1:
        if key[idx] == k and status[idx] == 0:
            return idx
        idx += 1
    return -1


def insert(k: str, v: int) -> None:
    idx = find(k)
    if idx != -1:
        val[idx] = v
        return
    idx = my_hash(k)
    while status[idx] == 0:
        idx += 1
    key[idx] = k
    val[idx] = v
    status[idx] = 0


def erase(k: str) -> None:
    idx = find(k)
    if idx == -1:
        return
    status[idx] = 1


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
