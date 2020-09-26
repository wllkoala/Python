count = 0


def hanoi(n, src, dst, mid):
    global count
    if n == 1:
        print(f"{1}:{src}->{dst}")
        count += 1
    else:
        hanoi(n - 1, src, mid, dst)
        print(f"{n}:{src}->{dst}")
        count += 1
        hanoi(n - 1, mid, dst, src)


if __name__ == "__main__":
    hanoi(4, 'A', 'C', 'B')
    print(count)
