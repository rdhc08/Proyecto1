
def algoritmo1(a,n):
	i=0
	b=0

	while i<n:
		j=0
		while j<n:
			s=a[j]
			b=b+s*i
			while a[i]<a[j]:
				#print a
				#print a[i]
				#print a[j]
				t=a[j]
				a[j]=a[i]
				a[i]=t
				#print a
				#print "_____________________"

			j=j+1
		print a
		i=i+1
	print b

a1=[5,4,3,2,1]
a2=[1,2,3,4,5]
a4=[3,5,1,4,2]
a3=[6,3,9,4,7,2,1]

algoritmo1(a1,len(a1))
#algoritmo1(a1,len(a1))
#algoritmo1(a2,len(a2))
algoritmo1(a3,len(a3))