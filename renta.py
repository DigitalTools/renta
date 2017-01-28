import logging

def calc(UIT, monthly):

  utilidades = 0
  renta_bruta = monthly * 14 + utilidades
  
  s = 'renta bruta: ' + str(renta_bruta)
  logging.debug(s)
  
  total_renta = renta_bruta - 7*UIT
  
  s = 'total renta: ' + str(total_renta)
  logging.debug(s)

  factors = [ 5, 20, 35, 45 ]
  taxes = [ 8, 14, 17, 20, 30 ]

  subtotal = total_renta

  factor_range = range(len(factors)) 

  topes = []
  for i in range(len(factors)) :
    factor = factors[i]
    topes.append( factor * UIT )

  #s = 'topes: ' + str(topes)
  #print(s)

  diffs = [topes[0]]
  for i in range(1,len(topes)) :
    diffs.append(topes[i]-topes[i-1])

  #s = 'diffs: ' + str(diffs)
  #print(s)

  total_impuesto_arr = []

  for diff in diffs :
    if subtotal > diff:
      total_impuesto_arr.append(diff)
      subtotal = subtotal - diff
    else:
      total_impuesto_arr.append(subtotal)
      break

  if subtotal > 0:
    total_impuesto_arr.append(subtotal)

  #s = 'total renta arr: ' + str(total_impuesto_arr)
  #print(s)

  impuesto_arr = []
  for i in range(len(total_impuesto_arr)):
    impuesto_arr.append ( total_impuesto_arr[i] * taxes[i]/100 )

  #s = 'impuesto_arr: ' + str(impuesto_arr)
  #print(s)

  impuesto_anual = 0
  for tramo_impuesto in impuesto_arr:
    impuesto_anual = impuesto_anual + tramo_impuesto

  #s = 'impuesto_anual: ' + str(impuesto_anual)
  #print(s)

  impuesto_mensual = impuesto_anual/12
  #s = 'impuesto mensual: ' + str(impuesto_mensual)
  #print(s)

  return impuesto_mensual
