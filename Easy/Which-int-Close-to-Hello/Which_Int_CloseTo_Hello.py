# Clear the working environment
from IPython import get_ipython
get_ipython().magic('reset -sf')

import itertools

# Which Integer is closer to Hello

# Form the dictionary of alphabetical-letters to decimal digits

def Ascel_Func(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]
        
def subset(array,num):
    result = []
    def find(arr,num,path=()):
        if not arr:
            return
        if arr[0]==num:
            result.append(path+(arr[0],))
        else:
            find(arr[1:],num-arr[0],path+(arr[0],))
            find(arr[1:],num,path)
    find(array,num)
    return result
        
Letter_To_Digit_Dict={'a':1,'b':1,'c':1,'d':2,'e':2,'f':2,'g':3,'h':3,'i':3,'j':4,'k':4,'l':4,\
                 'm':5,'n':5,'o':5,'p':6,'q':6,'r':6,'s':7,'t':7,'u':7,'v':8,'w':8,'x':8,\
                 'y':9,'z':9,'A':1,'B':1,'C':1,'D':2,'E':2,'F':2,'G':3,'H':3,'I':3,'J':4,'K':4,'L':4,\
                 'M':5,'N':5,'O':5,'P':6,'Q':6,'R':6,'S':7,'T':7,'U':7,'V':8,'W':8,'X':8,\
                 'Y':9,'Z':9}

Digit_To_Letter_Dict={1:('a', 'b', 'c'), 2:('d', 'e', 'f'), 3:('g', 'h', 'i'), \
                      4:('j', 'k', 'l'), 5:('m', 'n', 'o'), 6:('p', 'q', 'r'), \
                      7:('s', 't', 'u'), 8:('v', 'w', 'x'), 9:('y', 'z')}

# Generate all partitions of intgers from 1 to 10 in reverse lexicographic order

Int_Partitions=[]
for n in range(1,11):
    P=Ascel_Func(n)
    X=list(P)
    Int_Partitions.append(X)
    
Word=input("Enter the word to be checked for its closeness to integers from 1 to 10")

Word=Word.lower()

# Determine the list of digits in the input number
Digit_List=[]
for i in range(len(Word)):
    Digit_List.append(Letter_To_Digit_Dict[Word[i]])
    
# Partition the word into its bigrams 
Word_Bigrams_List=[]
i=1
while i < len(Word):
    Word_Bigrams_List.append(Word[i-1:i+1])
    i=i+1

# Find all subsets of List of Digits such that: the sum of digits is equal to the
# the specified integer and the number of digits in the subset is maximum

Subsets_List=[]

for n in range(1,11):  
    Subsets_Sum_n=subset(Digit_List,n)
    # Find the longest subsets and store in Subsets List
    if Subsets_Sum_n==[]:
        Subsets_List.append([])
    else:
        Subsets_List.append(Subsets_Sum_n)

#Max_Subset_Length=0
#for i in range(len(Subsets_List)):
#    for j in range(len(Subsets_List[i])):
#        if len(Subsets_List[i][j]) > Max_Subset_Length:
#            Max_Subset_Length=len(Subsets_List[i][j])
#
#for i in range(len(Subsets_List)):
#    Temp=list(Subsets_List[i])
#    for j in range(len(Subsets_List[i])):
#        if len(Subsets_List[i][j]) < Max_Subset_Length:
#            Temp.remove(Subsets_List[i][j])
#    Subsets_List[i]=Temp    

# Form all words corresponding maximum-length subsets and compute similarity



Words_And_SimList=[]            
for i in range(len(Subsets_List)):
    for j in range(len(Subsets_List[i])):
        if len(Subsets_List[i][j]) != 0:
            # compute all words of this subset
            Char_Sets=[]
            for k in Subsets_List[i][j]:
                Char_Sets.append(Digit_To_Letter_Dict[k])
            Words=list(itertools.product(*Char_Sets))
            for AWord in Words:
                Bigrams_List=[]
                for k in range(1,len(AWord)):
                    Bigrams_List.append(AWord[k-1]+AWord[k])
                    if len(Bigrams_List) > len(Word_Bigrams_List):
                        Bigrams_InterSect=set(Bigrams_List).intersection(Word_Bigrams_List)
                    else:
                        Bigrams_InterSect=set(Word_Bigrams_List).intersection(Bigrams_List)
                    SimDice=2*len(Bigrams_InterSect)/(len(Bigrams_List)+len(Word_Bigrams_List))
                    Words_And_SimList.append([AWord,SimDice])
    
WordsAndSimilarities=[]    
for i in Words_And_SimList:
    WordString=""
    for j in i[0]:
        WordString=WordString+j
    WordsAndSimilarities.append((WordString,i[1]))
        
Max_Score=max([j[1] for j in WordsAndSimilarities])

Words_with_MaxScore=[j for j in WordsAndSimilarities if j[1]==Max_Score]

for i in Words_with_MaxScore:
    Digit_Comp=[]
    for j in range(len(i[0])):
        Digit_Comp.append(Letter_To_Digit_Dict[i[0][j]])
        
    print("(Word:"+i[0]+" Dice Coeff. Value:" "%0.3f" % i[1],"from composition:",tuple(Digit_Comp))
            







    
    
    
    

