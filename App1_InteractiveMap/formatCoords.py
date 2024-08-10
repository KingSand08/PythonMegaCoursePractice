from decimal import Decimal
from deprecated import deprecated

@deprecated(version='0.4', reason="Not necessary anymore for API location coordinate managment.")
def extract_until_char(input_str, delimiter):
    if(input != None and delimiter != None):
        # Extract the substring up to and including the delimiter
        result = input_str[:input_str.find(delimiter)]
        # Update input_str to remove the extracted part
        input_str = input_str[(input_str.find(delimiter) + 1):]
    else:
        return ""    
    return (Decimal(result), input_str)

@deprecated(version='0.4', reason="Not necessary anymore for API location coordinate managment.")
def fixCoord(crd):
    crdStr = str(crd).replace(' ', '').replace('N', '').replace('E', '').replace('′', 'D').replace('(\"', '').replace('\",)', '').replace('(\'', '').replace('\',)', '').replace('(', '').replace(')', '').replace("\\", '').replace(",", '').replace('\'', 'D').replace('\"', 'R').replace("u200a", '').replace("\u200a", '').replace('xa0', '').replace('\xa0', '')
    if('–' in crdStr):
        numerator = extract_until_char(crdStr, '–')
        crdStr = numerator[1]
        denominator = extract_until_char(crdStr, '°')
        crdStr = denominator[1]
        definedCoord = (numerator[0] + denominator[0]) / 2
        if(crdStr != ''):
           if(crdStr[0] == 'S' or crdStr[0] == 'W'):
               definedCoord *= -1
        # print(definedCoord, end="")
        return definedCoord
    numerator = extract_until_char(crdStr, '°') 
    crdStr = numerator[1]
    if('D' in crdStr[0:3]):
        if("00D" in crdStr[0:3]):
            crdStr = crdStr[3:]
            definedCoord = numerator[0]
        else:
            denominator = extract_until_char(crdStr, 'D')
            crdStr = denominator[1]
            definedCoord = numerator[0] + (denominator[0] / 60)
    if('R' in crdStr[0:3]):
        denominator1 = extract_until_char(crdStr, 'R')
        crdStr = denominator1[1]
        definedCoord += (denominator1[0] / (60**2))
    else:
        definedCoord = numerator[0]
    if(crdStr[0] == 'S' or crdStr[0] == 'W'):
        definedCoord *= -1
        crdStr = crdStr[1:]
    if("to" in crdStr):
        crdStr = crdStr.replace("to", '')
        numerator = extract_until_char(crdStr, '°')
        crdStr = numerator[1]
        if('D' in crdStr):
            denominator = extract_until_char(crdStr, 'D')
            crdStr = denominator[1]
            to_definedCoord = numerator[0] + (denominator[0] / 60)
        else:
            to_definedCoord = numerator[0]
        if(crdStr != ''):
           if(crdStr[0] == 'S' or crdStr[0] == 'W'):
                to_definedCoord *= -1
                crdStr = crdStr[1:]
        finalCoordB = (definedCoord + to_definedCoord)
        finalCoord = finalCoordB / Decimal(2)
    # print(definedCoord, end="")
    return finalCoord
  