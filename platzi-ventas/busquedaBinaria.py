import random

def busquedaBinaria(lista,numero,inicio, fin):

  if inicio > fin:
    return False
  mid =  (fin + inicio) // 2

  if numero == lista[mid]:
    return True
  elif numero > lista[mid]:
    mid += 1
    inicio = mid
  else:
    mid -= 1
    fin = mid

  return busquedaBinaria(lista, numero, inicio, fin) 



if __name__ == '__main__':
  lista = [random.randint(0,10) for element in list(range(10)) ]
  lista.sort()
  print(lista)
  numero = input('inserta el numero a buscar')
  print(busquedaBinaria(lista, numero, 0, len(lista)-1))
