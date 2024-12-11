FREE = -1


def solve(data: str):
    disk = []
    cur_id = 0

    i = 0
    while i < len(data):
        filelen = int(data[i])
        i += 1
        disk.extend([cur_id] * filelen)
        cur_id += 1

        if i < len(data):
            freelen = int(data[i])
            i += 1
            disk.extend([FREE] * freelen)

    size = len(disk)

    def next_free(offset: int):
        return next(i for i in range(offset, size) if disk[i] == FREE)

    def prev_used(offset: int):
        return next(i for i in range(offset, -1, -1) if disk[i] != FREE)

    num_used = sum(disk[i] != FREE for i in range(size))
    freeptr, usedptr = next_free(0), prev_used(size - 1)
    while freeptr < num_used:
        disk[freeptr], disk[usedptr] = disk[usedptr], disk[freeptr]
        freeptr = next_free(freeptr + 1)
        usedptr = prev_used(usedptr - 1)
    return sum(i * disk[i] for i in range(num_used))
