import zipfile, os

FLAG = 'surctf_whow_i_cry_but_i_solved_it'
RICK = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
DORA = 'https://www.youtube.com/watch?v=SBCw4_XgouA'

with open('flag.txt', 'w') as f:
	f.write(FLAG + '\n\n' + DORA)

with open('rick', 'w') as f:
	f.write(RICK)

with zipfile.ZipFile('flag1.zip', 'w') as nzip:
	nzip.write('flag.txt')

n = 2500
for i in range(n):
	if i % 2 != 0:
		to_op = 'flag1.zip'
		to_wr = 'flag0.zip'
	else:
		to_op = 'flag0.zip'
		to_wr = 'flag1.zip'

	print(n, i+1)
	if n == i+1:
		to_op = 'flag.zip'

	with zipfile.ZipFile(to_op, 'w') as f:
			f.write(to_wr, 'flag.zip')
			f.write('rick', 'flag.txt')

os.remove('flag1.zip')
os.remove('flag0.zip')
os.remove('flag.txt')
os.remove('rick')
