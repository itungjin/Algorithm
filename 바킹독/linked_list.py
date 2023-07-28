MX = 1000005
dat = [0] * MX
pre = [-1] * MX
nxt = [-1] * MX
unused = 1


def traverse() -> None:
    cur = nxt[0]
    while cur != -1:
        print(dat[cur], end=' ')
        cur = nxt[cur]
    print()


def insert(addr: int, num: int):
    global unused
    dat[unused] = num
    pre[unused] = addr
    nxt[unused] = nxt[addr]
    nxt[addr] = unused
    if nxt[unused] != -1:
        pre[nxt[unused]] = unused
    unused += 1


def insert_test():
    insert(0, 10)
    traverse()
    insert(0, 30)
    traverse()
    insert(2, 40)
    traverse()
    insert(1, 20)
    traverse()
    insert(4, 70)
    traverse()


def erase(addr: int) -> None:
    nxt[pre[addr]] = nxt[addr]
    if nxt[addr] != -1:
        pre[nxt[addr]] = pre[addr]


def erase_test():
    erase(1)
    traverse()
    erase(2)
    traverse()
    erase(4)
    traverse()
    erase(5)
    traverse()


insert_test()
erase_test()
