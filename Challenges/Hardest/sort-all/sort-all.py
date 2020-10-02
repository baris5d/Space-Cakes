'''
Version : 3.5.0
Creator : Baris Dede
'''

def sub_lists(arr,l): 
  
    sublist = [] 
      
    for i in range(l + 1): 
          
        for j in range(i + 1, l + 1): 
              
            sub = arr[i:j] 
            sublist.append(sub) 
    return sublist

# For find distinct values
def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 


def f(values):
    arr = sub_lists(values, len(values))
    total_sum = 0
    # First loop 
    for i in range(0,len(arr)):
        arr[i] = Remove(arr[i])
        # Second loop
        for key, v in enumerate(arr[i], start=1):
            total_sum = total_sum + (key * v)
    return total_sum
        

f_size = int(input())
f_values = list(map(int,input().split()))
#if len(f_values) > f_size:
 #   print("Array size greater than entered size.")

#elif len(f_values) < f_size:
 #   print("Array size less than entered size")

#else:
f_values.sort()
print(f(f_values))
