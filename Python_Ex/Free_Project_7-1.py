#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)


#%%
from random import choice

subjects = ['SUM ', 'ASSOCIATE ', 'SEE ', 'MOSQUE ', 'FORT ', 'IMAGE ',
            'WINDOW ', 'TOWN ', 'SPIRE ', 'AGRICULTURALIST ', 'PASSAGE ', 'FRIEND ', 'NIGHT ',
            'HOME ', 'TABLE ', 'WORKER ', 'SWORD ', 'SHEILD ', 'MAN ', 'WOMAN ']
predicates = ['OPEN', 'QUIET', 'STRENGTH', 'GREAT', 'NARROW', 'CLOSE',
              'NEW', 'JUMP', 'FAR', 'DEEP', 'LATE', 'DARK', 'FREE',
              'LARGE', 'OLD', 'ANGRY']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'HIS', 'HERS', 'MY', 'MINE']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A MAN':
        text = 'AN WOMAN'
    return text

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

