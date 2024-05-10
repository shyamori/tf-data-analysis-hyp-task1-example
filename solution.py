import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest


chat_id = 386300009 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha=0.05
    return proportions_ztest([y_success, x_success], [y_cnt, x_cnt], alternative="larger")[1] < alpha
