
'''
Bubble Sort: Time Complexity: O(n^2)
Space Complexity: O(1)
'''
def BubbleSort(elements):
    length = len(elements)
    swapped = False
    for j in range(length-1):
        for i in range(length-1-j):
            if elements[i] > elements[i+1]:
                tmp = elements[i]
                elements[i] = elements[i+1]
                elements[i+1] = tmp
                swapped = True
        if not swapped:
            break
            


if __name__ == "__main__":
    elements = [5,9,2,1,67,34,88,34]
    BubbleSort(elements)
    print(elements)