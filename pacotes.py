def entrada():
    numeros=[]
    i=0
    while i<2:
        numeros.append(float(input("Digite o número: ")))
        i=i+1
    return numeros

def subtrai_and_quad(x:float,y:float):
    sub=x-y
    return sub**2

