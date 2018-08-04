#Sorting - Implement two types of sorting algorithms: Merge sort and
#bubble sort.

#Merge Sorting
def sorting(entry):
    if len(entry) > 1:
        left=entry[0:int(len(entry)/2)]
        right=entry[int(len(entry)/2):]

        sorting(left)
        sorting(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                entry[k]=left[i]
                i=i+1
            else:
                entry[k]=right[j]
                j=j+1
            k=k+1
        while i < len(left):
            entry[k]=left[i]
            i=i+1
            k=k+1
        while j < len(right):
            entry[k]=right[j]
            j=j+1
            k=k+1

    print(entry)


entry = [12,5,123,9,7,22,11]
if __name__ == "__main__":
    sorting(entry)
