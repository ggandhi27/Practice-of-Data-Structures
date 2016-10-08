import os
import subprocess
from os.path import exists

def dir(dr):
	dr.strip()
#	os.system("clear")
	cwd=os.getcwd()
	os.chdir(dr)
	os.system("ls -l >lis")
	fi=open("lis")
	for x in fi:
		a=[m for m in x.strip().split(' ')]
		l=len(a)
		strng=a[l-1]
		if x[0]=='d':
			if exists(strng):
				dir(strng)
		elif x[0]=='-':
			if strng.find(".pdf")==-1 and exists(strng):
				c=0
				f=open(strng)
				for d in f :
					c=c+1
					if(d.find("main(")!=-1):
						print("Directory : %s|\tLine no : %d|\t File : %s"%(dr,c,strng))
	os.system("rm lis")
	os.chdir(cwd)
	return

n=raw_input("Enter the name of the directory : ")
if exists(n):
	dir(n)
else:
	print("Invalid Name ")
