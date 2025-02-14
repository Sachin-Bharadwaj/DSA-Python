def BinarySearch(number_list, num_to_search):
    '''
    [1] number_list: assuming that this is ordered list in ascending order
    [2] num_to_search: the number to search in the list
    '''
    start = 0
    end = len(number_list)-1

    while start <= end:
        mid = (start + end)//2

        if num_to_search == number_list[mid]:
            return mid
        elif num_to_search < number_list[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return -1  # unsuccessful

if __name__ == "__main__":
    number_list = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    ans = BinarySearch(number_list, 99)
    print(ans)