# THIS CODE DETERMINES THE ENCODING TYPE OF THE CSV FILE
# import chardet
# with open("LANGUAGES.csv", 'rb') as rawdata:
#     result = chardet.detect(rawdata.read(100000))
#print(result)  		# Returns 'ISO-8859-1' as encoding type


#ADDS A NEW LANGUAGE TO LIST OF POPULAR LANGUAGES AND TRANSLATES
from translate import Translator
import pandas as pd
lang_frame = pd.read_csv("LANGUAGES.csv",encoding='ISO-8859-1')
langlist = lang_frame["Code"].tolist()  # DESIRED COLUMN TO A PYTHON LIST
popular = ['fr','ru','it','es','pt','ig','yo']
mylang = input("Enter new language code: ").lower()
if mylang in langlist:
     popular.append(mylang)
engtxt = open("englishtxt.txt").read()
print("----------------SEE TRANSLATIONS-------------------")
i = 0
while i < len(popular):
     t = Translator(from_lang='en',to_lang=popular[i])
     newlang = t.translate(engtxt)
     print(newlang)
     print('----------------------------------------------------------------------')
     i = i + 1
