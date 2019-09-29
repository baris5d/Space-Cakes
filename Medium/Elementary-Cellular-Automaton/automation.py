N=8
datas=input()
data_list=datas.split()
R=int(data_list[0])
iterating=int(data_list[1])
tam=int(data_list[2])
seq=int(data_list[3])

n=1
def obtain_bit(number,pos):
        bit=(number&pow(2,pos))>>pos
        return bit

def rule_translation(rules,buff):
    for i in range(N):
        buff_rules=rules[i]>>1
        if buff_rules==buff:
            return obtain_bit(rules[i],0)

def create_rules(N_rules):
    rules=[]            
    for i in range(N):
        bit=obtain_bit(R,i)
        element=(i<<1)|(bit)
        rules.append(element)
    return rules
def icon_translation(seq,tam):
    chain="-"
    for i in range(tam-1,-1,-1):    
        if obtain_bit(seq,i)==1:
            chain=chain+'*'
        else:
            chain=chain+' '
    chain=chain+'-'
    return chain


def create_seq(seq,tam):    
    rules=create_rules(R)
    seq_n=0
    
    for i in range(tam-1,-1,-1):
        
        n_bit3=i+1
        n_bit2=i
        n_bit1=i-1
        
        if n_bit3==tam+1:
            bit3=0
        else:
            bit3=obtain_bit(seq,i+1)    
    
        if n_bit1 == -1:
            bit1=0 
        else:
            bit1=obtain_bit(seq,i-1)
            
        bit2=obtain_bit(seq,i)
        
        buff=(bit3<<2)|(bit2<<1)|bit1 
        seq_inter=rule_translation(rules,buff)<<i 
        seq_n=seq_n|(seq_inter) 
    return seq_n


stable=False
while n<=iterating and stable==False:
    seq_n=create_seq(seq,tam)
    chain= icon_translation(seq,tam)

    if seq==seq_n: 
        stable=True
    else:
        number=str(n)
        print(number.ljust(3," ")+' '+chain)
        seq=seq_n
    
        n=n+1