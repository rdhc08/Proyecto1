import math

A = [9,8,7,6,5,4,3,2,1]		
B = [1,2,3,4,5,6,7,8,9]
i = 0						
n = 9


#print len(A)
#A[6] = 12
#print len(A)				
				
#print A

def insertionr_sort(s):
 	j = 1
 	while j < len(s):
  		i = j-1
  		key = s[j]
  		while i >= 0 and s[i] > key:
  			s[i+1] = s[i]
  			i = i-1
  		s[i+1] = key
  		j = j+1


def insertionr_sort1(s):
 	j = 1
 	while j < len(s):
  		i = j-1
  		key = s[j]
  		while i >= 0 and s[i] < key:
  			s[i+1] = s[i]
  			i = i-1
  		s[i+1] = key
  		j = j+1

insertionr_sort(A)
insertionr_sort1(B)
#print A
#print B

def search(a,v):
	j = 1
	while a[j] != v:
		j = j+1
	if a[j] == v:
		return j + 1
	else :
		return -1

def sumatorio(i,n):
	s=0;
	while i<=n :
		s=s+(i*i)+4
		i=i+1;
	return s

Alf  = ['A','B','C','D','E','F','G','H','I','J', 'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
Al1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

def cesar(a):
	i = 0;
	while i < len(a):
		b=a[i]
		a[i] = a[((i+3) % 26)]
		a[(i+3)%26] = b  
		i = i+1
	return a


#print cesar(Alf)


#print 5%25



def algoritmo1(a,n):
	i=0
	b=0

	#Contadores
	d1=0

	while i<n:
		j=0
		while j<n:
			s=a[j]
			b=b+s*i
			d1=d1+1
			while a[i] < a[j]:
				t=a[j]
				a[j]=a[i]
				a[i]=t
		  	j=j+1
		i=i+1
	print d1
	print b

a = [1,2,3,4,5,6,7,8,9]
n=9

#algoritmo1(a,n)
				

	
def algorito4(n):
	i=1
	c=0#contador pata linea 7
	while i<=n:
		k=i
		while k<=n:
			k=k+2
		k=1
		
		while k<=i :
			c=c+1 #Veces validas 
			k=k+1
		i=i+2
		c=c+1#Valores de salida  Salida 
	print c 

#algorito4(9)


def algortimo5(n):
	i=1
	c=0 #contador linea128
	while i<=n:
		k=i
		
		while k<=n:
			c=c+1
			k=k+2
		k=1
		c=c+1
		while k<=1:
			k=k+1
		i=2*i
	#c=c+1
	print c




def linea(n):
	print (math.ceil(n/2))+1+((math.floor(math.log(n,2)))*((math.floor(n/2))+2))-(math.pow(2,(math.floor(math.log(n,2))))-1)


algortimo5(4)

linea(4)
	
print math.floor(math.log(6,2))










