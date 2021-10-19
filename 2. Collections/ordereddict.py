from collections import OrderedDict

#Working of Normal Dict

normalDict = {}
normalDict['a'] = 1
normalDict['b'] = 2
normalDict['c'] = 3
normalDict['d'] = 4

# for key,pair in normalDict.items():
#     print(key + ":" + str(pair))

ordrdDict = OrderedDict()
ordrdDict['a'] = 1
ordrdDict['b'] = 2
ordrdDict['c'] = 3
ordrdDict['d'] = 4

# for key,pair in ordrdDict.items():
#     print(key + ":" + str(pair))

#If value of a certain key is changed, the position is maintained
ordrdDict['c'] = 5
# for key,pair in ordrdDict.items():
#     print(key + ":" + str(pair))

#deleting and reinserting

ordrdDict.pop('c')

ordrdDict['c'] =21

for key,pair in ordrdDict.items():
    print(key + ":" + str(pair))
