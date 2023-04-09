
import os
import streamlit as st
import numpy as np
import pandas as pd
import pickle
from matplotlib import image

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")
encoder = os.path.join(dir_of_interest, "data", "encoder.pkl")
scaler = os.path.join(dir_of_interest, "data", "scaler.pkl")
model = os.path.join(dir_of_interest, "data", "model_1.pkl")
scaler = pickle.load(open(scaler, 'rb'))
encoder = pickle.load(open(encoder, 'rb'))
model = pickle.load(open(model, 'rb'))



st.title(":blue[Enter the laptop details]")
IMAGE_PATH = os.path.join(dir_of_interest, "images", "mainimg.jpg")
img = image.imread(IMAGE_PATH)
st.image(img)

ram=st.selectbox(":blue[Ram (GB)]",(4,8,16,32))
ram_type=st.selectbox(":blue[Ram Type]",("DDR4","DDR5","LPDDR4","LPDDR4X","LPDDR5","Unified"))
p_c=st.selectbox(":blue[Processor_company]",("Intel","AMD","Apple"))
#Brand=st.selectbox(":blue[Brand]",("ASUS","Lenovo","HP","DELL","acer","RedmiBook","MSI","Infinix","Apple","realme"))
if p_c=="Intel":
	processor=st.selectbox(":blue[Processor]",("Celeron","Dual","Pentium","i3","i5","i7","i9"))
	Brand=st.selectbox(":blue[Brand]",("ASUS","Lenovo","HP","DELL","acer","RedmiBook","MSI","Infinix","realme"))
	if processor=="Celeron":
		ram=st.selectbox(":blue[Ram (GB)]",(4,8))
		ram_type=st.selectbox(":blue[Ram Type]",("DDR4","LPDDR4","LPDDR4X"))
		
	elif processor=="Pentium":
		ram=st.selectbox(":blue[Ram (GB)]",(8,))
		ram_type=st.selectbox(":blue[Ram Type]",("DDR4",))
		
	OS=st.selectbox(":blue[Operating System]",("win10","win11"))

elif p_c=="AMD":
    processor=st.selectbox(":blue[Processor]",("Athlon","r3","r5","r7","r9"))
    Brand=st.selectbox(":blue[Brand]",("ASUS","Lenovo","HP","DELL","acer","RedmiBook","MSI","Infinix","realme"))
    OS=st.selectbox(":blue[Operating System]",("win10","win11"))
   
   
elif p_c=="Apple":
    processor=st.selectbox(":blue[Processor]",("M1","M1P","M2","M1M"))
    Brand=st.selectbox(":blue[Brand]",("APPLE",))
    OS=st.selectbox(":blue[Operating System]",("MacOS",))
    
    

#Brand=st.selectbox(":blue[Brand]",("ASUS","Lenovo","HP","DELL","acer","RedmiBook","MSI","Infinix","APPLE","realme"))
touch_scr=st.selectbox(":blue[Touch_screen]",("yes","no"))
ssd=st.selectbox(":blue[SSD(GB)]",(0,128,256,512,1020,2040))
hdd=st.selectbox(":blue[HDD(GB)]",(0,256,1020))
X_test_num=pd.DataFrame({"Ram_1":ram,"SSD":ssd,"HDD":hdd},index=[0])
X_test_cat=pd.DataFrame({"processor_company":p_c,"Ram_type":ram_type,"Processor":processor,"Brand":Brand,"Operating_System":OS,"Touch_Screen":touch_scr},index=[0])

X_test_num_rescaled = pd.DataFrame(scaler.transform(X_test_num)) 
                                    
X_test_cat_ohe = pd.DataFrame(encoder.transform(X_test_cat)) 
                               
X_test_transformed = pd.concat([X_test_num_rescaled, X_test_cat_ohe], axis=1)

but=st.button("Predict Price")
if but==True:
	pred=model.predict(X_test_transformed)
	st.markdown(":blue[The price of the laptop is ₹ {}]".format(pred[0].round(2)))
# st.markdown("Predicted Laptop Price")
# st.subheader("₹", round(pred[0], 2))
