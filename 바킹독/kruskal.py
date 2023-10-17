V = 100

parent = [i for i in range(V)]

def find_parent(v1):
    if parent[v1] == v1:
        return v1
    parent[v1] = find_parent(parent[v1])
    return parent[v1]


def have_same_parent(v1, v2):
    pv1 = find_parent(v1)
    pv2 = find_parent(v2)
    if pv1 == pv2:
        return True
    else:
        if pv1 > pv2:
            parent[pv1] = pv2
        else:
            parent[pv2] = pv1
        return False