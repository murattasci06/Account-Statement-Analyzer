#Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import fitz 
import io
import streamlit as st
from playsound import playsound
import time
import warnings
warnings.filterwarnings("ignore")

    
def login():
   
    st.caption('Streamlit Version:  v1.7.0')
    st.markdown('<style>div[class="css-1vg7lpk e16nr0p30"] {height:25px;width:21%;margin-left:-46%;margin-top:-12%;  text-align: center;color: black; background:white; font-size: 80%; border:1px solid gray; border-radius: 9px; }</style>', unsafe_allow_html=True)
    
    #Streamlit Section for Login Interface
    #background settings
    st.markdown("""<style>.stApp {background: url("https://wallpaper.dog/large/990621.jpg");background-size: cover;}</style>""",unsafe_allow_html=True)
    
    #header settings
    st.markdown("<h1  style='text-align:center;color:black; top:-200px; text-shadow: 2px 2px white;   font-size:275%;  font-family:Arial; width:730px;'>Welcome to the App</h1>", unsafe_allow_html=True)
    path_input_0 = st.text_input(
        "File Path:","Please enter the path to the folder containing the Abstract_Account_Web_App.py file")

  
    #title and base-input settings
    st.markdown("""
    <style>
    .stTextInput > label {
    text-shadow: 2px 2px #3EADCD;
    box-shadow: 0px 7px #ABE9CD;
    font-size:123%;
    font-weight:bold;
    color:white;
    background:linear-gradient(to bottom,#BDD4E7  0%,#8693AB 100%);
    border: 2px;
    border-radius: 3px;
    margin-bottom:15px;
    }
    
    [data-baseweb="base-input"]{
    background:white;
    border: 2px;
    border-radius: 3px;
    
    }
    
    input[class]{
    font-weight: bold;
    font-size:100%;
    color: rgb(109, 105, 104,.6);
    font-style: italic;
    }
    </style>
    """, unsafe_allow_html=True)
    

 

    # interface codes for the login screen
    if st.button("PROCEED"):
              
                st.session_state["page"] = "main"
                st.session_state["PATH_INPUT_LAST"] = path_input_0
                st.experimental_rerun()
              
    #proceed button settings          
    st.markdown("""<style>
                div.stButton > button:first-child
                { margin-left: 64%; width:250px; height:46px;font-weight : bold;border: 3px solid #4BFFA3;border-radius:9px; background-color:black; color:white; transition: all 0.3s ease 0s; cursor: pointer;}
                div.stButton > button:hover {border: 3px solid #4BFFA3;border-radius:9px; background-color:black;color:white;  box-shadow: 0px 15px 20px rgba(75,255,163, 0.7);
                transform: translateY(-10px);text-weight: bold;} </style>"""
                , unsafe_allow_html=True)
    
    
    hide_st_style =" <style>footer {visibility: hidden;}</style>"
    st.markdown(hide_st_style, unsafe_allow_html=True) 
 
min_gift_money_info1=""
min_purchasing_gift1=""
spending_for_min_gift1=""

min_gift_money_info2=""
min_purchasing_gift2=""
spending_for_min_gift2=""

min_gift_money_info3=""
min_purchasing_gift3=""
spending_for_min_gift3=""

min_gift_money_info4=""
min_purchasing_gift4=""
spending_for_min_gift4=""

min_gift_money_info5=""
min_purchasing_gift5=""
spending_for_min_gift5=""

min_gift_money_info6=""
min_purchasing_gift6=""
spending_for_min_gift6=""



def main(): 
    global min_gift_money_info1
    global min_purchasing_gift1
    global spending_for_min_gift1
    
    
    global min_gift_money_info2
    global min_purchasing_gift2
    global spending_for_min_gift2
    
    
    global min_gift_money_info3
    global min_purchasing_gift3
    global spending_for_min_gift3
    
    global min_gift_money_info4
    global min_purchasing_gift4
    global spending_for_min_gift4
    
    global min_gift_money_info5
    global min_purchasing_gift5
    global spending_for_min_gift5
    
    global min_gift_money_info6
    global min_purchasing_gift6
    global spending_for_min_gift6


    global list
    if 'PATH_INPUT_LAST' in st.session_state:
       
        file0 = st.session_state["PATH_INPUT_LAST"]+"/Bankomat Alışveriş Özeti.csv"
        if(os.path.exists(file0) and os.path.isfile(file0)):
          os.remove(file0)
          print("file was deleted as preprocessing")
          
        else:
          print("file was not found to delete")
       

    #Reading pdf file
    def set_texts(pdf_files:list):
        print("starting to text process")
        #This function reads pdf and gets "CRC-32" components as texts
        for pdf_file in pdf_files:
            with fitz.open(pdf_file) as doc:
                text = ""
                for page in doc:
                    new_text = page.get_text()
                    text += new_text
            
        return text
  
    
    if 'PATH_INPUT_LAST' in st.session_state :

        pathz = st.session_state["PATH_INPUT_LAST"] + "/Bankomat Alışveriş Özeti.pdf"
          
        file_names = r'%s' % pathz
            
        text = set_texts([file_names])
            
       
        buffer = io.StringIO(text)
        new_text = ""
        flag = False
        i = 0
        for line in buffer.readlines():
           # print(line)  
            if "Bankomat Para Bilgileriniz" in line:
                flag = False
             
            
            elif "Bankomat Para (TL)" in line:
                flag = True
            
         
            elif "Vakıfbank" in line:
                flag = False
            elif flag:
                new_text += line
                
            elif "Sayın" in line :
                 name=(line.lstrip("Sayın ")).replace(",","")
                 print(name)
    
        buffer = io.StringIO(new_text)
        text_list = buffer.readlines()
    
        #preprocessing
          
        # ters n düzeltmesi (inverse n correction)
        a = list(map(lambda x: x.replace('\n', ''), text_list))
        # 4 bosluku tek bosluka dusurme (space reduction)
        b = list(map(lambda x: x.replace('    ', ' '), a))
    
        #kart kelimesi (card word)
        c = list(map(lambda x: x.replace('BANKOMAT KART ', 'BANKOMAT KART'), b))
    
        #istenmeyen ifadeler (undesired expressions)
        stopwords = ['BANKOMAT KART','İŞLEMİ','Kampanyası', 'ALIŞVERİŞ EKSTRESİ', 'Dekont yerine kullanılmaz. Uyuşmazlık halinde Banka kayıtları esas alınacaktır', 'www.vakifbank.com.tr I 0850 222 0 724', 'Türkiye Vakıflar Bankası T.A.O. Büyük Mükellefler V.D. 9220034970 Sicil Numarası: 776444','Saray Mahallesi Dr. Adnan Büyükdeniz Caddesi No :7 / A-B Ümraniye /İSTANBUL Mersis: 0922003497000017','Saray Mahallesi Dr. Adnan Büyükdeniz Caddesi No :7 / A-B Ümraniye /İSTANBUL Mersis: 0922003497000017          Sf 2 \\ 3   ','Saray Mahallesi Dr. Adnan Büyükdeniz Caddesi No :7 / A-B Ümraniye /İSTANBUL Mersis: 0922003497000017          Sf 2 \\ 2   ']
        d = list(filter(lambda w: w not in stopwords, c))
    
        e = list(map(lambda x: x.replace('CÜZDANDAN HESABA TRANSFER ', 'CÜZDANDAN HESABA TRANSFER İŞLEMİ'), d))
        
        f=  list(map(lambda x: x.replace('2022 Temmuz Internet ', '2022 Temmuz Internet Kampanyası'), e))
    
        g=  list(map(lambda x: x.replace('2022 Temmuz Restoran ', '2022 Temmuz Restoran Kampanyası'), f))
    
        # df'nin 4 sütununa uygun olarak liste elemanlarını 4'erli olarak uygun sırada alt alta getirme (Aligning the list elements by 4 in the appropriate order according to the 4 columns of the df)
        z=[]
        for  i in range(int(len(g)/4)):
              y=((g[i*4:i*4+4]))
              z.append(y)
    
        df = pd.DataFrame( z,columns=['ISLEM TARIHI', 'ACIKLAMA','TUTAR', "BANKOMAT PARA"])
    
    
        df.to_csv("Bankomat Alışveriş Özeti.csv", index=False)
        print('CSV file has created...')
    
    
    
        # dönem bilgisi (term information)
        date=(df["ISLEM TARIHI"].min())
        period=date.split(".")[1]
        list=["01","02","03","04","05","06","07","08","09","10","11","12"]
        for i in list:
            if period =="01":
                 period="Ocak"
            elif period =="02":
                 period="Şubat"
            elif period =="03":
                 period="Mart"
            elif period =="04":
                 period="Nisan"
            elif period =="05":
                 period="Mayıs"
            elif period =="06":
                 period="Haziran"
            elif period =="07":
                 period="Temmuz"
            elif period =="08":
                 period="Ağustos"
            elif period =="09":
                 period="Eylül"
            elif period =="10":
                 period="Ekim"
            elif period =="11":
                 period="Kasım"
            elif period =="12":
                 period="Aralık"
    
    
    
        # Max value of Purchasing/campaign
        df_count=df["ACIKLAMA"].value_counts(ascending=False).to_frame()
        df_count.columns=["count_of_purchase/campaign"]
        max_purchasing=df_count.iloc[0:1]
        max_purchasing.rename(columns = {'count_of_purchase/campaign':'max_count_of_purchase/campaign'}, inplace = True)
        print("max number of purchasing/campaign frequency:\n\n",max_purchasing)
        
        
        
        # Min value of Purchasing/campaign
        df_count_min=df["ACIKLAMA"].value_counts(ascending=True).to_frame()
        df_count_min.columns=["count_of_purchase/campaign"]
        min_purchasing=df_count_min.loc[df_count_min['count_of_purchase/campaign'] == 1]
        min_purchasing.rename(columns = {'count_of_purchase/campaign':'min_count_of_purchase/campaign'}, inplace = True)
        print("min number of purchasing/campaign frequency:\n\n",min_purchasing)
        
        
    
      
        #pie chart
        import pylab
        df_count_percent = (df_count['count_of_purchase/campaign'] / df_count['count_of_purchase/campaign'].sum()) * 100
        plot0 = df_count_percent.plot.pie(y='count_of_purchase/campaign', fontsize=17,figsize=(16, 16),autopct='%0.2f%%',pctdistance=1.5,
                                           labeldistance=None,stacked=True)
     
        pylab.ylabel('')
        pylab.xlabel('')
        
        plt.title('\nCount of Purchase or Campaign as Percentage (Pie)\n\n\n\n\n', fontsize=19,fontweight="bold",pad=6)
        
        plt.legend(loc='upper right', fontsize=9,prop={'size': 17}, bbox_to_anchor=(2,1),frameon=False)
          
        plot0=plot0.figure
        #border settings
        plot0.patch.set_linewidth(8)                       
        plot0.patch.set_edgecolor('#888888')                 
        #plt.show()
        
        
        #Plot a bar chart
        figure_0=df_count.plot.barh( y="count_of_purchase/campaign",
                  color='red',fontsize=15,figsize = (19, 19),edgecolor="#111111",stacked=True)
        plt.title('Count of Purchase or Campaign', fontsize=16,fontweight="bold",pad=12)
        figure_0.set_xlabel('\nFrequency\n',fontsize=14,fontweight="bold")
        figure_0=figure_0.figure
        #border settings
        figure_0.patch.set_linewidth(8)                       
        figure_0.patch.set_edgecolor('#888888') 
        
        plt.box(False)
        plt.show()
      
    
    
    
        # Plot a bar chart as percentage
    
        # df_count_percent1 = (df_count['count_of_purchase/campaign'] / df_count['count_of_purchase/campaign'].sum()) * 100
        # figure_1=df_count_percent1.plot.barh( y="count_of_purchase/campaign",fontsize=15 ,figsize = (19, 19),color='red',edgecolor="#111111",stacked=True)
        
        # plt.title('Count of Purchase or Campaign as Percentage', fontsize=16,fontweight="bold",pad=12)
        # figure_1.set_xlabel('\nPercentage',fontsize=14,fontweight="bold")
        # figure_1=figure_1.figure
        # plt.show()
        
        
    
        # Max Purchasing Value
        serie00=df["TUTAR"].apply(lambda x: x.strip("'"))
        serie = serie00.apply(lambda x: x.replace('.', ''))
        serie1=serie.apply(lambda x: x.replace(",","."))
        df_s=serie1.to_frame()
        df_s1=df_s.astype("float")
        df_s2=df_s1.sort_values(by="TUTAR",ascending=False)
        df_s3 = df_s2.assign(Index=range(len(df_s2))).set_index('Index')
        max_purchasing_value=df_s3["TUTAR"][0]
        print("Max purchasing value:",max_purchasing_value)
    
        m=df_s1.idxmax()[0] #max purchasing's id value
        max_purchasing_info=df["ACIKLAMA"][m]
        print("Max purchasing info:",max_purchasing_info)
    
        max_purchasing_gift0=df["BANKOMAT PARA"][m]     
        print("Gift money of max purchasing :",max_purchasing_gift0)
    
        max_purchasing_date=df["ISLEM TARIHI"][m]
        print("Date of max purchasing :",max_purchasing_date)
    
    
        # Min Purchasing Value
        df_ignore_return=df[df.ACIKLAMA != "Puan Kazanım İade -Satış İade"] 
        min_serie00=df_ignore_return["TUTAR"].apply(lambda x: x.strip("'"))
        min_serie=min_serie00.apply(lambda x: x.replace('.', ''))
        min_serie1=min_serie.apply(lambda x: x.replace(",","."))
        df_m=min_serie1.to_frame()
        df_m1=df_m.astype("float")
        #ignore transactions and campaigns (0.00)
        df_m2=df_m1[df_m1.TUTAR > float(0.0)]
    
        df_m3=df_m2.sort_values(by="TUTAR",ascending=True)
        df_m4 = df_m3.assign(Index=range(len(df_m3))).set_index('Index')
        min_purchasing_value=df_m4["TUTAR"][0]
        print("Min purchasing value:",min_purchasing_value)
    
        min=df_m2.idxmin()[0] #min purchasing's id value
        min_purchasing_info=df["ACIKLAMA"][min]
        print("Min purchasing info:",min_purchasing_info)
    
        min_purchasing_gift=df["BANKOMAT PARA"][min]
        print("Gift money of min purchasing :",min_purchasing_gift)
    
        min_purchasing_date=df["ISLEM TARIHI"][min]
        print("Date of min purchasing :",min_purchasing_date)
             
    
        # The number of campaigns benefited and the gift money earned
        df_campaign_numb=df_s1[(df_s1.TUTAR == float(0.0)) &  (df.ACIKLAMA!="CÜZDANDAN HESABA TRANSFER İŞLEMİ") & (df.ACIKLAMA!="PUAN BAKIM İŞLEMİ") & (df.ACIKLAMA!="Takas Iade") ].count()
        number_of_campaigns_benefited=df_campaign_numb[0]
        print("Number of campaigns benefited:",number_of_campaigns_benefited)
    
        campaign_id_list=df_s1[(df_s1.TUTAR == float(0.0)) &  (df.ACIKLAMA!="CÜZDANDAN HESABA TRANSFER İŞLEMİ") & (df.ACIKLAMA!="PUAN BAKIM İŞLEMİ") & (df.ACIKLAMA!="Takas Iade") ].index.tolist()
    
        # gift money column without "" and ,
        bankomat_para0=df["BANKOMAT PARA"].apply(lambda x: x.strip("'"))
        bankomat_para=bankomat_para0.apply(lambda x: x.replace(",","."))
        df_bankomat_para=bankomat_para.to_frame().reset_index()
        sum0=float(0)                          
        for i in campaign_id_list:
            sum0=sum0+float(df_bankomat_para["BANKOMAT PARA"][i]) 
        print("Total money earned from campaign:",sum0)
    
        #earned money as max and min
        campaign_earned_money=pd.DataFrame(np.array(df_bankomat_para["BANKOMAT PARA"][campaign_id_list]).reshape(len(campaign_id_list), 1),  columns=['campaign_earned_money']).astype(float)
        max_campaign_earned_money=float((campaign_earned_money.max())[0])
        min_campaign_earned_money=float((campaign_earned_money.min())[0])
        print("Maximum money earned from the campaign:",max_campaign_earned_money)
        print("Minumum money earned from the campaign:",min_campaign_earned_money)
    
    
        # Transfer Process from Account
        df_campaign_numb=df_s1[df.ACIKLAMA=="CÜZDANDAN HESABA TRANSFER İŞLEMİ"].count()
        number_of_transfer_process=df_campaign_numb[0]
        print("Number of transfer process:",number_of_transfer_process)
    
        transfer_id_list=df_s1[df.ACIKLAMA =="CÜZDANDAN HESABA TRANSFER İŞLEMİ"].index.tolist()
    
    
    
    
        #Transfered money as max and min
        transfered_money=pd.DataFrame(np.array(df_bankomat_para["BANKOMAT PARA"][transfer_id_list]).reshape(len(transfer_id_list), 1),  columns=['transfered_money'])
        max_transfered_money=float((transfered_money.max())[0])*(-1)
        min_transfered_money=float((transfered_money.min())[0])*(-1)
        print("Max. transferred money :",max_transfered_money)
        print("Min. transferred money:",min_transfered_money)
    
    
    
        # transferred money column without "" and ,
        tf0=df["BANKOMAT PARA"].apply(lambda x: x.strip("'"))
        tf1=tf0.apply(lambda x: x.strip("-"))
        tf2=tf1.apply(lambda x: x.replace(",","."))
        df_tf=tf2.to_frame().reset_index()
        sum=float(0)
        for i in transfer_id_list:
            sum=sum+float(df_tf["BANKOMAT PARA"][i])
        print("Total transferred money to the account:",sum)
    
    
    
    
        # Gift Money / Max
        gift_m00=df["BANKOMAT PARA"].apply(lambda x: x.strip("'"))
        gift_m=gift_m00.apply(lambda x: x.replace('.', ''))
        gift_m1=gift_m.apply(lambda x: x.replace(",","."))
        df_m1=gift_m1.to_frame()
        df_m2=df_m1.astype("float")
        df_m3=df_m2.sort_values(by="BANKOMAT PARA",ascending=False)
        df_m4 = df_m3.assign(Index=range(len(df_s2))).set_index('Index')
    
    
        z=df_m2.idxmax()[0] #max gift money's id value
        max_gift_money_info=df["ACIKLAMA"][z]
        print("Max gift money info (including campaigns):",max_gift_money_info)
    
        max_purchasing_gift=df["BANKOMAT PARA"][z]
        print("Gift money max. (including campaigns) :",max_purchasing_gift)
    
        spending_for_max_gift=df["TUTAR"][z]
        print("Spending value for gift money max. (including campaigns) :",spending_for_max_gift)
    
    
        ## Gift Money / Max (without campaigns)
    
        # Processed df
        serie_a100=df["TUTAR"].apply(lambda x: x.strip("'"))
        serie_a1=serie_a100.apply(lambda x: x.replace('.', ''))
        serie_a2=serie_a1.apply(lambda x: x.replace(",","."))
        df_a1=serie_a2.to_frame()
        df_a2=df_a1.astype("float")
    
    
    
        serie_a300=df["BANKOMAT PARA"].apply(lambda x: x.strip("'"))
        serie_a3=serie_a300.apply(lambda x: x.replace('.', ''))
        serie_a4=serie_a3.apply(lambda x: x.replace(",","."))
        df_a4=serie_a4.to_frame()
        df_a5=df_a4.astype("float")
    
        df_processed=pd.concat([df["ACIKLAMA"],df_a2, df_a5], axis=1)
        #drop campaign info rows
        d = df_processed[(df_processed["TUTAR"] == float(0.00)) & ( df_processed["BANKOMAT PARA"] > float(0.00))  ].index.values
        for i in range(len(d)):
            df_processed.drop(d[i],inplace=True)
        df_last =df_processed
        df_last1=df_last.sort_values(by="BANKOMAT PARA",ascending=False)
        #Head 5 value
        max_list_without=df_last1.head(5).values.tolist()
        #first
        max_list_without00=max_list_without[0][0]
        print("Max gift money info (without campaign / 1.):",max_list_without00)
        max_list_without01=max_list_without[0][1]
        print("Spending value for gift money max. (without campaign / 1.):",max_list_without01)
        max_list_without02=max_list_without[0][2]
        print("Gift money max. (without campaign / 1.) :",max_list_without02)
        #second
        print("--------------------------------------------------------------------")
        max_list_without10=max_list_without[1][0]
        print("Max gift money info (without campaign / 2.):",max_list_without10)
        max_list_without11=max_list_without[1][1]
        print("Spending value for gift money max. (without campaign / 2.):",max_list_without11)
        max_list_without12=max_list_without[1][2]
        print("Gift money max. (without campaign / 2.) :",max_list_without12)
        #third
        print("--------------------------------------------------------------------")
        max_list_without20=max_list_without[2][0]
        print("Max gift money info (without campaign / 3.):",max_list_without20)
        max_list_without21=max_list_without[2][1]
        print("Spending value for gift money max. (without campaign / 3.):",max_list_without21)
        max_list_without22=max_list_without[2][2]
        print("Gift money max. (without campaign / 3.) :",max_list_without22)
        #fourth
        print("--------------------------------------------------------------------")
        max_list_without30=max_list_without[3][0]
        print("Max gift money info (without campaign / 4.):",max_list_without30)
        max_list_without31=max_list_without[3][1]
        print("Spending value for gift money max. (without campaign / 4.):",max_list_without31)
        max_list_without32=max_list_without[3][2]
        print("Gift money max. (without campaign / 4.) :",max_list_without32)
        #fifth
        print("--------------------------------------------------------------------")
        max_list_without40=max_list_without[4][0]
        print("Max gift money info (without campaign / 5.):",max_list_without40)
        max_list_without41=max_list_without[4][1]
        print("Spending value for gift money max. (without campaign / 5.):",max_list_without41)
        max_list_without42=max_list_without[4][2]
        print("Gift money max. (without campaign / 5.) :",max_list_without42)
    
    
        # Gift Money / Min
        gift_min=df["BANKOMAT PARA"].apply(lambda x: x.strip("'"))
        gift_m1_min=gift_min.apply(lambda x: x.replace(",","."))
        df_m1_min=gift_m1_min.to_frame()
        df_m2_min=df_m1_min.astype("float")
    
    
        df_mz=df_m2_min[~(df_m2_min <= 0).all(axis=1)] # drop negative values
        z=df_mz.idxmin()[0] #max gift money's id value
        min_gift_money_info=df["ACIKLAMA"][z]
       
        min_purchasing_gift=df["BANKOMAT PARA"][z]
    
        spending_for_min_gift=df["TUTAR"][z]
       
        #There can be more than one situation where the minimum gift money is the same
        id_gift_money = df.index[df["BANKOMAT PARA"] == min_purchasing_gift].tolist()
        
        
        if id_gift_money[0]!="":
           
            min_gift_money_info1=df["ACIKLAMA"][id_gift_money[0]]
          
            print("Min gift money info (min gift money values are same) 1:",min_gift_money_info1)
           
            min_purchasing_gift1=df["BANKOMAT PARA"][id_gift_money[0]]
           
            print("Gift money min. (min gift money values are same) 1:",min_purchasing_gift1)
           
            spending_for_min_gift1=df["TUTAR"][[id_gift_money[0]]]
            spending_for_min_gift1=(spending_for_min_gift1._get_value(0, 'TUTAR'))
            print("Spending value for gift money min (min gift money values are same) 1:",spending_for_min_gift1)
           
           
        if len(id_gift_money)>=2: ####
            if id_gift_money[1]!="":
                min_gift_money_info2=df["ACIKLAMA"][id_gift_money[1]]
              
                print("Min gift money info (min gift money values are same) 2:",min_gift_money_info2)
                
                min_purchasing_gift2=df["BANKOMAT PARA"][id_gift_money[1]]
               
                print("Gift money min. (min gift money values are same) 2:",min_purchasing_gift2)
                
                spending_for_min_gift2=df["TUTAR"][[id_gift_money[1]]]
                spending_for_min_gift2=(spending_for_min_gift2._get_value(0, 'TUTAR'))
                print("Spending value for gift money min (min gift money values are same) 2:",spending_for_min_gift2)
               
        if len(id_gift_money)>=3:  
            if id_gift_money[2]!="":
                min_gift_money_info3=df["ACIKLAMA"][id_gift_money[2]]
               
                print("Min gift money info (min gift money values are same) 3:",min_gift_money_info3)
                
                min_purchasing_gift3=df["BANKOMAT PARA"][id_gift_money[2]]
                
                print("Gift money min. (min gift money values are same) 3:",min_purchasing_gift3)
                
                spending_for_min_gift3=df["TUTAR"][[id_gift_money[2]]]
                spending_for_min_gift3=(spending_for_min_gift3._get_value(0, 'TUTAR'))
                print("Spending value for gift money min (min gift money values are same) 3:",spending_for_min_gift3)
    
        if len(id_gift_money)>=4:  
            if id_gift_money[3]!="":
                min_gift_money_info4=df["ACIKLAMA"][id_gift_money[3]]
               
                print("Min gift money info (min gift money values are same) 4:",min_gift_money_info4)
                 
                min_purchasing_gift4=df["BANKOMAT PARA"][id_gift_money[3]]
          
                print("Gift money min. (min gift money values are same) 4:",min_purchasing_gift4)
                 
                spending_for_min_gift4=df["TUTAR"][[id_gift_money[3]]]
                spending_for_min_gift4=(spending_for_min_gift4._get_value(0, 'TUTAR'))
                print("Spending value for gift money min (min gift money values are same) 4:",spending_for_min_gift4)
        
        if len(id_gift_money)>=5:  
            if id_gift_money[4]!="":
                min_gift_money_info5=df["ACIKLAMA"][id_gift_money[4]]
               
                print("Min gift money info (min gift money values are same) 5:",min_gift_money_info5)
                 
                min_purchasing_gift5=df["BANKOMAT PARA"][id_gift_money[4]]
               
               
                print("Gift money min. (min gift money values are same) 5:",min_purchasing_gift5)
                 
                spending_for_min_gift5=df["TUTAR"][[id_gift_money[4]]]
                spending_for_min_gift5=(spending_for_min_gift5._get_value(0, 'TUTAR'))
               
                print("Spending value for gift money min (min gift money values are same) 5:",spending_for_min_gift5)
         
        try:
            print(id_gift_money[0])
        except:
            min_gift_money_info1="NA"
            min_purchasing_gift1="NA"
            spending_for_min_gift1="NA"
        
        try:
            print(id_gift_money[1])
        except:
            min_gift_money_info2="NA"
            min_purchasing_gift2="NA"
            spending_for_min_gift2="NA"
                 
        try: 
            print(id_gift_money[2])
        except:
            min_gift_money_info3="NA"
            min_purchasing_gift3="NA"
            spending_for_min_gift3="NA"
        
        try:
            print(id_gift_money[3])
        except:
            min_gift_money_info4="NA"
            min_purchasing_gift4="NA"
            spending_for_min_gift4="NA"  
        
        try:
            print(id_gift_money[4])
        except:
            min_gift_money_info5="NA"
            min_purchasing_gift5="NA"
            spending_for_min_gift5="NA" 
         
        try: 
             print(id_gift_money[5])
        except:
              min_gift_money_info6="NA"
              min_purchasing_gift6="NA"
              spending_for_min_gift6="NA" 
    
       
        #Sum of Values
        sum_of_gift_money=df_mz.sum()[0]
        print("Sum of gift money:",sum_of_gift_money)
        sum_of_spending=df_s3.sum()[0]
        print("Sum of spending:",sum_of_spending)

    ######################################### Streamlit Section for Main Interface
        with st.container(): 
            st.markdown("""<style>.stApp {background: url("https://c4.wallpaperflare.com/wallpaper/643/285/221/simple-background-blue-gradient-waveforms-wallpaper-preview.jpg");background-size: cover}</style>""",unsafe_allow_html=True)
        
          
            # giving a title as html
            st.markdown("<h1  style='text-align:center;  border: 3px solid rgba(255, 255, 255, 0); color:white; background:linear-gradient(to bottom, #00ffff  0%,#3399ff  100%); padding: 1px; border-radius: 6px;   font-size:275%;  font-family:bernard mt condensed; width:730px; text-shadow:2px 2px black;'>Account Statement Analyzer</h1>"
                      
                       , unsafe_allow_html=True)
        
            #color and font style settings
            
            st.markdown("<style>.stDateInput > label {font-size:120%; font-weight:bold; color:white; background:linear-gradient(to bottom, #3399ff  0%,#00ffff  100%);border: 2px ;border-radius: 3px;} </style>",unsafe_allow_html=True) #for all date input sections 
            st.markdown("<style>.stMultiSelect > label {font-size:120%; font-weight:bold; color:white;background:linear-gradient(to bottom, #3399ff   0%,#00ffff  100%);border: 2px;border-radius: 3px;}} </style>",unsafe_allow_html=True) #for all multi-select label sections
            
            st.markdown("""<style>span[data-baseweb="tag"] {background-color: green !important;}</style>""",unsafe_allow_html=True) #for all tag sections
            
            #button style settings
            st.markdown("""<style>div.stButton > button:first-child {width:250px; height:46px;font-weight : bold;border: 3px solid #4BFFA3; background-color:black; color:white;} div.stButton > button:hover {border: 3px solid #66ffcc; background-color:#66ffcc;color:black; @keyframes button {0% {transform: translate(-50%,-75%) rotate(0deg);} 100% {transform: translate(-50%,-75%) rotate(360deg);}  text-weight: bold; </style>""", unsafe_allow_html=True)
        
         
        col1, col2, col3 = st.columns(3)
        # getting the input data from the user 
        with col1:
         
          if st.button('Show Info Analysis'):    
                 for i in range((56)):
                   txt1=["Customer:"+"  "+ name ,"Period:"+"  "+period,"Max purchasing value:"+"  "+str(max_purchasing_value),"Max purchasing info:"+"  "+max_purchasing_info,"Gift money of max purchasing:"+"  "+str(max_purchasing_gift0),
                     "Date of max purchasing:"+"  "+str(max_purchasing_date),"Min purchasing value:"+"  "+str(min_purchasing_value),"Min purchasing info:"+"  "+min_purchasing_info,
                     "Gift money of min purchasing:"+"  "+str(min_purchasing_gift),"Date of min purchasing :"+"  "+str(min_purchasing_date),"Number of campaigns benefited:"+"  "+str(number_of_campaigns_benefited),"Total money earned from campaign:"+"  "+str(sum0),
                     "Maximum money earned from the campaign:"+"  "+str(max_campaign_earned_money),"Minumum money earned from the campaign:"+"  "+str(min_campaign_earned_money),"Number of transfer process:"+"  "+str(number_of_transfer_process),
                     "Max. transferred money:"+"  "+str(max_transfered_money),"Min. transferred money:"+"  "+str(min_transfered_money),"Total transferred money to the account:"+"  "+str(sum),"Max gift money info (including campaigns):"+"  "+max_gift_money_info,
                     "Gift money max. (including campaigns):"+"  "+max_purchasing_gift,
                     "Spending value for gift money max. (including campaigns) :"+"  "+spending_for_max_gift,"Max gift money info (without campaign / 1.):"+"  "+max_list_without00,
                     "Spending value for gift money max. (without campaign / 1.):"+"  "+str(max_list_without01),
                     "Gift money max. (without campaign / 1.):"+"  "+str(max_list_without02),"Max gift money info (without campaign / 2.):"+"  "+str(max_list_without10),"Spending value for gift money max. (without campaign / 2.):"+"  "+str(max_list_without11),"Gift money max. (without campaign / 2.):"+"  "+str(max_list_without12),"Max gift money info (without campaign / 3.):"+"  "+str(max_list_without20),
                     "Spending value for gift money max. (without campaign / 3.):"+"  "+str(max_list_without21),"Gift money max. (without campaign / 3.):"+"  "+str(max_list_without22),"Max gift money info (without campaign / 4.):"+"  "+str(max_list_without30),"Spending value for gift money max. (without campaign / 4.):"+"  "+str(max_list_without31),"Gift money max. (without campaign / 4.):"+"  "+str(max_list_without32),
                     "Max gift money info (without campaign / 5.):"+"  "+str(max_list_without40),"Spending value for gift money max. (without campaign / 5.):"+"  "+str(max_list_without41),"Gift money max. (without campaign / 5.) :"+"  "+str(max_list_without42),"Min gift money info (1):"+"  "+min_gift_money_info1,"Gift money min. (1):"+"  "+min_purchasing_gift1,"Spending value for gift money min. (1):"+"  "+spending_for_min_gift1,
                     "Min gift money info .(2):"+"  "+min_gift_money_info2,"Gift money min. (2):"+"  "+min_purchasing_gift2,"Spending value for gift money min. (2):"+"  "+spending_for_min_gift2,
                     "Min gift money info (3):"+"  "+min_gift_money_info3,"Gift money min. (3):"+"  "+min_purchasing_gift3,"Spending value for gift money min. (3):"+"  "+spending_for_min_gift3,
                     "Min gift money info (4):"+"  "+min_gift_money_info4,"Gift money min. (4):"+"  "+min_purchasing_gift4,"Spending value for gift money min. (4):"+"  "+spending_for_min_gift4,
                     "Min gift money info (5):"+"  "+min_gift_money_info5,"Gift money min. (5):"+"  "+min_purchasing_gift5,"Spending value for gift money min. (5):"+"  "+spending_for_min_gift5,
                     "Min gift money info (6):"+"  "+min_gift_money_info6,"Gift money min. (6):"+"  "+min_purchasing_gift6,"Spending value for gift money min. (6):"+"  "+spending_for_min_gift6,
                     "Sum of gift money:"+"  "+str(sum_of_gift_money),"Sum of spending:"+"  "+str(sum_of_spending)]
                     
                  
                  
                   txt1=txt1[i]
                 
                 
                 
                   htmlstr1=f"""<p style='background-color:rgb(0,128,0,0.6);
                                               color:rgb(255,255,255,1);
                                               font-size:18px;
                                               font-weight:bold;
                                               border-radius:3px;
                                               line-height:60px;
                                               width: 730px;
                                               font-family: Source Sans Pro;
                                               padding-left:17px;'>
                                               {txt1}</style>
                                               <br></p>""" 
                   st.markdown(htmlstr1,unsafe_allow_html=True) 
                 
                 
        pressed_button2=""
        pressed_button3=""
        with col2:
             if st.button("Show Table Analysis") :
                pressed_button2=1
        with col3:
                 
             if st.button("Show Plot Analysis"):
                pressed_button3=1
                
         
        if   pressed_button2==1:
              # data frame style
              #data frame style
              st.markdown('<style>div[class="css-o1jpvw e19lei0e1"] {color: black; background:white;font-weight: normal;border:2px solid black; border-radius: 5px; } .data:hover{ background:#3399ff;border:2px solid black; )}</style>', unsafe_allow_html=True)
              ## left column color
              st.markdown('<style>div[class="css-zjmy26 e1wqxbhn1"] {color:black;} </style>', unsafe_allow_html=True)

        
     
              st.dataframe(max_purchasing,height=400)
        
              st.dataframe(min_purchasing,height=400)
             
         
             
         
        if   pressed_button3==1:    
             st.pyplot(plot0)
             st.pyplot(figure_0)
        
  
        footer="""
         <style>
            .img 
            {
              max-width: 100%;
                      
            }
                    
                    
            .Headerstyle 
            {
              color:white;
              font-size:20px;
              font-style: italic;
              text-shadow:1.5px 1.5px #4BFFA3;
              transition: transform .2s;
              text-align: center;
             
            
            }  
                     
            .Headerstyle:hover {
                          
              transform: scale(1.5);
              transition: 0.2s;
            }
                     
            .image1 { 
              padding: 10px;  
              transition: transform .2s;
            }
                     
            .image2 { 
              padding: 10px;
              transition: transform .2s;
            }
            .image1:hover {  
              #border: 4px solid green;
              #border-radius: 15px;
              transform: scale(1.5);
              transition: 0.2s;
            }
            .image2:hover {  
              #border: 4px solid green;
              #border-radius: 15px;
              transform: scale(1.5);
              transition: 0.2s;
            }
                     
            
            .footer {
                       
              position: relative;
           
              left: -98%;
             
              width: 300%;
              background-color: ##0000ffff;
              color: white;
              text-align: center;
            }			  
            
            
            
            
            .container {
            
              position: relative;
              width: 100%;
              margin: 0px auto; 
              padding: 10px 3px;
              
            
            }
            
            .Loading {
              position: relative;
              display: inline-block;
              width: 100%;
              height: 50%;
              background: rgb(34,193,195);
              background: linear-gradient(90deg, rgba(34,193,195,1) 0%, rgba(253,187,45,1) 100%);
              box-shadow: inset 0 0 5px rgba(0, 0, 0, .2);
              border-radius: 4px;
              overflow: hidden;
            }
            
            .Loading:after {
              content: '';
              position: absolute;
              background: #eeebda;
              color:black;
              font-size: 200%;
              width: 25%;
              left:38%;
              height: 100%;
              border-radius: 2px;
              box-shadow: 0 0 5px rgba(0, 0, 0, .7);
              animation: load 5s infinite;
            }
            
            @keyframes load {
              0% {
              content: 'Best';
              font-style: italic;
              }
              
              
              20% {
              content: 'Results';
              font-style: italic;
              }
              
              40% {
              content: 'Data';
              font-style: italic;
            
              }
              
              60% {
              content: 'Engineering';
              font-style: italic;
            
              }
              
              80% {
              content: 'Premium';
              font-style: italic;
            
              }
              
              100% {
              content: 'Ui';
              font-style: italic;
             
              }
          </style>
        <body>
        <div class="footer" style="
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 10vh;">
            <p class="Headerstyle"><b>Stay in Touch With Me !</b></p>
            <div><div style="display: flex;justify-content: center;"><a href="https://stackoverflow.com"><img class="image1" src="https://cdn-icons-png.flaticon.com/128/2111/2111628.png" alt="stackoverflow icon" width="60" height="60"></a><a href="https://www.linkedin.com"><img class="image2" src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="linkedin icon" width="60" height="60"></a></div>
            <div class="container"></div>
            <div class="Loading"></div>
            </div>       
        </div>
        
        </body>
         """
        hide_st_style =" <style>footer {visibility: hidden;}</style>"
        st.markdown(hide_st_style, unsafe_allow_html=True)  
        st.markdown(footer,unsafe_allow_html=True) 
    

try:
    if __name__=='__main__':
                               
                   if "page" not in st.session_state:
                       st.session_state["page"] = "login"
                
                   if st.session_state["page"] == "login":
                     
                        login()
                   
                   elif st.session_state["page"] == "main":
                   
                        main()
    
except fitz.FileNotFoundError: 
      
       st.warning("Please make the correct login on the login screen or check the pdf file in app path and try again.")
       st.markdown("""<style>.stApp {background: url("https://cutewallpaper.org/22/gears-wallpaper-background/208187525.jpg");background-size: cover}</style>""",unsafe_allow_html=True)
       hide_st_style =" <style>footer {visibility: hidden;}</style>"
       st.markdown(hide_st_style, unsafe_allow_html=True)  
       sound = st.session_state["PATH_INPUT_LAST"]+"/warning.mp3"
       playsound(sound)

except AttributeError:
       
       st.warning("Please check the content of the pdf file.") 
       st.markdown("""<style>.stApp {background: url("https://cutewallpaper.org/22/gears-wallpaper-background/208187525.jpg");background-size: cover}</style>""",unsafe_allow_html=True)
       hide_st_style =" <style>footer {visibility: hidden;}</style>"
       st.markdown(hide_st_style, unsafe_allow_html=True)  
       sound = st.session_state["PATH_INPUT_LAST"]+"/warning.mp3"
       playsound(sound)
       
except IndexError:                
       st.warning("Generic application error. Please request software update.")
       st.markdown("""<style>.stApp {background: url("https://cutewallpaper.org/22/gears-wallpaper-background/208187525.jpg");background-size: cover}</style>""",unsafe_allow_html=True)
       hide_st_style =" <style>footer {visibility: hidden;}</style>"
       st.markdown(hide_st_style, unsafe_allow_html=True)
       sound = st.session_state["PATH_INPUT_LAST"]+"/warning.mp3"
       playsound(sound)
       
except PermissionError:
       st.warning("Please close the Bankomat Alışveriş Özeti.csv file.")
       st.markdown("""<style>.stApp {background: url("https://cutewallpaper.org/22/gears-wallpaper-background/208187525.jpg");background-size: cover}</style>""",unsafe_allow_html=True)
       hide_st_style =" <style>footer {visibility: hidden;}</style>"
       st.markdown(hide_st_style, unsafe_allow_html=True)
       sound = st.session_state["PATH_INPUT_LAST"]+"/warning.mp3"
       playsound(sound)
