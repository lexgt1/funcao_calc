def calc(num, num1, ope):
    if ope == 1:
        resultado = num + num1
        return resultado
    elif ope == 2:
        resultado = num - num1
        return resultado
    elif ope == 3:
        resultado = num * num1
        return resultado
    elif ope == 4:
        if num1 != 0: 
            resultado = num / num1
            return resultado
        else:
            return "Deu ruim: Não se divide por zero"
    else:
        return "Operação inválida"
        print ("Resultado:", resultado)