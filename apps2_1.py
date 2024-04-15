import streamlit as st
st.title('Title -> GeeksForGeeks')          # Title Tag
st.header('Header -> GeeksForGeeks')        # Header Tag
st.subheader('subheader -> GeeksForGeeks')  # subheader Tag
st.text('Text -> GeeksForGeeks')            # Text

st.markdown('# Hi')                         # Markdown
st.markdown('## Hi')
st.markdown('### Hi')
st.markdown('#### Hi')

st.markdown('Hi, I am Aman.')

st.success('Success!')                      # command if something is
                                            # submitted successfully

st.info('Information')                      # Information

st.warning('Warning!')                      # Warning
st.error('Error!')                          # Error

# if we want to display a exception that we have crreated then, we have to write

exp = ZeroDivisionError('Division not possible with 0')  #Exception
st.exception(exp)

st.exception(ZeroDivisionError('Division not possible'))


st.help(ZeroDivisionError)         # in help function we have to pass functions name and it will take you to the documentation of the function.  Help


st.write('range(1,10)')             # Write
st.write(range(1,10))

st.write('1+2+3')
st.write(1+2+3)
st.write(1*21*3)


st.code('x=10 \n'                   # Code 
        'for i in range(x):\n'
        '       print(i)')


st.checkbox('Male')                 # Checkbox
st.checkbox('Female')

if(st.checkbox('Adult')):           # checkbox with validation
    st.write('You are Adult\n')


st.radio('select : ', ('Check','Uncheck'))  # Radio

# st.radio('Select :',('Male','Female','Other'))  # Radio

radio = st.radio('Select: ',('Male','Female','Other')) 
if(radio=='Male'):                      # Radio with Validation
    st.write('You are a Male')
elif(radio=='Female'):
    st.write('You are a Female')
else:
    st.write('Other')


st.subheader('Select Box')          # Select Box

st.selectbox('Data Science: ',['Data Analysis','Machine Learning',
                               'Web Scraping','Deep Learning',
                               'Computer Vision','Image Processing'])


selectbox = st.selectbox('Data Science: ',['Data Analysis','Web Scraping','Machine Learning'])


st.write('You have Selected: ' + selectbox)


st.subheader('Multi-SelectBox')     # Multi Select Box

multislectbox = st.multiselect('Data Science: ',['Data Analysis','Web Scraping','Machine Learing','Deep Learning'])

st.write('You Have selected: ',len(multislectbox),'courses')


st.subheader('Button')

st.button('Click Me')                 # Button


if(st.button('Button')):              # Button + Validation
    st.write('Thanks for Clicking Me.')


st.subheader('Slider')

st.slider('Select the level',1,10,step=1)
vol = st.slider('Select the Volume: ',1,100)
st.write('Vol is :',vol)


st.subheader('Text Input')   # Text Input (for taking i/p from users)

st.text_input('Name: ')


age = st.text_input('Enter your Age: ')
if(age):
    st.write('Age is: ',age)

username = st.text_input('Enter your username: ')
if(username):
    st.write('Hi,',username)

password = st.text_input('Enter password: ',type='password')
if(password=='Aman@123'):
    st.write('Welcome!')


# Text Area for writing Paragraphs

st.subheader('Text Area')
text_area = st.text_area('Write About yourself.')
if(text_area):
    st.write(text_area)



st.subheader('Input Number')                # Input-Number

age = st.number_input('Enter your age: ',18,100,step=1)
if(age):
    st.write(age)


st.subheader('Input Date')                  # Input-Date
dob = st.date_input('enter your dob')
if(dob):
    st.write(dob)



st.subheader('Input Time')                  # Input-Time
time = st.time_input('enter time of your birth: ')
if(time):
    st.write(time)
    
