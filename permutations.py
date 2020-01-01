def permutations(things):
    # Heap's Permutation Algorithm
    thing_list = list(things)
    thing_count = len(thing_list)
    swap_tracker = [0] * thing_count

    yield tuple(thing_list)
    i = 0
    while i < thing_count:
        j = swap_tracker[i]
        if j < i:
            if i % 2:
                thing_list[j], thing_list[i] = thing_list[i], thing_list[j]
            else:
                thing_list[0], thing_list[i] = thing_list[i], thing_list[0]
            yield tuple(thing_list)
            swap_tracker[i] += 1
            i = 0
        else:
            swap_tracker[i] = 0
            i += 1
