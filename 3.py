# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 22:06:58 2022

@author: Vinod
"""

import pandas as pd

lst1 = [{"id": 1, "x": "one"}, {"id": 2, "x": "two"}]
lst2 = [{"id": 2, "x": "two"}, {"id": 3, "x": "three"}]

lst1_ds = pd.DataFrame(lst1)
lst2_ds = pd.DataFrame(lst2)
lst_concat_ds = pd.concat([lst1_ds, lst2_ds])
lst_grouped_res_ds = lst_concat_ds.groupby(["id", "x"]).agg(sum)
print(lst_grouped_res_ds.reset_index().to_dict('records'))

