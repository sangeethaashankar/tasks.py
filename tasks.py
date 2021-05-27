Word = str(input("Input a string ( Word ) :"))
n = len(Word)
x = []

for word in range(0,n):
    x.append(Word[word])

My_set = set(x) # converting it to a set to get the unique variables
List = list(My_set)# converting it back to control how the list is printed
print("The unique letters from this word are :", List)
m = len(List)
i = 0
for i in range(m - 1):
    # range(n) also work but outer loop will repeat one time more than needed.

    # Last i elements are already in place
    for j in range(0, m - i - 1):

        # traverse the array from 0 to n-i-1
        # Swap if the element found is greater
        # than the next element
        if x.count(List[j].lower()) < x.count(List[j+1].lower()):
            List[j], List[j + 1] = List[j + 1], List[j]


for i in range(0,m):
        print("" + List[i] + " = ", x.count(List[i].lower()))
