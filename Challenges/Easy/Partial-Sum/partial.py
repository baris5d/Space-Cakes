'''
Version : 3.5.0
Creator : Baris Dede
'''
import sys

n = int(input())

partial_sum = 0

for i in range(n):
    number = int(input())
    partial_sum += number
    print(partial_sum)
    sys.stdout.flush()
	