# -*- coding: utf-8 -*-

import numpy 


def getCountArr(arr):
    countArr = []
    for v in arr:
        countArr.append (len(v))
    return countArr

def getTheDividendAtIndex (index,arrCount,num):
    dividend = num;
    for i in range(index):
                        # print i,"除前:",dividend
        dividend = dividend / arrCount[i]
                        # print "除后:",dividend,arrCount[i]

    return dividend                                              

def getTheOneLoc (zArr,num): 
    arrCount = getCountArr(zArr)
    newArr = []
    for i in range(len(arrCount)):
        dividend = getTheDividendAtIndex (i,arrCount,num)
                        # print arrCount, '第',i,'个' ,':',arrCount[i],'-',dividend
        k = dividend%(arrCount[i])
        newArr.append(k)
    print '最终',newArr
    return newArr





def get_parameters(request):
    if request.method == 'GET' :   
        s = request.META['QUERY_STRING']   
        if len(s) != 0 :
            return dict([x.split('=',1) for x in s.split('&')])
    if request.method == 'POST':
        # result = str(result_list) 
        return request.POST



#类转成字典
def classToDict(obj):
    is_list = obj.__class__ == [].__class__
    is_set = obj.__class__ == set().__class__

    if is_list or is_set:
        obj_arr = []
        for o in obj:
            dict = {}
            dict.update(o.__dict__)
            obj_arr.append(dict)
        return obj_arr
    else:
        dict = {}
        dict.update(obj.__dict__)
        return dict


def dbClassListToList(c_name):
    class_list = numpy.array(c_name.objects.all())
    new_list = []
    for oc in class_list:
        nc = classToDict(oc)
        new_list.append(nc)
    return new_list


def get_dbvalue_list(class_name,attribute_name):
    ol = numpy.array(class_name.objects.all())
    nlist = []
    for olv in ol :
        v = getattr(olv, attribute_name)
        nlist.append (v)
    return nlist





