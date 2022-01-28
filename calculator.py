
from functools import partial

from tkinter import *


root= Tk()
txtVar= StringVar()
display=Label(root,textvariable=txtVar,width=0,height=5,borderwidth=1).grid(row=0,column=0,columnspan=3)

chain=""
operations=["+","-","/","*","="]
preVal=""

def enterVal(val):
    global chain,display,preVal,txtVar
    if not val == "=" :
        if val in operations:
            if not preVal in operations and not preVal=="":
                chain+=val
        else:
            chain+=val
        preVal=val
    else:
        chain=Calculate()
    print(chain)
    changeText(txtVar)
def changeText(txt):
    txt.set(chain)

def Calculate():
    #split
    ops=[]
    nums=[]
    firstSplit= chain.split("+")
    for char in chain:
        if char in ["+","-"]:
            ops.append(char)
    for num in firstSplit:
        temp = num.split("-")
        for val in temp:
            nums.append(val)
    tempOps=[]
    tempNums=[]

    for i in range(len(nums)):
        if not "/" in nums[i] and not "*" in nums[i]:
            tempNums.append(int(nums[i]))
        else:
            result=0
            tempN=""
            tempO=[]
            for char in nums[i]:
                if char in operations:
                    tempO.append(char)
                    tempN+=" "
                else:
                    tempN+=char
            tempN=tempN.split(" ")
            tempN= [int(x) for x in tempN]
            for i in range(len(tempN)):
                if i ==0:
                    result=tempN[i]
                else:
                    if tempO[i-1]=="/":
                        result/=tempN[i]
                    elif tempO[i-1]=="*":
                        result*=tempN[i]
            tempNums.append(result)
    result=0
    for i in range(len(tempNums)):
        if i==0:
            result=tempNums[i]
        else:
            if ops[i-1]=="+":
                result+=tempNums[i]
            elif ops[i-1]=="-":
                result-=tempNums[i]
    print(result)
    return result

numbers=[]
opButtons=[]

for i in range(10):
    if i ==0:
        numbers.append(Button(root,text=str(i), command=partial(enterVal,str(i)), padx=30,pady=30).grid(row=4,column=1))
    else:
        numbers.append(Button(root,text=str(i), command=partial(enterVal,str(i)), padx=30,pady=30).grid(row=1+(i-1)//3,column=(i-1)%3))
ct=0
for operation in operations:
    opButtons.append(Button(root,text=operation, command=partial(enterVal,operation), padx=30,pady=30).grid(row=1+ct,column=3))
    ct+=1
root.mainloop()