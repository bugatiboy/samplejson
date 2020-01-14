import json
from pandas.io.json import json_normalize
import flatten_json as fj

#Function for denormalize
def fj(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


#Load Json file
with open("sample_api_output.json") as f:
    js=json.load(f)

#parse and print on screen
xx = json.dumps(js, indent=2)
print(xx)

##Write denormalized output to flatfile.out
with open("flatfile.out", "w") as wr:
   ##wr.write(json_normalize(js, 'schoolDistrict', ['address', 'city', 'medianHouseValue', 'zip'], errors='ignore').to_string())
   for addr in js:
        wr.write(json_normalize(fj(addr)).to_string())


