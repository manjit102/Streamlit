import streamlit as st

st.title('Title -> GeeksforGeeks')                 # Title
st.header('Header -> GeeksforGeeks')               # Header
st.subheader('Subheader -> GeeksforGeeks')         # Subheader
st.text('Text -> GeeksforGeeks')                   # Text

st.markdown('# Hi')                                # Markdown
st.markdown('## Hi')
st.markdown('### Hi')
st.markdown('#### Hi')
st.markdown('##### Hi')
st.markdown('###### Hi')
st.markdown('Hi')

st.success('Success!')                     # Success
st.info('Information!')                        # Info
st.warning('Warning!')                     # Warning
st.error('Error!')                         # Error

# exp = ZeroDivisionError('Division not possible with 0')
# st.exception(exp)

st.exception(ZeroDivisionError('Div not possible'))    # Exception

st.help(ZeroDivisionError)                             # Help

st.write('range(1,10)')                                # Write
st.write(range(1,10))
st.write('1+2+3+4')
st.write(1+2+3+4)

# st.code('x = 10'
#         'for i in range(x):'
#         '   print(i)')

st.code('x = 10\n'                                      # Code
        'for i in range(x):\n'
        '\tprint(i)')

st.checkbox('Male')                                     # Checkbox
# st.checkbox('Female')

if(st.checkbox('Adult')):                               # Checkbox with Validation
    st.write('You are an Adult')

# st.radio('select : ',('Male', 'Female','Other'))
radioButton = st.radio('Select : ', ('Male', 'Female', 'Other'))      # Radio Button
if (radioButton == 'Male'):
    st.write('You are male')
elif (radioButton == 'Female'):
    st.write('You are female')
elif (radioButton == 'Other'):
    st.write('You are an other gender')

st.subheader('Select Box:')                       # SelectBox
selectBox = st.selectbox('Data Science : ', ('Data Analysis','Web Scraping', 'Machine Learning',
                                 'Deep Learning', 'Natural Language Processing',
                                 'Computer Vision', 'Image Processing'))
st.write('You have selected : ', selectBox)

# st.subheader('Multi Select Box:')                       # MultiSelectBox
# mulselBox = st.multiselect('Data Science : ', ('Data Analysis','Web Scraping', 'Machine Learning',
#                                  'Deep Learning', 'Natural Language Processing',
#                                  'Computer Vision', 'Image Processing'))
# st.write('You have selected : ', len(mulselBox), mulselBox)

st.subheader('Multi Select Box:')                       # MultiSelectBox
mulselBox = st.multiselect('Data Science : ', ('Data Analysis','Web Scraping', 'Machine Learning',
                                 'Deep Learning', 'Natural Language Processing',
                                 'Computer Vision', 'Image Processing'))
st.write('You have selected : ', len(mulselBox), 'Courses')

st.subheader('Button')                                  # Button
if(st.button('Click me')):
    st.write('Thanks for clicking me')

st.subheader('Button')                                  # Slider
vol = st.slider('Select the Volume',0,100,step =1)
st.write('Volume is : ', vol)

st.subheader('Text Input')                                  # Text Input
name = st.text_input('Name : ')
if (name):
    st.write('Hi, ', name)
username = st.text_input('Username : ')
password = st.text_input('Password : ', type = 'password')

st.subheader('Text Area')                                  # Text Area
textArea = st.text_area('Write something interesting about yourself')

st.subheader('Input Number')                                  # Input Number
st.number_input('Select your age : ',18,102)

st.subheader('Input Date')                                  # Input Date
st.date_input("Date")

st.subheader('Input Time')                                  # Input Time
st.time_input('Time')
