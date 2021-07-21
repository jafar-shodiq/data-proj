#  Version: 2020.02.21
#
#  MIT License
#
#  Copyright (c) 2018 Jiankang Deng and Jia Guo
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import os
import argparse
import numpy as np
import mxnet as mx

parser = argparse.ArgumentParser(description='merge age and gender models')
# general
parser.add_argument('--age-model', default='', help='path to load age model.')
parser.add_argument('--gender-model', default='', help='path to load gender model.')
parser.add_argument('--prefix', default='', help='path to save model.')
args = parser.parse_args()

i = 0
tsym = None
targ = {}
taux = {}
for model in [args.age_model, args.gender_model]:
  _vec = model.split(',')
  assert len(_vec)==2
  prefix = _vec[0]
  epoch = int(_vec[1])
  print('loading',prefix, epoch)
  sym, arg_params, aux_params = mx.model.load_checkpoint(prefix, epoch)
  if tsym is None:
    all_layers = sym.get_internals()
    tsym = all_layers['fc1_output']
  if i==0:
    prefix = 'age'
  else:
    prefix = 'gender'
  for k,v in arg_params.iteritems():
    if k.startswith(prefix):
      print('arg', i, k)
      targ[k] = v
  for k,v in aux_params.iteritems():
    if k.startswith(prefix):
      print('aux', i, k)
      taux[k] = v
  i+=1
dellist = []
#for k,v in arg_params.iteritems():
#  if k.startswith('fc7'):
#    dellist.append(k)
for d in dellist:
  del targ[d]
mx.model.save_checkpoint(args.prefix, 0, tsym, targ, taux)

