# Я не плачу - это просто лук: Write-up

### Первое
Читаем условие, понимаем что вложенных архивов больше 1337 и ручками здесь решить не получится.
Гуглим как можно с помощью ЯП автоматически распаковывать архивы, например на python.

### Второе
Находим библиотеку [zipfile](https://docs.python.org/3/library/zipfile.html)(либо любую другую), читаем как ей пользоваться. Поняв всё что нужно, пишем скрипт.

Например такой:
```python3
# python3.7
import zipfile, shutil

c = 1

with zipfile.ZipFile('flag.zip', 'r') as f:
    f.extract('flag.zip', 'flag%s' % c)

while True:
    try:
        with zipfile.ZipFile('flag%s/flag.zip' % c, 'r') as f:
            c += 1
            f.extract('flag.zip', 'flag%s' % c)
    except KeyError:
        break
```
~~(осторожно много папок)~~

### Третье
Запускаем скрипт, распаковываем до последнего архива в котором будет лежать flag.txt. 

Флаг: `surctf_whow_i_cry_but_i_solved_it`

> Архив генерировался с помощью [generate.py](generate.py)
