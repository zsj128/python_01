"""import my_calc as m
import showtime as s
from my_calc import multiply
print("1 + 2 =",m.add(1,2))
print("2 × 3 =",multiply(2,3))
print("圆周率近似为:",m.PI)"""

import random_code as rc
import showtime as st
import sys
print("生成六位的随机验证码为:",rc.random_code())
f1,f2=st.show_time()
print("时间格式化:",f1)
print(sys.path)