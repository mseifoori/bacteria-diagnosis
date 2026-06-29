import numpy as np
import pandas as pd

from bacteria_lists import enterobacteriaceae_bacteria, nfb_bacteria, gram_positive_bacteria


enterobacteriaceae_bacteria_tests = pd.DataFrame({
    'Oxidase': ['-', '-', '-', '-', '-',
                '-', '-', '-', '-', '-',
                '-', '-', '-', '-', '-',
                '-', '-', '-'],
    'TSI': ['A/A', 'K/A', 'K/A', 'A/A', 'A/A',
            'A/A', 'A/A', 'K/A', 'A/A', 'K/A',
            'K/A', 'K/A', 'K/A', 'K/A', 'K/A',
            'K/A', 'A/A or K/A', 'A/A'],
    'OF': 'F+',
    'Urease': ['-', '-', '-', '+', '-',
               '-', '-', '+', '+', '+',
               '+', '-', '-', '-', '-',
               '-', '-', '-'],
    'PD': ['-', '-', '-', '-', '-',
               '-', '-', '+', '+', '+',
               '+', '-', '-', '-', '-',
               '-', '-', '-'],
    'IMViC': ['++--',
              '++--',
              '-+--',
              '--++',
              '+-++',
              '--++',
              '--++',
              '-+vv',
              '++vv',
              '++vv',
              '++vv',
              '-+vv',
              '-+vv',
              '-+vv',
              '-+vv',
              '++-+',
              '-+-+',
              '++++'],
    'Motility': ['+', '+', '-', '-', '-',
                 '+', '+', '+', '+', '+',
                 '+', '+', '+', '+', '+',
                 '+', '+', '+'],
    'H2S': ['-', '-', '-', '-', '-',
            '-', '-', '+', '+', '+',
            '-', '+', '-', '+', '+',
            '+', '+', '-'],
    'LDC': ['+', '+', '-', 'NI', 'NI',
            'NI', 'NI', 'NI', 'NI', 'NI',
            'NI', '+', '+', '+', '+',
            '+', '-', '-'],
    'ONPG': ['NI', '+', '-', 'NI', 'NI',
             'NI', '-', 'NI', 'NI', 'NI',
             'NI', 'NI', 'NI', 'NI', 'NI',
             'NI', '+', '+']
}, index=enterobacteriaceae_bacteria)

enterobacteriaceae_bacteria_tests.index.name = 'Bacteria'

nfb_bacteria_tests = pd.DataFrame({
    'Oxidase': ['+', '+', '+', '+', '+',
                '+', '-', '-', '-', '-'],
    'TSI': 'K/K',
    'OF': ['O+', 'NR', 'O+', 'NR', 'NR',
           'O+', 'O+', 'NR', 'O+', 'NR'],
    'Urease': '-',
    'PD': '-',
    'IMViC': ['-+v+',
              '-+v+',
              '++v-',
              '-+v-',
              '-+v-',
              '-+v-',
              '-+vv',
              '-+vv',
              '-+v+',
              '-+v+'],
    'Motility': ['+', '+', '-', '-', '-',
                 '+', '-', '-', '+', '-'],
    'H2S': ['-', '-', '-', '-', '-',
            '+', '-', '-', '-', '-'],
    'LDC': 'NI',
    'ONPG': 'NI'
}, index=nfb_bacteria)

nfb_bacteria_tests.loc['Burkholderia cepacia', 'LDC'] = '+'
nfb_bacteria_tests.loc['Stenotrophomonas maltophilia', 'LDC'] = '+'

nfb_bacteria_tests.index.name = 'Bacteria'

gram_negative_bacteria_chart = pd.concat([enterobacteriaceae_bacteria_tests, nfb_bacteria_tests])


