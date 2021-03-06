# -*- coding: utf-8 -*-
"""AWGN_params.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16MsUTmwD-WpoNjjk-pK2lolhW4GiEsVE
"""

critic_params = {
    'dim': 1,
    'layers': 4,
    'embed_dim': 32,
    'hidden_dim': 64,
    'activation': 'relu',
    'ref_batch_factor': 10,
    'learning_rate': 0.00002
}

nit_params = {'dim': 1,
              'layers': 5,
              'hidden_dim': 64,
              'activation': 'relu',
              'tx_power': 1.0,
              'learning_rate': 0.0001,
              'peak_amp': None }