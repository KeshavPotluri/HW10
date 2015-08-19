def len_list(s):
	count = 0
	for item in s:
		count+=1
	return count

def main():
	a = "abcd"
	b = ["a","b","c"]
	c = {"A":"a", "B":"b"}
	d = ("a",1,"elephant","z")

	print len_list(a)
	print len_list(b)
	print len_list(c)
	print len_list(d)

if __name__ == '__main__':
    main()
