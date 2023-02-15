'''
The first line contains .
 The second line contains an array   of  integers each separated by a space.

ex : 
5
2 3 6 6 5

op:
5

Find the Runner-Up Score! (it means second highes person)
'''


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(set(arr), reverse=True)[1])
    