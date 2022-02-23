def calcular_pagamento(horas, valor_hora):
    horas = float(horas)
    taxa = float(valor_hora)
    if horas <= 40:
        salario=horas*taxa
    else:
        hora_extra = horas - 40
        salario = 40*taxa+(hora_extra*(1.3*taxa))
    return salario

calcular_pagamento(50, 6)  

def pagamentoSemanal(horas, valordahora):
  pagamentoSemanal= horas*valordaHora
  return pagamentoSemanal

horas = float(input('Horas trabalhadas:'))
valordaHora = float(input('Valor hora trabalhada:'))
pagamentoSemanal(horas, valordaHora)
