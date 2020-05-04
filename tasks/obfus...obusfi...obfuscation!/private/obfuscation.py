
flag = ''

result = ''.join([chr(ord(flag[i]) + i - 20) if i % 2 ==
                  0 else chr(ord(flag[i]) - i + 10) for i in range(len(flag))])


print(result)
