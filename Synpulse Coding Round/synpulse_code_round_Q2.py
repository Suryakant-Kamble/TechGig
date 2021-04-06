"""
Palindrome String (50 Marks)
Given a string, find the longest substring which is palindrome.

Note: The string can consists of space, lowercase alphabets and uppercase alphabets


Input Format
The only line of input consists of a string, S.

Constraints
1<= |S| <=50

Output Format
Print the longest palindrome substring.

Sample TestCase 1
Input
GOOGLE

Output
GOOG

"""


def substr(param, l, h):
    for i in range(l, h + 1):
        print(param[i], end="")


def main(para):
    n = len(para)
    maxlen = 1
    start = 0
    for i in range(n):
        for j in range(i, n):
            flag = 1
            for k in range(0, ((j - i) // 2) + 1):
                if (para[i + k] != para[j - k]):
                    flag = 0
            if (flag != 0 and (j - i + 1) > maxlen):
                start = i
                maxlen = j - i + 1
    substr(para, start, start + maxlen - 1)


if __name__ == '__main__':
    i_str = input()
    if 1 <= len(i_str) <= 50:
        main(i_str)
