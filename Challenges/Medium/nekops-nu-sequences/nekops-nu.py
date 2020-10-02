def subs(seq):
    output = []

    number = seq[0]
    instances = 1

    for i in range(1,len(seq)):
        if seq[i] == number:
            instances += 1
        else:
            output.append(instances)
            output.append(number)
            number = seq[i]
            instances = 1
        output.append(instances)
        output.append(number)

    return output

  
def join_ints(int_list):
    joined_str = ""
    for i in int_list:
        joined_str = joined_str + str(i) + " "
    return joined_str[:-1]

def print_seq(nekops_str, pad_len):
    extra_dot = pad_len-len(nekops_str)
    if extra_dot < 0:
        extra_dot = 0
        
    n_dots_right = extra_dot // 2
    n_dots_left = extra_dot - n_dots_right
    
    dots_left = ""
    
    for i in range(n_dots_left):
        dots_left = dots_left + "."


    mid_str = dots_left + nekops_str

    dots_right = ""
    for i in range(n_dots_right):
        dots_right = dots_right + "."    
    
    out_str = mid_str + dots_right
    print(out_str)


def main():
    line = input().split()
    n_exec =  int(line[0])

    N = []
    for x in line[1:]:
        N.append(int(x))
    cp_seq = [N]
    cp_str = [join_ints(N)]

    lengths_seq = [0]
    lengths_str = [len(join_ints(N))]
    for i in range(1, n_exec+1):
        s = subs(cp_seq[i-1]) 
        
        cp_seq.append(s)
        lengths_seq.append(len(s))
        
        s_str = join_ints(s)
        cp_str.append(s_str)
        lengths_str.append(len(s_str)) 

    max_len_seq = max(lengths_seq)
    max_len_str = max(lengths_str)


    for seq in cp_str:
        print_seq(seq,max_len_str)

    print(max_len_seq)


if __name__== "__main__":
    main()

