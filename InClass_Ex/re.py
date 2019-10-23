#%%

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

#%%
import re
txt = "aaaaabaaa"
x = re.search("a*", txt)
print(x)
 
#%%
import re
zipcode1 = "\d + \d + \d + \d + \d"
zipcode2 = "\d + \d + \d + \d + \d + \d + \d +\d +\d"
x = re.search("\d", zipcode1)
x = re.search("\d", zipcode2)
print(x)