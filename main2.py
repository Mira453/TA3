count1 = 0
count2 = 0

def median_of_three(arr, p, r):
    mid = (p + r) // 2
    a, b, c = arr[p], arr[mid], arr[r]
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    return b

def partition(arr, p, r):
    global count1
    x = arr[r] # опорний елемент
    i = p - 1  # індекс для менших елементів

    for j in range(p, r):
        count1 += 1
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

def partition_median(arr, p, r):
    global count2
     # Якщо підмасив містить 3 або менше елементи, сортуємо вручну
    if r - p <= 2:  
        if arr[p] > arr[r]:  
            arr[p], arr[r] = arr[r], arr[p]
            count2 += 1
        if r - p == 2:  # Якщо рівно 3 елементи
            if arr[p] > arr[p+1]:
                arr[p], arr[p+1] = arr[p+1], arr[p]
                count2 += 1
            if arr[p+1] > arr[r]:
                arr[p+1], arr[r] = arr[r], arr[p+1]
                count2 += 1
        return r  
    
    pivot = median_of_three(arr, p, r)
    i, j = p, r
    while True:
        while arr[i] < pivot:
            count2 += 1
            i += 1
        while arr[j] > pivot:
            count2 += 1
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

def quickSortSimple(arr, p, r):
    if p < r:
        index = partition(arr, p, r)
        quickSortSimple(arr, p, index - 1)
        quickSortSimple(arr, index + 1, r)

def quickSortMedian(arr, p, r):
    if r - p > 2:
        q = partition_median(arr, p, r)
        quickSortMedian(arr, p, q)
        quickSortMedian(arr, q + 1, r)
    else:
        global count2
        if r > p:
            count2 += 1
            if arr[p] > arr[r]:
                arr[p], arr[r] = arr[r], arr[p]

def main():
    global count1, count2
    input_file = input("введіть назву файлу: ")
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            array = file.read().splitlines()
            array.pop(0)
            array = [int(i) for i in array]
    except FileNotFoundError:
        print("помилка")
        return
    except ValueError:
        print("помилка. некоректні дані")
        return
    
    arr1 = array[:]
    arr2 = array[:]
    
    count1 = 0
    quickSortSimple(arr1, 0, len(arr1) - 1)
    
    count2 = 0
    quickSortMedian(arr2, 0, len(arr2) - 1)
    
    output_file = "output.txt"
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(f"{count1} {count2}\n")
    
if __name__ == "__main__":
    main()

