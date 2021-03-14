def compress(s):
	ordvalue=["0"*(7-len(bin(ord(i))[2:]))+bin(ord(i))[2:] for i in s]
	key,remain,bgroup=[i[2:5] for i in ordvalue],[i[:2]+i[5:] for i in ordvalue],[]
	if len(remain)%2==1:bgroup.append("0000")
	for i in remain:bgroup.append(i)
	output="".join([chr(int(bgroup[i]+bgroup[i*2+1],2)) for i in range(len(bgroup)//2)])
	compvalue=hex(int("".join(key),2))[2:]
	return output,compvalue

while True:a=input();print(compress(a))