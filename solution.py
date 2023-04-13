import pandas as pd
import numpy as np
from scipy import stats


chat_id = 324151080 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы

    #res = stats.anderson_ksamp([x, y])
    res = stats.cramervonmises_2samp([x, y])
    #return res.statistic, res.critical_values, res.pvalue
    #return res.significance_level
    #return pval
    #if res.significance_level < 0.06:
    if res.pval < 0.06:
        return True
    else:
        return False
