if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tuple_data = tuple(integer_list)
    print(hash(tuple_data))