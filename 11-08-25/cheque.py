resultado = ''
unidade = ' reais'
numeros = ['zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze', 'quinze','dezesseis','dezessete','dezoito','dezenove']
dezenas = ['vinte','trinta','quarenta','cinquenta','sessenta','setenta','oitenta','noventa']


def icheque(money):
    if (money == 1):
        return 'Um real'
    elif (money < 20):
        resultado = numeros[money]
    else:
        resultado = dezenas[money/10 - 2]
        if (money%10 != 0):
            resultado += " e " + numeros[money%10]

    return resultado + unidade

def fcheque(money):
    money = round(100*money)
    imoney = int(money)
    resultado = ''
    
    if (imoney == 1):
        return 'um centavo'
    elif (imoney < 20):
        resultado = numeros[imoney]
    else:
        resultado = dezenas[imoney/10 - 2]
        if (imoney%10 != 0):
            resultado += " e " + numeros[imoney%10]

    return resultado + ' centavos'

def cheque(money):
    imoney = int(money)
    fmoney = money - imoney
    resultado = ''
    
    if (imoney > 0):
        resultado += icheque(imoney)
    if (fmoney > 0):
        if (imoney > 0):
            resultado += " e "
        resultado += fcheque(fmoney)
    
    return resultado.capitalize()
    
