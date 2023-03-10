import streamlit as st
import pickle 
import numpy as np 
import pandas as pd

def load_model():
    with open('final_saved_steps (2).pkl','rb') as file:
        data1=pickle.load(file)
    return data1

data1=load_model()

clf=data1["model"]
le = data1["encoder"]

st.title("Know your dominant dosha in 20 questions!")

 


gender = ("Female","Male")
skin_Type=("Thin","Thick")
teeth_Color=("MilkyWhite","Yellowish","Dull/Blackish")
bowel_Freq=("Regular","Irregular","Variable")
speaking_Amount=("Moderate","Excessive","Less")

bodyframes = ("Thin/Narrow","Medium","Broad")
stoolcons = ("Medium","Hard","Loose/Soft/Semisolid")
shoulder_breadths = ("Thin/Narrow","Medium",'Broad')
walking_styles = ("Sharp/Accurate","Firm/Steady","Unsteady")
skin_pimple = ("Pimples","Non_Pimples")

bodyHair_Color = ("Black","DarkBrown","Dusky","LightBrown")
eye_Size = ("Moderatelydeveloped","Weaklydeveloped","Welldeveloped")
eye_Symmetry = ("Proportionate","Disproportionate")
eyebrow_Size = ("Large","Medium","Small")
eyelash_Size = ("Small","Medium","Large")

face_size = ("Moderatelydeveloped","Welldeveloped","Weaklydeveloped")
forehead_breadth = ("Medium","Thin/Narrow","Broad")
hair_nature = ("Normal","Dry","Oily","Seasonal Variable")
hands_length=("Long","Medium","Tooshort/Toolong")
palate_color = ("Pink","Pale/Yellow","Reddish")

selected_Gender=st.radio("I identify as a: ",gender)
selected_skin_Type = st.selectbox("In general, my skin type is :",skin_Type)
selected_teeth_color = st.selectbox("When I smile, my teeth color is :",teeth_Color)
selected_bowel_Freq= st.selectbox("Sorry for asking but we need to know, select your bowel frequency on a good day:",bowel_Freq)
selected_speaking_Amount = st.selectbox("How much do I speak in general?:",speaking_Amount)

selected_face_size = st.selectbox("How would you describe your face size? ",face_size)
selected_forehead_breadth = st.selectbox("I would say forehead breadth is: ",forehead_breadth)
selected_hair_nature = st.selectbox("My hair feels: ",hair_nature)
selected_hands_length = st.selectbox("The length of my hands are:",hands_length)
selected_palate_color = st.selectbox("My palate color is (the top part of the inside of your mouth.???? )",palate_color)

selected_stoolcons=st.selectbox("Sorry for asking this also, but again, we need to know, select your stool consistency: ", stoolcons) 
selected_bodyframe=st.selectbox("I would describe my bodyframe as: ",bodyframes) 
selected_shoulder_breadths=st.selectbox("My shoulder breadth is:",shoulder_breadths) 
selected_walking_style = st.selectbox("In general, my walking style can be described as: ",walking_styles) 
selected_skin_pimple = st.selectbox("Do I have pimple prone skin? ",skin_pimple)

selected_bodyHair_Color=st.selectbox("My body hair color is: ",bodyHair_Color)
selected_eye_Size=st.selectbox("My eye size can be described as: ",eye_Size)
selected_eye_Symmetry=st.selectbox("Are my eyes symmertrical? : ",eye_Symmetry)
selected_eyebrow_Size=st.selectbox("In general, I would describe my eyebrow size as: ",eyebrow_Size)
selected_eyelash_Size=st.selectbox("My eyelashes are: ",eyelash_Size)

if selected_Gender == "Female":
    input1 = 0
else:
    input1 = 1

if selected_skin_Type == "Thick":
    input2 = 0
else:
    input2 =1

if  selected_teeth_color == "MilkyWhite":
    input3 = 1
elif selected_teeth_color=="Yellowish": 
    input3 = 2
else:
    input3 = 0
    
if  selected_bowel_Freq== "Regular":
    input4 = 1 
elif selected_bowel_Freq == "Irregular":
    input4 = 0
else:
    input4 = 2

if  selected_speaking_Amount=="Moderate":
    input5 =  2
elif selected_speaking_Amount == "Excessive":
    input5 = 0
else:
    input5 = 1

if selected_stoolcons == "Medium":
    input11 = 2
elif selected_stoolcons=="Hard":
    input11 =0
else:
    input11 = 1

if selected_bodyframe == "Thin/Narrow":
    input12 = 2
elif selected_bodyframe=="Medium":
    input12 =1
else:
    input12 = 0

if selected_face_size == "Moderatelydeveloped":
    input6 = 0
elif selected_face_size == "Weaklydeveloped":
    input6 = 1
else:
    input6 = 2

if selected_forehead_breadth == "Broad":
    input7 = 0
elif selected_forehead_breadth == "Medium":
    input7 = 1
else:
    input7 = 2

if selected_hair_nature == "Dry":
    input8 = 0
elif selected_hair_nature == "Normal":
    input8 = 1
elif selected_hair_nature == "Seasonal/Variable":
    input8 = 2
else:
    input8 = 3

if selected_hands_length == "Long":
    input9 = 0
elif selected_hands_length=="Medium":
    input9 = 1
else:
    input9 = 2

if stoolcons == "Medium":
    input11 = 2
elif stoolcons=="Hard":
    input11 =0
else:
    input11 = 1
if bodyframes == "Thin/Narrow":
    input12 = 2
elif bodyframes=="Medium":
    input12 =1
else:

    input12 = 0
if selected_palate_color =="Pink":
    input10 = 1
elif selected_palate_color =="Reddish":
    input10 = 2
else:
    input10 =0

if selected_shoulder_breadths == "Broad":
    input13 = 0
elif selected_shoulder_breadths=="Medium":
    input13 = 1
else:
    input13 = 2

if selected_walking_style =="Firm/Steady":
    input14 = 0
elif selected_walking_style=="Sharp/Accurate":
    input14 = 1
else:
    input14 = 2

if selected_skin_pimple == "Pimples":
     input15=1
else:
     input15=0

if selected_bodyHair_Color == "Black":
    input16 = 0
elif selected_bodyHair_Color  == "DarkBrown":
    input16 = 1
elif selected_bodyHair_Color  == "LightBrown":
    input16 = 3
else:
     input16 = 2

if selected_eye_Size == "Moderatelydeveloped":
     input17=0
elif selected_eye_Size == "Weaklydeveloped":
     input17=1
else:
     input17=2

if selected_eye_Symmetry == "Proportionate":
     input18=1
else:
     input18=0

if selected_eyebrow_Size == "Medium":
     input19=1
elif selected_eyebrow_Size == "Large":
     input19=0
else:
     input19=2

if selected_eyelash_Size == "Small":
     input20=2
elif selected_eyelash_Size == "Medium":
     input20=1
else:
     input20=0


ok=st.button("Check Dominant Dosha")

if ok:
        X=np.array([[input1,input12,input16,input17,input18,input19,input20,input6,input7,input8,input9,input10,input13,input2,
        input3,input4,input11,input5,input14,input15]])
        
        hs = clf.predict(X)

        if hs[0]==2:
            st.subheader("You dominant dosha is **VATA**.")
            st.markdown("**Strengths**: learn quickly, highly creative, multitasker, kind-hearted, flexible, ???on the go,??? naturally slim")
            st.text("")
            st.markdown("**Weaknesses**: forgetful, anxious, unstable mood, can get overwhelmed easily, highly sensitive to the cold, has trouble sleeping, irregular appetite and eating patterns, prone to digestive issues and gas, poor circulation (cold hands and feet)")
        elif hs[0]==0:
            st.subheader("You dominant dosha is **KAPHA**.")
            st.markdown("**Strengths**: empathetic, caring, trusting, patient, calm, wise, happy, romantic, strong bones and joints, healthy immune system")
            st.text("")
            st.markdown("**Weaknesses**: prone to weight gain, slow metabolism, sluggishness, over-sleeping, breathing issues (i.e., asthma, allergies), higher risk of heart disease, mucus buildup, susceptible to depression, needs regular motivation and encouragement")
        else:
            st.subheader("You dominant dosha is **PITTA**.")
            st.markdown("**Strengths**: intelligent, purposeful, learns quickly, self-determined, masters skills easily, strong desire for success, strong, natural leaders, quick metabolism, good circulation, healthy skin and hair")
            st.text("")
            st.markdown("impatient, prone to conflict, always hungry, mood swings when hungry, prone to acne and inflammation, sensitive to hot temperatures")


        
