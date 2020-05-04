# obfus...obusfi...obfuscation!
by @EugeneFronzak, reverse, 150

Смотрим на исходники, и понимаем, что это просто обфусцированный код на python.

Разбираем код по кусочкам, и получаем примерно [исходник](private/obfuscation.py)

Разбираемся как работал шифр: сдвиг по ASCII в зависимости от условий. Если быть повнимательней, то можно понять, что достаточно поменять пару знаков, и мы полчим код, который дешифрует сообщение:

```python
flag = '_~`jdkQ3,gKR;11,,G](STe#4=e [L;"'

result = ''.join([chr(ord(flag[i]) - i + 20) if i % 2 ==
                  0 else chr(ord(flag[i]) + i - 10) for i in range(len(flag))])
print(result)
```

Флаг: `surctf_08fUSC4710N_1S_c00L_1S_17`