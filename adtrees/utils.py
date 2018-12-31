def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.

    Code by Rory McCann:
    https://www.technomancy.org/python/powerset-generator-python/
    """
    if len(seq) == 0:
        yield []
    elif len(seq) == 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]] + item
            yield item


def combine_bundles(A, B):
    """
    Needed for set semantics.
    A = [[set, set], [set, set], ..., [set, set]]
    B = [[set, set], [set, set], ..., [set, set]]
    result
    """
    if len(A) > 0 and len(B) > 0:
        res = []
        for a in A:
            for b in B:
                candidate = [a[0].union(b[0]), a[1].union(b[1])]
                if candidate not in res:
                    res.append(candidate)
        # return [[a[0].union(b[0]), a[1].union(b[1])] for a in A for b in B]
        return res
    elif len(A) > len(B):
        return A
    elif len(B) != 0:
        return B
    else:
        return []


def listunion(A, B):
    """
    Needed for set semantics.
    """
    res = [x for x in A]
    for x in B:
        if x not in res:
            res.append(x)
    return res


def otimes(A, B):
    """
    """
    return [listunion(a, b) for a in A for b in B]


def odot(A, B):
    if A == [[]] or B == [[]]:
        return [[]]
    else:
        return listunion(A, B)
