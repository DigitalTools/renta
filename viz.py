from renta import calc

def vizrenta():

  UIT = 4050
  monthly_base = 7000

  monthly_arr = []
  impuestos_arr = []
  netos = []
  for i in range(20):
    monthly = monthly_base + i*(500)
    monthly_arr.append(monthly)
    impuesto_mensual = calc(UIT, monthly + i*(100), 'prod')
    impuestos_arr.append(impuesto_mensual)
    netos.append(monthly-impuesto_mensual)
    #s = 'monthly: ' + str(monthly) + ' impuesto: ' + str(impuesto_mensual)
    #print(s)


  import matplotlib.pyplot as plt
  plt.plot(
    monthly_arr, monthly_arr, 'bs',
    monthly_arr, impuestos_arr, 'r--',
    monthly_arr, netos, 'g^'
  )
  plt.show()