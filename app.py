#from viz import vizrenta

#vizrenta()

import logging
from renta import calc

def main():

    logging.basicConfig(level=logging.INFO)
    logging.info('Started')

    UIT = 4050
    monthly = 7000
    impuesto_mensual = calc(UIT, monthly)
    logging.debug('impuesto_mensual: ' + str(impuesto_mensual))

    logging.info('Finished')

if __name__ == '__main__':
    main()