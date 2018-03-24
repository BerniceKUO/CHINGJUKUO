'''
這是一家餐廳,有三類餐點(義大利麵/比薩/濃湯)供顧客自助選餐
'''

import easygui
#計算價錢
def getprice(choices,pList):
    for choicesvar in pList:
       if choicesvar[0]==choices:
           return choicesvar[1]
        

#計算分數*金額

def getHMprice(pList):
    total=0
    for choices in pList:
        
        if choices[1]  is not None and choices[2] is not None:
            total= total+(int(choices[1])*int(choices[2]))
         
    return total
#取出項目
def getitem(pList):
    item=""
    for choices in pList:
         if choices[0] is not None and choices[1] is not None:
             item= item+(choices[0])+(str(choices[1]))+"份"+"\n"
    return item


#取出定價檔
def getPriceFile(filename):
    file=open(filename,"r")
    lines=file.readlines()
    file.close()
    price_list=[]
    for entry in lines:
        price=entry.split(',')
        price_list.append([price[0],int(price[1])])
    return price_list



#取出定價
義大利麵List=getPriceFile("pricepasta.txt")
比薩List=getPriceFile("pricepizza.txt")
濃湯List=getPriceFile("pricesoup.txt")






#義大利麵
#組合方式 [選項,幾份,價錢]
義大利麵flag=1;
顧客選項義大利麵=[]

while 義大利麵flag==1:
  
    義大利麵=easygui.choicebox(msg="請選擇義大利麵?",choices=["義大利肉醬麵","蛤利義大利麵","白醬義大利麵"])
    
    義大利麵幾份=easygui.integerbox(msg=str(義大利麵)+"要幾份?")
     
   
    顧客選項義大利麵Var=list(顧客選項義大利麵)
    #判斷選擇的義大利麵是不是己存在,存在就取代掉
    
    if len(顧客選項義大利麵)>0:
        i=0
        for 找義大利麵index,找義大利麵var in enumerate(顧客選項義大利麵Var):
            
            if 義大利麵==找義大利麵var[0]:
                #取代原本的義大利麵位置
                顧客選項義大利麵[找義大利麵index]=[義大利麵,義大利麵幾份, getprice(義大利麵,義大利麵List)]
                break
            else:
                #找到最後了確定沒有才加
                if(找義大利麵index==len(顧客選項義大利麵Var)-1):
                   顧客選項義大利麵.append([義大利麵,義大利麵幾份, getprice(義大利麵,義大利麵List)])
                
    else:
        顧客選項義大利麵.append([義大利麵,義大利麵幾份, getprice(義大利麵,義大利麵List)])
         
    義大利麵flag=easygui.ynbox("還要加點義大利麵嗎?")

print("最後輸出",顧客選項義大利麵)

#比薩


比薩flag=1;
顧客選項比薩=[]

while 比薩flag==1:
  
    比薩=easygui.choicebox(msg="請選擇比薩?",choices=["招牌比薩","海鮮比薩","雞肉比薩"])
    比薩幾份=easygui.integerbox(msg=str(比薩)+"要幾份?")
    顧客選項比薩Var=list(顧客選項比薩)
    #判斷選擇的比薩是不是己存在,存在就取代掉
    
    if len(顧客選項比薩)>0:
        i=0
        for 找比薩index,找比薩var in enumerate(顧客選項比薩Var):
            
            if 比薩==找比薩var[0]:
                #取代原本的比薩位置
                顧客選項比薩[找比薩index]=[比薩,比薩幾份, getprice(比薩,比薩List)]
                break
            else:
                #找到最後了確定沒有才加
                if(找比薩index==len(顧客選項比薩Var)-1):
                   顧客選項比薩.append([比薩,比薩幾份, getprice(比薩,比薩List)])
                
    else:
        顧客選項比薩.append([比薩,比薩幾份, getprice(比薩,比薩List)])
         
    比薩flag=easygui.ynbox("還要加點比薩嗎?")

print("最後輸出",顧客選項比薩)

#濃湯
濃湯flag=1;
顧客選項濃湯=[]

while 濃湯flag==1:
  
    濃湯=easygui.choicebox(msg="請選擇濃湯?",choices=["玉米濃湯","巧達濃湯","火腿玉米濃湯"])
    濃湯幾份=easygui.integerbox(msg=str(濃湯)+"濃湯要幾份?")
    顧客選項濃湯Var=list(顧客選項濃湯)
    #判斷選擇的濃湯是不是己存在,存在就取代掉
    
    if len(顧客選項濃湯)>0:
        i=0
        for 找濃湯index,找濃湯var in enumerate(顧客選項濃湯Var):
            
            if 濃湯==找濃湯var[0]:
                #取代原本的濃湯位置
                顧客選項濃湯[找濃湯index]=[濃湯,濃湯幾份, getprice(濃湯,濃湯List)]
                break
            else:
                #找到最後了確定沒有才加
                if(找濃湯index==len(顧客選項濃湯Var)-1):
                   顧客選項濃湯.append([濃湯,濃湯幾份, getprice(濃湯,濃湯List)])
                
    else:
        顧客選項濃湯.append([濃湯,濃湯幾份, getprice(濃湯,濃湯List)])
         
    濃湯flag=easygui.ynbox("還要加點濃湯嗎?")

print("最後輸出",顧客選項濃湯)
#組合方式 [選項,幾份,價錢]

結帳flag=easygui.ynbox(msg="要為您結帳嗎?",choices=('結帳', '不買了'))
if(結帳flag):
    easygui.msgbox("您總共點了"+"\n"+str(getitem(顧客選項義大利麵))+str(getitem(顧客選項比薩))+str(getitem(顧客選項濃湯))+"總共"+str(getHMprice(顧客選項義大利麵)+getHMprice(顧客選項濃湯)+getHMprice(顧客選項比薩))+"元")
else:
    easygui.msgbox("謝謝光臨!!")






