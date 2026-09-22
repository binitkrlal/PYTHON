def mirror_pattern(N, char):
    for i in range(1, N + 1):
        spaces = ' ' * (N - i)
        stars = char * i
        print(spaces + stars)

    print('_' * N)

    for i in range(N, 0, -1):
        spaces = ' ' * (N - i)
        stars = char * i
        print(spaces + stars)

# Input
N = int(input())
char = input()

# Output
mirror_pattern(N, char)