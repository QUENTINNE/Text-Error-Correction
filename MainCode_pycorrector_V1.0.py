# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 18:31
# @Author  : QUENTINNE
# @File    : main.py
# @Software: PyCharm

from pycorrector import Corrector
import os

pwd_path = os.path.abspath(os.path.dirname(__file__))
lm_path = os.path.join(pwd_path, './people_chars_lm.klm')
model = Corrector(language_model_path=lm_path)

corrected_sent, detail = model.correct('效国不是特别好')
print(corrected_sent, detail)