import simplejson
import unicodedata
import random

from datetime import datetime

names = [u'Marcos', u'João', u'Maria', u'Antônio', u'Tiago', u'Luciana', u'Lucas', u'Renata',
         u'Fátima', u'Cláudia']

def generate_email(name):
    return unicodedata.normaliza('NFKD', name).encode(
        'ascii', 'ignore').decode('ascii').strip().lower()

        
