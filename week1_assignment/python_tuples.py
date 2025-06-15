if __name__ == '__main__':
    n = input()
    integer_list = map(int, raw_input().split())
    print hash(tuple(integer_list))
