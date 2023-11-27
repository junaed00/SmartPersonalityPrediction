import streamlit as st
from PIL import Image
import pickle
import numpy as np
import pandas as pd
import csv
from sklearn.cluster import KMeans


# model = pickle.load(open('./Model/ML_Model.pkl', 'rb'))

def run():
    img = Image.open('icon_pers.png')
    img = img.resize((156,145))
    st.image(img,use_column_width=False)
    st.title("Smart Personality Prediction Model")

    ## Full Name
    fn = st.text_input('Full Name')

    gen_display = ('Female','Male','Others')
    gen_options = list(range(len(gen_display)))
    gen = st.selectbox("Gender",gen_options, format_func=lambda x: gen_display[x])

    ## For _der
    _1_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _1_options = list(range(len(_1_display)))
    _1 = st.selectbox("I am the life of the party.",_1_options, format_func=lambda x: _1_display[x])

    ## For _ital Status
    _2_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _2_options = list(range(len(_2_display)))
    _2 = st.selectbox("I don't talk a lot.", _2_options, format_func=lambda x: _2_display[x])

    ## No of _endets
    _3_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _3_options = list(range(len(_3_display)))
    _3 = st.selectbox("I feel comfortable around people.",  _3_options, format_func=lambda x: _3_display[x])

    ## For _
    _4_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _4_options = list(range(len(_4_display)))
    _4 = st.selectbox("I keep in the background.",_4_options, format_func=lambda x: _4_display[x])

    ## For _
    _5_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _5_options = list(range(len(_5_display)))
    _5 = st.selectbox("I start conversations.",_5_options, format_func=lambda x: _5_display[x])

    ## For _ status
    _6_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _6_options = list(range(len(_6_display)))
    _6 = st.selectbox("I have little to say.",_6_options, format_func=lambda x: _6_display[x])

    ## For _erty status
    _7_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _7_options = list(range(len(_7_display)))
    _7 = st.selectbox("I talk to a lot of different people at parties.",_7_options, format_func=lambda x: _7_display[x])

    ## For _it Score
    _8_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _8_options = list(range(len(_8_display)))
    _8 = st.selectbox("I don't like to draw attention to myself.",_8_options, format_func=lambda x: _8_display[x])

    ## For der
    _9_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _9_options = list(range(len(_9_display)))
    _9 = st.selectbox("I don't mind being the center of attention.",_9_options, format_func=lambda x: _9_display[x])

      ## For der
    _10_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _10_options = list(range(len(_10_display)))
    _10 = st.selectbox("I am quiet around strangers.",_10_options, format_func=lambda x: _10_display[x])

      ## For _der
    _11_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _11_options = list(range(len(_11_display)))
    _11 = st.selectbox("I get stressed out easily.",_11_options, format_func=lambda x: _11_display[x])

      ## For _der
    _12_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _12_options = list(range(len(_12_display)))
    _12 = st.selectbox("I am relaxed most of the time.",_12_options, format_func=lambda x: _12_display[x])

      ## For _der
    _13_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _13_options = list(range(len(_13_display)))
    _13 = st.selectbox("I worry about things.",_13_options, format_func=lambda x: _13_display[x])

      ## For _der
    _14_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _14_options = list(range(len(_14_display)))
    _14 = st.selectbox("I seldom feel blue.",_14_options, format_func=lambda x: _14_display[x])

      ## For _der
    _15_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _15_options = list(range(len(_15_display)))
    _15 = st.selectbox("I am easily disturbed.",_15_options, format_func=lambda x: _15_display[x])

      ## For _der
    _16_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _16_options = list(range(len(_16_display)))
    _16 = st.selectbox("I get upset easily.",_16_options, format_func=lambda x: _16_display[x])

      ## For _der
    _17_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _17_options = list(range(len(_17_display)))
    _17 = st.selectbox("I change my mood a lot.",_17_options, format_func=lambda x: _17_display[x])

      ## For _der
    _18_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _18_options = list(range(len(_18_display)))
    _18 = st.selectbox("I have frequent mood swings.",_18_options, format_func=lambda x: _18_display[x])

      ## For _der
    _19_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _19_options = list(range(len(_19_display)))
    _19 = st.selectbox("I get irritated easily.",_19_options, format_func=lambda x: _19_display[x])

      ## For _der
    _20_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _20_options = list(range(len(_20_display)))
    _20 = st.selectbox("I often feel blue.",_20_options, format_func=lambda x: _20_display[x])

      ## For _der
    _21_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _21_options = list(range(len(_21_display)))
    _21 = st.selectbox("I feel little concern for others.",_21_options, format_func=lambda x: _21_display[x])

      ## For _der
    _22_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _22_options = list(range(len(_22_display)))
    _22 = st.selectbox("I am interested in people.",_22_options, format_func=lambda x: _22_display[x])

      ## For _der
    _23_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _23_options = list(range(len(_23_display)))
    _23 = st.selectbox("I insult people.",_23_options, format_func=lambda x: _23_display[x])

      ## For _der
    _24_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _24_options = list(range(len(_24_display)))
    _24 = st.selectbox("I sympathize with others' feelings.",_24_options, format_func=lambda x: _24_display[x])

      ## For _der
    _25_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _25_options = list(range(len(_25_display)))
    _25 = st.selectbox("I am not interested in other people's problems.",_25_options, format_func=lambda x: _25_display[x])

      ## For _der
    _26_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _26_options = list(range(len(_25_display)))
    _26 = st.selectbox("I have a soft heart.",_26_options, format_func=lambda x: _26_display[x])

      ## For _der
    _27_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _27_options = list(range(len(_27_display)))
    _27 = st.selectbox("I am not really interested in others.",_27_options, format_func=lambda x: _27_display[x])

      ## For _der
    _28_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _28_options = list(range(len(_28_display)))
    _28 = st.selectbox("I take time out for others.",_28_options, format_func=lambda x: _28_display[x])

      ## For _der
    _29_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _29_options = list(range(len(_29_display)))
    _29 = st.selectbox("I feel others' emotions.",_29_options, format_func=lambda x: _29_display[x])

      ## For _der
    _30_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _30_options = list(range(len(_30_display)))
    _30 = st.selectbox("I make people feel at ease.",_30_options, format_func=lambda x: _30_display[x])

      ## For _der
    _31_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _31_options = list(range(len(_31_display)))
    _31 = st.selectbox("I am always prepared.",_31_options, format_func=lambda x: _31_display[x])

      ## For _der
    _32_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _32_options = list(range(len(_32_display)))
    _32 = st.selectbox("I leave my belongings around.",_32_options, format_func=lambda x: _32_display[x])

      ## For _der
    _33_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _33_options = list(range(len(_33_display)))
    _33 = st.selectbox("I pay attention to details.",_33_options, format_func=lambda x: _33_display[x])

      ## For _der
    _34_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _34_options = list(range(len(_34_display)))
    _34 = st.selectbox("I make a mess of things.",_34_options, format_func=lambda x: _34_display[x])

      ## For _der
    _35_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _35_options = list(range(len(_35_display)))
    _35 = st.selectbox("I get chores done right away.",_35_options, format_func=lambda x: _35_display[x])

      ## For _der
    _36_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _36_options = list(range(len(_36_display)))
    _36 = st.selectbox("I often forget to put things back in their proper place.",_36_options, format_func=lambda x: _36_display[x])

      ## For _der
    _37_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _37_options = list(range(len(_37_display)))
    _37 = st.selectbox("I like order.",_37_options, format_func=lambda x: _37_display[x])

      ## For _der
    _38_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _38_options = list(range(len(_38_display)))
    _38 = st.selectbox("I shirk my duties.",_38_options, format_func=lambda x: _38_display[x])

      ## For _der
    _39_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _39_options = list(range(len(_39_display)))
    _39 = st.selectbox("I follow a schedule.",_39_options, format_func=lambda x: _39_display[x])

      ## For _der
    _40_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _40_options = list(range(len(_40_display)))
    _40 = st.selectbox("I am exacting in my work.",_40_options, format_func=lambda x: _40_display[x])

      ## For _der
    _41_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _41_options = list(range(len(_41_display)))
    _41 = st.selectbox("I have a rich vocabulary.",_41_options, format_func=lambda x: _41_display[x])

      ## For _der
    _42_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _42_options = list(range(len(_42_display)))
    _42 = st.selectbox("I have difficulty understanding abstract ideas.",_42_options, format_func=lambda x: _42_display[x])

      ## For _der
    _43_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _43_options = list(range(len(_43_display)))
    _43 = st.selectbox("I have a vivid imagination.",_43_options, format_func=lambda x: _43_display[x])

      ## For _der
    _44_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _44_options = list(range(len(_44_display)))
    _44 = st.selectbox("I am not interested in abstract ideas.",_44_options, format_func=lambda x: _44_display[x])

      ## For _der
    _45_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _45_options = list(range(len(_45_display)))
    _45 = st.selectbox("I have excellent ideas.",_45_options, format_func=lambda x: _45_display[x])

      ## For _der
    _46_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _46_options = list(range(len(_46_display)))
    _46 = st.selectbox("I do not have a good imagination.",_46_options, format_func=lambda x: _46_display[x])

      ## For _der
    _47_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _47_options = list(range(len(_47_display)))
    _47 = st.selectbox("I am quick to understand things.",_47_options, format_func=lambda x: _47_display[x])

      ## For _der
    _48_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _48_options = list(range(len(_48_display)))
    _48 = st.selectbox("I use difficult words.",_48_options, format_func=lambda x: _48_display[x])

      ## For _der
    _49_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _49_options = list(range(len(_49_display)))
    _49 = st.selectbox("I spend time reflecting on things.",_49_options, format_func=lambda x: _49_display[x])

      ## For _der
    _50_display = ('Strongly Disagree', ' Disagree', 'Neutral', 'agree', 'Strongly agree')
    _50_options = list(range(len(_50_display)))
    _50 = st.selectbox("I am full of ideas.",_50_options, format_func=lambda x: _50_display[x])

    datas=['Extrovert','Conseientions','Open','Competitive','Emotionally Stable','Agreeable','Introvert','Consistent','Spontaneity','Neurotic']

    df=pd.read_csv('pers-group.csv', index_col=0)
    if st.button("Submit"):
        

        features=[[_1,_2,_3,_4,_5,_6,_7,_8,_9,_10,_11,_12,_13,_14,_15,_16,_17,_18,_19,_20,_21,_22,_23,_24,_25,_26,_27,_28,_29,_30,_31,_32,_33,_34,_35,_36,_37,_38,_39,_40,_41,_42,_43,_44,_45,_46,_47,_48,_49,_50,]]
        print(features)

        # Create a DataFrame with column names
        df = pd.DataFrame(columns=['EXT1','EXT2','EXT3','EXT4','EXT5','EXT6','EXT7','EXT8','EXT9','EXT10','EST1','EST2','EST3','EST4','EST5','EST6','EST7','EST8','EST9','EST10','AGR1','AGR2','AGR3','AGR4','AGR5','AGR6','AGR7','AGR8','AGR9','AGR10','CSN1','CSN2','CSN3','CSN4','CSN5','CSN6','CSN7','CSN8','CSN9','CSN10','OPN1','OPN2','OPN3','OPN4','OPN5','OPN6','OPN7','OPN8','OPN9','OPN10'])

        # Insert a row with values
        df = df.append(features, ignore_index=True)

        # Print the DataFrame
        print(df)

        # with open('milon.csv','w') as f:
        #     write=csv.writer(f)

        #     write.writerows(features)
        df_model='dtmodel.csv'
        kmeans = KMeans(n_clusters=5)
        k_fit = kmeans.fit(df_model)
        

        # with open('junayed.csv','w', newline='') as f:
        #   write=csv.writer(f)
        #   write.writerows(features)

        # pred= pd.read_csv('junayed.csv')

        prediction = k_fit.predict(df)
        
        st.subheader('My Personality group :'+prediction)    
        st.subheader('Personality groups')
        st.table(df)
run()