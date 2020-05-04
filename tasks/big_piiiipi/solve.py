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
