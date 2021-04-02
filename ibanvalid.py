import csv






def withoutfile():
    pyletter_dic = {"AL": 28, "AD": 24, "AT": 20, "AZ": 28, "BH": 22, "BY": 28, "BE": 16, "BA": 20, "BR": 29, "BG": 22,
                "CR": 22, "HR": 21, "CY": 28, "CZ": 24, "DK": 18, "DO": 28, "TL": 23, "EG": 29, "SV": 28, "EE": 20,
                "FO": 18, "FI": 18, "FR": 27, "GE": 22, "DE": 22, "GI": 23, "GR": 27, "GL": 18, "GT": 28, "HU": 28,
                "IS": 26, "IQ": 23, "IE": 2, "IL": 23, "IT": 27, "JO": 30, "KZ": 20, "XK": 20, "KW": 30, "LV": 21,
                "LB": 28, "LY": 25, "LI": 21, "LT": 20, "LU": 20, "MK": 19, "MT": 31, "MR": 27, "MU": 30, "MC": 27,
                "MD": 24, "ME": 22, "NL": 18, "NO": 15, "PK": 24, "PS": 29, "PL": 28, "PT": 25, "QA": 29, "RO": 24,
                "LC": 32, "SM": 27, "ST": 25, "SA": 24, "RS": 22, "SC": 31, "SK": 24, "SI": 19, "ES": 24, "SE": 24,
                "CH": 21, "TN": 24, "TR": 26, "UA": 29, "AE": 23, "GB": 22, "VA": 22, "VG": 24, "A": 10, "B": 11,
                "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "I": 18, "J": 19, "K": 20, "L": 21, "M": 22,
                "N": 23, "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29, "U": 30, "V": 31, "W": 32, "X": 33,
                "Y": 34, "Z": 35}
# bank_name = {"SEB": "LT1", "BANK2": "LT5", "BANK1": "LT6"}
bank_name = {"LT2":"SEB", "LT5":"BANK2", "LT6":"BANK1"}


def withoutfile():
    iban = input("Enter iban: ")
    # filepath = input('Enter output csv filepath: ')
    #filepath = 'C:\\Users\\Žymantas\\Desktop\\valid16.csv'
    #with open(user_input, "r") as f:
    #lines = f.read().splitlines()
    valids = []
    banks = []
    #for i in lines:
      #  print(f'processing {i}')
    if iban[:2] not in pyletter_dic and len(iban)==pyletter_dic.get(iban[:2]):
        #print('Character check failed, skipping Digit check')
        #print("Digit check failed. IBAN is not valid!")
        valids.append([iban, False])
        banks.append([iban, bank_name.get(iban[:3], '')])
        #continue
    iban = iban.replace(' ','')
    final = iban[4:] + iban[:4]
    temp = ''
    for letter in final:
        temp += str(pyletter_dic.get(letter, letter))
        #print(temp)
        modulo = int(temp) % 97
        if modulo == 1:
            #print("Digit check passed. IBAN is be valid!")
            valids.append([iban, True])
            banks.append([iban, bank_name.get(iban[:3], ';;')])
            #print(iban,banks,valids)
        else:
            #print(modulo)
            #print("Digit check failed. IBAN is not valid!")
            valids.append([iban,False])
            banks.append([iban, bank_name.get(iban[:3], ';;')])
            #print(iban,banks, valids)
    print("IBAN bank name", banks[1])  
    print("IBAN validation status", valids[-1])      
   
   
   








pyletter_dic = {"AL": 28, "AD": 24, "AT": 20, "AZ": 28, "BH": 22, "BY": 28, "BE": 16, "BA": 20, "BR": 29, "BG": 22,
                "CR": 22, "HR": 21, "CY": 28, "CZ": 24, "DK": 18, "DO": 28, "TL": 23, "EG": 29, "SV": 28, "EE": 20,
                "FO": 18, "FI": 18, "FR": 27, "GE": 22, "DE": 22, "GI": 23, "GR": 27, "GL": 18, "GT": 28, "HU": 28,
                "IS": 26, "IQ": 23, "IE": 2, "IL": 23, "IT": 27, "JO": 30, "KZ": 20, "XK": 20, "KW": 30, "LV": 21,
                "LB": 28, "LY": 25, "LI": 21, "LT": 20, "LU": 20, "MK": 19, "MT": 31, "MR": 27, "MU": 30, "MC": 27,
                "MD": 24, "ME": 22, "NL": 18, "NO": 15, "PK": 24, "PS": 29, "PL": 28, "PT": 25, "QA": 29, "RO": 24,
                "LC": 32, "SM": 27, "ST": 25, "SA": 24, "RS": 22, "SC": 31, "SK": 24, "SI": 19, "ES": 24, "SE": 24,
                "CH": 21, "TN": 24, "TR": 26, "UA": 29, "AE": 23, "GB": 22, "VA": 22, "VG": 24, "A": 10, "B": 11,
                "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "I": 18, "J": 19, "K": 20, "L": 21, "M": 22,
                "N": 23, "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29, "U": 30, "V": 31, "W": 32, "X": 33,
                "Y": 34, "Z": 35}
# bank_name = {"SEB": "LT1", "BANK2": "LT5", "BANK1": "LT6"}
bank_name = {"LT2":"SEB", "LT5":"BANK2", "LT6":"BANK1"}


def withfile():
    user_input = input("Enter path: ")
    # filepath = input('Enter output csv filepath: ')
    #filepath = 'C:\\Users\\Žymantas\\Desktop\\valid16.csv'
    with open(user_input, "r") as f:
        lines = f.read().splitlines()
        valids = []
        banks = []
        for i in lines:
            print(f'processing {i}')
            if i[:2] not in pyletter_dic and len(i)==pyletter_dic.get(i[:2]):
                #print('Character check failed, skipping Digit check')
                #print("Digit check failed. IBAN is not valid!")
                valids.append([i, False])
                banks.append([i, bank_name.get(i[:3], '')])
                continue
            i = i.replace(' ','')
            final = i[4:] + i[:4]
            temp = ''
            for letter in final:
                temp += str(pyletter_dic.get(letter, letter))
            print(temp)
            modulo = int(temp) % 97
            if modulo == 1:
                #print("Digit check passed. IBAN  is valid!")
                valids.append([i, True])
                banks.append([i, bank_name.get(i[:3], '')])
            else:
                #print(modulo)
                #print("Digit check failed. IBAN is not valid!")
                valids.append([i,False])
                banks.append([i, bank_name.get(i[:3], '')])

    file = open('C:\\Users\\Žymantas\\Desktop\\valid100.csv', 'w',newline='')
    csvw = csv.writer(file, delimiter=',')
    csvw.writerows(valids)
    file.close()

    file = open('C:\\Users\\Žymantas\\Desktop\\bank100.csv', 'w',newline='')
    csvw = csv.writer(file, delimiter=',')
    csvw.writerows(banks)
    file.close()





user_input=input("Input 1 for user input or input 2 for file input")
if user_input=="1":
    withoutfile()
elif user_input=="2":
    withfile()
else:
    exit()