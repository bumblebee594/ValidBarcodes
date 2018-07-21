import json,re
from pprint import pprint

with open('kiranaData.json') as f:
    data = json.load(f)

dataSet=set()
count=0
for key in data:
    key=key.replace(' ','')
    if len(key)!=13:count+=1
    dataSet.add(key)
print(len(dataSet),count)

def digitSum(n):
    ans=0
    while(n>0):
        ans=ans+(n%10)
        n=n//10
    return ans

l=""
for c in "ĽᝢႮ⏿ዿၮ∉᜝Ꮺൢ៫ǋẜ᳼╭᛭ᰡඡᆸߡⓞ᠜ȍ῏᪆":
    l+="%04d"%ord(c)
#print(l)
#Damm Algo using regex
def Damm(b):#Source CodeGolf for God knows what input
    a="0"
    for i in b:
        a=l[10*int(a)+int(i)]
    return b+a

print(Damm('04462013'+'6'))
print(Damm('30126440'+'7'))
input()    
#mentioned Algo will fail on 10% of more complex errors
def DammAlgo(code):
    matrix=(
    (0, 3, 1, 7, 5, 9, 8, 6, 4, 2),
    (7, 0, 9, 2, 1, 5, 4, 8, 6, 3),
    (4, 2, 0, 6, 8, 7, 1, 3, 5, 9),
    (1, 7, 5, 0, 9, 8, 3, 4, 2, 6),
    (6, 1, 2, 3, 0, 4, 5, 9, 7, 8),
    (3, 6, 7, 4, 2, 0, 9, 5, 8, 1),
    (5, 8, 6, 9, 7, 2, 0, 1, 3, 4),
    (8, 9, 4, 5, 3, 6, 2, 0, 1, 7),
    (9, 4, 3, 8, 6, 1, 7, 2, 0, 5),
    (2, 5, 8, 1, 4, 3, 6, 7, 9, 0)
    )
    row=0
    for d in code:
        row=matrix[row][int(d)]
    #print(row)
    return matrix[row][row]==0
#number=input()
#print(DammAlgo(number))

true,false=0,0
TrueV,FalseV=[],[]
total,notLen13=0,0
for key in set(data):
    total+=1
    key=re.sub("\D","",key)
    if(len(key)!=13):
        notLen13+=1
        print('{0}=>{1}(using Damm Algo)'.format(key,False))
        false+=1
        
    else:
        x=key[-1]
        y=Damm(key[:len(key)])
        if(x==y[-1]):
            true+=1
            TrueV.append(key)
        else:
            false+=1
            FalseV.append(key)
        print('{0}=>{1}(using Damm Algo)'.format(key,x==y[-1]))
           
#print('true=>{0},false=>{1}'.format(true,false))#660,6010
#print('{0}=>total,{1}=>Notlen13(using Damm Algo)'.format(total,notLen13))#6670,370

x=input()


dTable = (
    (0,1,2,3,4,5,6,7,8,9),
    (1,2,3,4,0,6,7,8,9,5),
    (2,3,4,0,1,7,8,9,5,6),
    (3,4,0,1,2,8,9,5,6,7),
    (4,0,1,2,3,9,5,6,7,8),
    (5,9,8,7,6,0,4,3,2,1),
    (6,5,9,8,7,1,0,4,3,2),
    (7,6,5,9,8,2,1,0,4,3),
    (8,7,6,5,9,3,2,1,0,4),
    (9,8,7,6,5,4,3,2,1,0))
pTable = (
    (0,1,2,3,4,5,6,7,8,9),
    (1,5,7,6,2,8,3,0,9,4),
    (5,8,0,3,7,9,6,1,4,2),
    (8,9,1,6,0,4,3,5,2,7),
    (9,4,5,3,1,2,6,8,7,0),
    (4,2,8,6,5,7,3,9,0,1),
    (2,7,9,3,8,0,6,4,1,5),
    (7,0,4,6,9,1,3,2,5,8))
invTable = (0,4,3,2,1,5,6,7,8,9)

def calcsum(number):
    """For a given number returns a Verhoeff checksum digit"""
    c = 0
    for i, item in enumerate(reversed(str(number))):
        c = dTable[c][pTable[(i+1)%8][int(item)]]
    return invTable[c]

def checksum(number):
    """For a given number generates a Verhoeff digit and
    returns number + digit"""
    c = 0
    for i, item in enumerate(reversed(str(number))):
        c = dTable[c][pTable[i % 8][int(item)]]
    return c

def generateVerhoeff(number):
    return number+str(calcsum(number))

# Some tests and also usage examples
assert calcsum('75872') == 2
assert checksum('758722') == 0
assert calcsum('12345') == 1
assert checksum('123451') == 0
assert calcsum('142857') == 0
assert checksum('1428570') == 0
assert calcsum('123456789012') == 0
assert checksum('1234567890120') == 0
assert calcsum('8473643095483728456789') == 2
assert checksum('84736430954837284567892') == 0
assert generateVerhoeff('12345') == '123451'


def VerhoeffAlgo(code):
    code=(generateVerhoeff(code))
    return checksum(code)==0
    
print(VerhoeffAlgo(str(236)))

#def LuhnModNAlgo():#supports non-numerical string
    
    
def LuhnAlgorithmChecker(accountNo):#mod 10 algo to validate credit card nos.,IMEI nos, National Provider IDs in US,Canadian Social Insurance No.,Israel ID ,Greek Social Security
    #will not detect transposition error of 09<=>90
    #not detect 3 twin errors 22<=>55,33<=>66,44<=>77
    #not a crytographically secure hash function
    lastDigit,sumTotal=int(accountNo[-1]),0
    #accidental errors not malicious attacks(mistyped or otherwise incorrect no.)

    lenBar=len(accountNo)-1#including check digit
    #works with systems that use zero padding 
    for i in range(lenBar):
        
        if (i%2==1):sumTotal+=digitSum(2*int(accountNo[i]))
        #OR 2*num-9
        else:sumTotal+=int(accountNo[i])
            
    #print(sumTotal)
    unitDigit=sumTotal%10
    #print(unitDigit)
    checkDigit=10-unitDigit
    return checkDigit==lastDigit

a=str(79927398710)

print(LuhnAlgorithmChecker(a))
        
def isValidISBN10Barcode(barcode):#uses variable(i+1) weighting and modulo 11  
    x=len(barcode)#detects all single digit substitution and transposition errors(jump transpositions)
    checkSum,oddTotal,evenTotal=0,0,0

    lastDigit=int(barcode[-i])
    for i in range(x-1):
        if(i%2==0):oddTotal+=((i+1)*int(barcode[i]))
        
        else:evenTotal+=((i+1)*int(barcode[i]))
        
    checkSum=11-((evenTotal+oddTotal)%11)
    
    checkSum=checkSum%11
    return  checkSum==lastDigit


#Also for ISBN13 GS1 Algorithm
def isValidEAN13Barcode(barcode):#use 13 weighting system for EAN8 and
    #31 for EAN 13(does not rectify 10% of transposition errors) 3*(a+d)-
    lastDigit=int(barcode[-1])#weights=>3-1 or 1-3=>even number so does not catch transpositions of 2 digits differ by 5
    checkSum,oddTotal,evenTotal=0,0,0
    #barcode=str('0')+barcode+str('0')
    for i in range(len(barcode)-1):
        if(i%2==0):evenTotal+=int(barcode[i])
        else:oddTotal+=int(barcode[i])
    #if(x==8):
     #   evenTotal=3*evenTotal
    #error due to 3*(c)+d-(3*(d)+c)=2*(c-d)=(0)mod(10) So, if c=0,1,2,3,4 and d=1,6,7,8,9.
    oddTotal=3*oddTotal
    checkSum=(10-((evenTotal+oddTotal)%10))%10
    return checkSum==lastDigit

total,Notlen13=0,0
data1=[]

for key in data:
    data1.append(key)
data1=set(data1)
falsy,truthy,TruthyV,FalsyV=0,0,[],[]
for key in (data1):
    total+=1
    key=key.replace(' ','')
    if(len(key)!=13):
        print('{0}=>{1}(using EAN Algo)'.format(key,False))
        falsy+=1
        Notlen13+=1
        
    else:
        if isValidEAN13Barcode(key):
            truthy+=1
            TruthyV.append(key)
        else:
            FalsyV.append(key)
            falsy+=1
        print('{0}=>{1}(using EAN Algo)'.format(key,isValidEAN13Barcode(key)))
    
print('{0}=>total,{1}=>Notlen13(using EAN Algo)'.format(total,Notlen13))#6670,377
print('{0}=>truthy,{1}=>falsy'.format(truthy,falsy))#1095,5575

#print(len(set(TruthyV)-set(TrueV)),len(set(FalsyV)-set(FalseV)))
#print('TruthyV=>{0}'.format(set(TruthyV)))
print('FalsyyV=>{0}'.format(set(FalsyV)))

#print('TrueV=>{0}'.format(set(TrueV)))
#print('FalseV=>{0}'.format(set(FalseV)))
barcode=input()

lenBarCode=len(barcode)

for i in range(lenBarCode):
    if(math.isnan(float(barcode[i]))):#not a valid upc or ean
        exit(print(False))
        
if lenBarCode==8 or lenBarCode==13:
    exit(print(isValidEAN13And8Barcode(barcode)))
    
#if lenbarCode==18:
    #return #EAN13-code weighting

#def isValidBarcode(barcode):
 #   x=len(barcode)
    #if(x<8 or x>18 or (x!=8 and x!=12 and x!=13 and x!=14 and x!=18)):
     #   return False


    

    
    
