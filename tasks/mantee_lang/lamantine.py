#-*- coding: utf-8 -*-
def encrypt(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] != ' ' and s[i] != '\n':
            s[i] = bin(ord(s[i]))[2:]
            s[i] = s[i].replace('1', 'Ы')
            s[i] = s[i].replace('0', 'И')
        s[i] = '{}~'.format(s[i])
    return ''.join(s)

def decrypt(s):
    s = s.replace('Ы', '1')
    s = s.replace('И', '0')
    s = s.split('~')
    s.pop()
    for i in range(len(s)):
        if s[i] != ' ' and s[i] != '\n':
            s[i] = chr(int(s[i], 2))
    return ''.join(s)