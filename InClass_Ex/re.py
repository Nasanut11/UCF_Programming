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
zipcode1 = "12345"
zipcode2 = "12345-6789"
x = re.search("^\d{5}$", zipcode1)
y = re.search("^\d{5}(-\d{4})?$", zipcode2)
print(x, y)

#%%
import re
time1 = "5pm"
time2 = "5am"
time3 = "17:00"
x = re.search("^([1-9]|1[0-2])(:\d\d)?[ap]m?$", time1)
print(x)
 