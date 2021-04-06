""""
Q.1) First Day (50 Marks)
It is Rajeev's first day at Synpulse and he has been given a scenario to code.
The scenario is as follows:
Given an integer array, find the output array such that the elements at each index of the output array are the product
of all the numbers in the input array except itself.



Input Format
The first line of input consists of number of elements in the array, N.
The second line of input consists of the N space-separated integers Ai.

Constraints
1<= N <=50
-100<= Ai <=100


Output Format
Print the output array space-separately.

Sample TestCase 1
Input
5
3 6 8 4 7
Output
1344 672 504 1008 576


Explanation
6 * 8 * 4 * 7 = 1344

3 * 8 * 4 * 7 = 672
3 * 6 * 4 * 7 = 504
3 * 6 * 8 * 7 = 1008
3 * 6 * 8 * 4 = 576

"""




def main(param):
    n =len(param)
    l = [0]* n
    r = [0]* n
    l[0] = 1
    for i in range(1,n):
        l[i]= param[i-1]*l[i-1]
    r[n-1] = 1
    for j in reversed(range(n-1)):
        r[j] = param[j+1] *r[j+1]
    for i in range(n):
        param[i] = l[i] * r[i]


if __name__=='__main__':
    lst = []
    num = int(input())
    i_lst = input()
    spt_lst = i_lst.split()
    if num == len(spt_lst):
        for tlst in range(len(spt_lst)):
            lst.append(int(spt_lst[tlst]))
    main(lst)
    for inlst in lst:
        print(inlst, end=" ")


