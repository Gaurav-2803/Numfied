import os

clear=lambda:os.system("cls")                   #Clear_Fn
clear()

'''Color Functions'''
color_brwhite=lambda:os.system("color 0f")      #BrWhite_Color_Fn
color_red=lambda:os.system("color 0c")          #Red_Color_Fn
color_purple=lambda:os.system("color 0d")       #Purple_Color_Fn

'''Main'''
color_brwhite()
print("\t\t\t\t===========\n\t\t\t\t<|Numfied|>\n\t\t\t\t===========")
print("\nEg. xxx-xxx-xxxx")
num=input("Enter Number As Shown Above : ")
print("")
error=1
if len(num)!=12:
    print(error,"] Incorrect Format < Length Of Phone No. Must Be '12' Including Dash(-) >, Your Length : ",len(num))
    error+=1
for i in range(0,len(num)):
    if i!=3 and i!=7:
        if num[i].isdigit()==False:
            print(error,"] Incorrect Number < '",num[i],"' Must Not Present In Phone No. : ",num,"> At Postion :",i+1)
            error+=1
    else:
        if num[i]=='-':
            continue        
        else:
            print(error,"] Incorrect Format < '-' Must Present In Phone Number At Correct Positions >")
            error+=1
if error==1:
    color_purple()
    print("Correct No. < Phone No. Has 0 Error's >")      
else:
    color_red()
    print("\nSorry But Your Number Has '",error-1,"' Error's")      

input("\nHit Enter To Exit")    