def print_hi(N):
    for i in range(1, N):
        j = i
        if i % 3 == 0:
            j = "Frontend"
        if i % 5 == 0:
            j = "Backend"
        if i % 5 == 0 and i % 3 == 0:
            j = "Frontend Backend"
        print(j, ",", end="")


if __name__ == '__main__':
    print_hi(50)

