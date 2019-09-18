#%%
import random
verbs = ["runs","walks","milks","flys","climbs","swims"]
nouns = ["man","woman","ocean","cat","dog"]
names = ["Disney","Australia","Orlando","Wawa","Casablanca","Starbucks"]
adjectives = ["gargantuan","gaseous","hairy","damaged","baggy","bare","eager"]

print(random.choice(verbs))
print(random.choice(nouns))
print(random.choice(names))
print(random.choice(adjectives))

print("There was once a boy named" + random.choice(names) + ". He lived in the jungle, and his best friend was a" + random.choice(nouns) + ". He tried his hardest to impress his friend by learning how to run a python program, but unfortunately there were no" + random.choice(nouns) + "in the jungle. So," + random.choice(names) + "had to come up with a different idea of how to run his python program. He walked for days and days to the nearest lake," + random.choice(names) + ", to find a shop where he could buy a python." + random.choice(names) + "returned to the jungle to his friend the lobster with his new python. His friend looked at him and said, “I thought python was a computer program, not a" + random.choice(nouns) + ".")