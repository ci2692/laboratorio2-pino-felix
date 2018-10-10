# Sorts.py
# Autor: Luis Pino (15-11138) y Félix Arnos (15-10088)
# Descripcion: Implementacion de los algoritmos InsertionSort y MergeSort
import sys 
# Ordenamiento por inserción
def InsertionSort(A:list,P:int,R:int):
    for j in range (P+1,R):
        key=A[j]  #Elemento a Insertar
        i=j-1
        while (i>=P and A[i]>key):
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    return(A)

#Ordenamiento por unión
def Mergesort(arreglo:list, p:int , r:int ):
	if p < r :
		q = (p+r)//2  #q es la mitad del arreglo 
		Mergesort(arreglo, p, q) #Se realiza mergesort desde el primer elemento p hasta la mitad del arreglo q
		Mergesort(arreglo, q+1, r) #Se realiza mergesort desde el elemento q+1 haasta el ultimo elemento r
		Merge(arreglo, p, q, r) #Intercala los elementos que se dividieron 
<<<<<<< HEAD
	return(Merge(arreglo,p,q,r))
#Funcion Merge
def Merge(arreglo, p, q, r):
=======
	return(arreglo)

def Merge(arreglo:list, p:int, q:int, r:int):
>>>>>>> d70e920d669b3c65987c780a6351b1e54f1ed8e4
	i,j=0,0 # Variables de incremento 
	resultado=[] #Lista del arreglo final 
	n = q-p+1   #Tamaño de arreglo[p...q]
	m = r-q   #Tamaño de arreglo[q+1...r]
	L = arreglo[n]
	R = arreglo[m]
	for i  in range(0,len(L)):
		L[i] = arreglo[p+i-1]
	for i  in range(0,len(R)):
		R[i] = arreglo[q+i]
	L[n+1],R[m+1] = sys.maxint #Sentinelas 
	for k in range(p,r):
		if L[i]<=R[j]:
			arreglo[k]=L[i] #Remover primero de L 
			i=i+1
		else:
			arreglo[k]=R[j] #Remover primero de R
			j=j+1
<<<<<<< HEAD
	
=======
    return arreglo
>>>>>>> d70e920d669b3c65987c780a6351b1e54f1ed8e4
