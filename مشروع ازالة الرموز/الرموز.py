import string
str_ = string.punctuation
USER = input(' ﺔﻠﻤﺠﻟﺍ ﻞﺧﺩ ﺖﺤﻤﺳﻮﻟ\n')
new_str = ''
for x in USER:
    if x not in str_:
        new_str += x
print(f"({new_str})  ﻞﻳﺪﻌﺘﻟﺍ ﺪﻌﺑ ﺔﻠﻤﺠﻟﺍ ﻩﺬﻫ")
