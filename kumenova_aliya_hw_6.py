num = [34, 16, 78, 94, 67, 21]

def bubble_sort(num):
    for i in range(len(num)):
        for j in range(len(num) - i - 1):
            if num[j] > num[j + 1]:
                k = num[j]
                num[j]= num[j + 1]
                num[j+1] = k

    return num

print(bubble_sort(num))

def binary_search(list, val):
    N = len(list)
    ResultOk=False
    first=0
    last=N-1
    pos=-1
    while first<=last:
        middle=(first+last)//2
        if val==list[middle]:
            first=middle
            last=first
            ResultOk=True
            pos=middle
            break
        elif val>list[middle]:
            first=middle+1
        else:
            last= middle-1
    if ResultOk==True:
        print(f'Элемент найден под индексом {pos}')
    else:
        print('Элемент не найден')

numbers = [1,2,3,6,8,11,13,14]
binary_search(numbers,11)