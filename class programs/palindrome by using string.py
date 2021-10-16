#its normal and simple
'''s='abccba'
print('palindrome' if s==s[::-1] else 'no')'''

s='abccba'
x=''
for k in s:
    x+=k
print('yes' if x==s else 'no')

str='abba'
rev=''.join(reversed(str))
print('yes' if rev==str else 'no')


#type2
def isPalindrome(str):
	# Run loop from 0 to len/2
	for i in range(0, int(len(str)/2)):
		if str[i] != str[len(str)-i-1]:
                 return False
	return True

# main function
s = "bhargav" 
ans = isPalindrome(s)
print('yes' if ans else 'no')