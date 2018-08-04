#Sorting - Implement two types of sorting algorithms: Merge sort and
#bubble sort.

#Bubble Sorting
def sorting(entry):
    for j in range(len(entry)-1):
        for i in range(len(entry)-1):
            if entry[i] > entry[i+1]:
                entry[i], entry[i+1] = entry[i+1], entry[i]
                print (entry)
    #print(entry)


entry = [12,5,123,9,7,22,11,12,33,0,3]
if __name__ == "__main__":
    sorting(entry)
