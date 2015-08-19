def numbered_lines():
	count = 1
	with open("small.txt", 'r') as fin:
		#file_lines = [''.join([str(count)," ",x.strip(),'\r\n']) for x in fin.readlines()]
		file_lines = ''
		for x in fin.readlines():
			file_lines = file_lines + ''.join([str(count)," ",x.strip(),'\r\n'])
			count += 1

	with open("small_new.txt", 'w') as fout:
		fout.writelines(file_lines)

def main():
	numbered_lines()

if __name__ == '__main__':
    main()
