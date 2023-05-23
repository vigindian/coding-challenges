#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'avgRotorSpeed' function below.
#
# URL for cut and paste
# https://jsonmock.hackerrank.com/api/iot_devices/search?status={statusQuery}&page={number}
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING statusQuery
#  2. INTEGER parentId
#

#web calls
import requests

def avgRotorSpeed(statusQuery, parentId):
    # define api-url
    apiUrl="https://jsonmock.hackerrank.com/api/iot_devices/"
    #get api-results from given values
    getResp=requests.get(apiUrl+"?status="+statusQuery+"&parentId="+str(parentId))
    getRespJson=getResp.json()
    totalPages=getRespJson["total_pages"]
    
    #define default values - will increment if we find parent-id in results
    totalParentMatch=0
    avgRotorSpeedAccumulate=0
    
    #ensure we go through all pages
    totalPagesRange = totalPages + 1
    #start from page 1
    for pageNumber in range (1, totalPagesRange):
        getRespPage=requests.get(apiUrl+"?status="+statusQuery+"&parentId="+str(parentId)+"&page="+str(pageNumber))
        getRespPageJson=getRespPage.json()
        #extract what we need
        dataOp=getRespPageJson["data"]
        #debug
        #print(dataOp)
     
        #let's iterate
        for i in range (len(dataOp)):    
            #print (dataOp[i])
            #if parent present
            if "parent" in dataOp[i]:
                parentValue=dataOp[i]["parent"]
                #print(parentValue)
                #ensure not None
                if parentValue is not None:
                    #extract parent-id
                    parentValueId=parentValue["id"]
                    if parentValueId is not None:
                        #print(str(parentValueId)+" is not none")
                        if parentValueId == parentId:
                          #print(str(parentValueId)+" same as "+ str(parentId))
                          #increment to use it for average calc
                          totalParentMatch += 1
                          #increment to with existing value
                          avgRotorSpeedAccumulate += int(dataOp[i]["operatingParams"]["rotorSpeed"])
                          #print(totalParentMatch)
                          #print(avgRotorSpeedAccumulate)
        #else:
        #    print(str(i)+" has no parentId")
    
    #outside-loop
    #print("totalParentMatch: " +str(totalParentMatch))
    #print("avgRotorSpeedAccumulate: " + str(avgRotorSpeedAccumulate))
    if avgRotorSpeedAccumulate == 0:
        avgRotorSpeedValue=avgRotorSpeedAccumulate
        #print(avgRotorSpeedAccumulate)
    else:
        avgRotorSpeedValue=int(avgRotorSpeedAccumulate/totalParentMatch)
        #print(avgRotorSpeedValue)
            
    return(avgRotorSpeedValue)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    statusQuery = input()

    parentId = int(input().strip())

    result = avgRotorSpeed(statusQuery, parentId)

    fptr.write(str(result) + '\n')

    fptr.close()
