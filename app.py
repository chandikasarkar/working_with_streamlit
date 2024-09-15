import streamlit as st
st.title('hello this is chandika')
st.header('an aspiring data scienctis')
st.subheader('python developer')
st.text('Sql,data anlytics')
st.text('-'*100)

st.markdown('# Hi')
st.markdown('## Hi')
st.text('-'*100)

st.success('Success!')
st.info('Information!')
st.warning('Warning!')
st.error('Error!')
st.text('-'*100)

st.exception(ZeroDivisionError('division not possible with zero'))
st.help(ZeroDivisionError)
st.text('-'*100)

st.write("range(1,10)")
st.write(range(1,10))
st.text('-'*100)

st.code('x=10\n'
        'for i in range(0,x)\n'
        '    print(i)')
st.text('-'*100)

st.checkbox('male')
st.checkbox('female')
st.checkbox('prefer not to say')
st.text('-'*100)

if(st.checkbox('age >=18')):
   st.write("You are an adult")
st.text('-'*100)

st.radio('select an option:\n Are you a student?',('yes','no'))
st.text('-'*100)

radioButton= st.radio('select you Gender :',('Male','Female'))
if(radioButton== 'Male'):
   st.write("Your gender is Male")
elif(radioButton== 'Female'):
   st.write("Your gender is Female")
st.text('-'*100)

st.subheader('Select Box')
select_box=st.selectbox("Select your area of interest in Data Science: ",['Data Analysis','ML','AI','SQL','NPL'])
st.write("you have selected",select_box)
st.text('-'*100)

st.subheader('multiSelect Box')
multiselect_box=st.multiselect("Select your area of interest in Data Science: ",['Data Analysis','ML','AI','SQL','NPL'])
st.write("you have selected",len(multiselect_box),'topics')
st.text('-'*100)

st.button('click here')
st.text('-'*100)

vol=st.slider('select your communication proficiency',0,10,step=2)
if(vol<4):
   st.write("Low")
elif(vol==5):
   st.write("Medium")
elif(vol>5):
   st.write("High")
st.text('-'*100)

name=st.text_input("Enter your name")
if(name):
    st.write('hello! ',name)
st.text('-'*100)

uname=st.text_input("Enter username")
Pass= st.text_input("Enter password",type='password')
about=st.text_area("Write about yourself in 100 words")
age=st.number_input("Enter your age",18,110)
date=st.date_input("Enter date")
time=st.time_input("Enter time")