count = 0
def partition(arr,p, r):
    global count
    x = arr[r] #опорний елемент
    i = p-1#індекс для менших елементів

    for j in range(p,r):
        count+= 1
        if arr[j] <= x:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i+1]
    return i+1

def quickSortSimple(arr, p, r):
    if p < r:
        index = partition(arr,p, r)
        quickSortSimple(arr,p, index -1)
        quickSortSimple(arr, index +1, r)


def main():
    global count
    input_file = input("введіть назву файлу: ")
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            array = file.read().splitlines()
            array.pop(0)
            array =  [int(i) for i in array]
    except FileNotFoundError:
        print("помилка")
        return
    except ValueError:
        print("помилка. некоректні дані")
        return
    count = 0
    quickSortSimple(array, 0, len(array) - 1)
    print("відсортований масив:", array)
    print("кількість порівнянь:", count)

    output_file = "output.txt"
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(f"відсортований масив: {array}\n")
        file.write(f"кількість порівнянь: {count}\n")
if __name__ == "__main__":
    main()