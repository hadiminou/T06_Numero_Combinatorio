from combinatoria import*
print("\nNumero combinatorio")
num=int(input("teclea el numerador "))
den=int(input("teclea el dominador "))
if den>num:
    print("el numerador es mas pequeno que el denominador")
else:
    print(num,"sobre",den,"es",numero_combinatoria(num,den))