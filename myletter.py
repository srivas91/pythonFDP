c=input('enter any character:')
d=''
if c.isupper():
    d=c.lower()
else:
    d=c
match d:
    case 'a'|'e'|'i'|'o'|'u':
        print('vowel')
        print('hello')
    case _:
        print('consonant')
