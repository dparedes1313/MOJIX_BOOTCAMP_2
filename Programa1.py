import streamlit as st  
####SIDE BAR ################################################################# 
st.sidebar.title("10 Cool Beginner Python Tricks That Will Make Your Life Easier")
# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    ) 
#st.sidebar.checkbox('contenido')
#st.sidebar.checkbox('contacto')
page_names = ['Contenido','Contacto']
page = st.sidebar.radio('navigation', page_names) 
st.sidebar.write("The Variable 'Page' returns:**",page)

if page = 'Contenido':
   st.sidebar.subheader ('Welcome to the Checkbox page!')
   st.sidebar.write("Nice to see You! :wave:")
   check = st.sidebar.checkbox("Click Here")
    st.sidebar.write('state of the checkbox',check)

else:       
st.sidebar.header('1. Walrus operator')
st.sidebar.header('2. Splitting a string')
st.sidebar.header('3. Reversing a string')
st.sidebar.header('4. Merging two dictionaries')
st.sidebar.header('5.The zip() function')
st.sidebar.header('6. Assigning multiple list values to a variable')
st.sidebar.header('7. Remove duplicate list items')
st.sidebar.header('8. Lambda function')
st.sidebar.header('9. Swapping variable value')
st.sidebar.header('10. Use a password in your code')
####MAIN PAGE #################################################################
st.title("10 Cool Beginner Python Tricks That Will Make Your Life Easier")
st.header ("Simple but effective tips for every python lovers")
st.image ('https://miro.medium.com/max/700/1*5IFgojJ4nU8f0YKTcjWDrg.jpeg')
st.caption("<h4 style='text-align: center';'>Photo by Miesha Maiden from Pexels</h4>", unsafe_allow_html=True)
st.write("<h2><p>The compactness of Python can make a developer&rsquo;s life a lot easier when writing lines and lines of code. But there are some lesser-known Python tricks that can surprise you with their amazing capabilities.</p></h2>", unsafe_allow_html=True)
st.write("<h2><p>In today’s article, I will discuss 10 Python tips and tricks that will be really helpful for beginners to write more compact code. Knowing these tips and tricks will definitely save you some valuable time.</p></h2>", unsafe_allow_html=True)
 #####################################################################
st.header('1. Walrus operator')
st.write("<h2><p>The&nbsp;<code><strong>Walrus</strong></code><strong>&nbsp;or&nbsp;</strong><code><strong>:=</strong></code>&nbsp;operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.</p></h2>", unsafe_allow_html=True)
st.header('Example')
st.write("<h2><p>If we want to check and print the length of a list:</p></h2>", unsafe_allow_html=True)
code = '''Mylist = [1,2,3]
if(l := len(mylist) > 2)
print(l)'''
st.code(code, language='python')
st.write("<h2><p>Output</p></h2>", unsafe_allow_html=True)
st.code("3")
 #####################################################################
st.header('2. Splitting a string')
st.write("<h2><p>If you want to split the components of a string into a list you can do that easily using the split() function in python. This will make the string operations a lot easier!<p></h2>", unsafe_allow_html=True)
st.header('Example')
code = '''string = “hello world”
string.split()'''
st.code(code, language='python')
st.write("<h2><p>Output</p></h2>", unsafe_allow_html=True)
st.code("[‘hello’, ‘world’]")
 #####################################################################
st.header('3. Reversing a string')
st.write("<h2><p>If you want to reverse a given string, you can do that with only one line of code using the negative indexing of the string.<p></h2>", unsafe_allow_html=True)
st.header('Example')
code = '''str=”hello world!”
a=str[::-1]
print(a)'''
st.code(code, language='python')
st.write("<h2><p>Output</p></h2>", unsafe_allow_html=True)
st.code("[!dlrow olleh]")
 #####################################################################
st.header('4. Merging two dictionaries')
st.write("<h2><p>This amazing trick will help you merge two dictionaries with just 1 line of code. We just need to use ** in front of the name of the two dictionaries like below two merge them into a single dictionary:<p></h2>", unsafe_allow_html=True)
st.header('Example')
code = '''d1 = {“a”: 10, “b”:20}
d2 = {“c”: 30, “d”:40}
d3 = {**d1, **d2}
print(d3)'''
st.code(code, language='python')
st.write("<h2><p>Output</p></h2>", unsafe_allow_html=True)
st.code("{‘a’: 10, ‘b’: 20, ‘c’: 30, ‘d’: 40}")
 #####################################################################
st.header('5.The zip() function')
st.write("<h2><p>The zip() function in python can make your life a lot easier when working with lists and dictionaries. It is used to combine several lists of the same length.<p></h2>", unsafe_allow_html=True)
st.header('Example')
code = '''colour = [“red”, “yellow”, “green”]
fruits = [‘apple’, ‘banana’, ‘mango’]
for colour, fruits in zip(colour, fruits):
print(colour, fruits)'''
st.code(code, language='python')
st.write("<h2><p>Output</p></h2>", unsafe_allow_html=True)
code = '''red apple
yellow banana
green mango'''
st.code(code, language='python')
st.write("<h2><p>The zip() function can also be used for combining two lists into a dictionary. This method can be really helpful while grouping data from the list.<p></h2>", unsafe_allow_html=True)
st.header('Example')
code = '''students = [“Rajesh”, “kumar”, “Kriti”]
marks = [87, 90, 88]
dictionary = dict(zip(students, marks))
print(dictionary)'''
st.code(code, language='python')
st.write("<h2><p>Output</p></h2>", unsafe_allow_html=True)
code = '''{‘Rajesh’: 87, ‘kumar’: 90, ‘Kriti’: 88}'''
st.code(code, language='python')
 #####################################################################
st.header('6. Assigning multiple list values to a variable')
st.write("<h2><p>If you want to assign some specific values of a list to a variable and all the remaining values to another variable in a list format, you can use the following technique:<p></h2>", unsafe_allow_html=True)
st.header('Example')
code = '''mylist = [1,2,3,4,5]
a,*b = mylist
print(f”a =”,a)
print(f”b =”,b)'''
st.code(code, language='python')
st.write("<h2><p>Output</p></h2>", unsafe_allow_html=True)
code = '''a = 1
b = [2, 3, 4, 5]'''
st.code(code, language='python')
 #####################################################################
st.header('7. Remove duplicate list items')
st.write("<h2><p>Do you have duplicate items in your list which you want to remove? You can do that with only one line of code using the set() function.<p></h2>", unsafe_allow_html=True)
st.header('Example')
code = '''mylist = [1,1,1,2,2,3,3,4,4,5,6,7,7,8,9]
newlist = set(mylist)
print(newlist)'''
st.code(code, language='python')
st.write("<h2><p>Output</p></h2>", unsafe_allow_html=True)
code = '''{1, 2, 3, 4, 5, 6, 7, 8, 9}'''
st.code(code, language='python')
 #####################################################################

st.header('8. Lambda function')
st.write("<h2><p>If you need a function that is not very complicated, it can be done easily in one line using lambda. They are also called anonymous functions and are used heavily in data science and web development.<p></h2>", unsafe_allow_html=True)
st.header('Example')
st.write("<h2><p>Let’s say you want to write a function to multiply two numbers. Instead of writing a conventional function, you can do that in one line using :<p></h2>", unsafe_allow_html=True)
code = '''mul = lambda a,b: a*b
mul(5,6)'''
st.code(code, language='python')
st.write("<h2><p>Output</p></h2>", unsafe_allow_html=True)
code = '''30'''
st.code(code, language='python')
 #####################################################################

st.header('9. Swapping variable value')
st.write("<h2><p>One of the first programs that we learn while learning about variables is swapping the values of two variables. In python you can achieve that with one line of code:<p></h2>", unsafe_allow_html=True)
st.header('Example')
code = '''a = 100
b = 200
a,b = b,a
print(f’a = ‘,a)
print(f’b = ‘,b)'''
st.code(code, language='python')
st.write("<h2><p>Output</p></h2>", unsafe_allow_html=True)
code = '''a = 200
b = 100'''
st.code(code, language='python')
 #####################################################################
st.header('10. Use a password in your code')
st.write("<h2><p>This python trick is amazing for securing your code with a password. We will use the getpass() function from the library getpass which encodes your input. This will prevent anyone from running the code without a password. Isn’t that cool!<p></h2>", unsafe_allow_html=True)
st.header('Example')
code = '''from getpass import getpass
password = getpass(“password: “)
if password == “abcd”:
    print(“welcome strnger!”)
else:
    print(“wrong password”)'''
st.code(code, language='python')
st.write("<h2><p>Output</p></h2>", unsafe_allow_html=True)
code = '''password: **** [abcd]
Welcome stranger!
Password: **** [abdc]
Wrong password'''
st.code(code, language='python')
st.header('Conclusion')
st.write("<h2><p><p> These were a few amazing Python tips and tricks which will make your work a lot easier while coding. There are many more shortcuts like these that you can explore from the official documentation or any other website.</p><p><strong><em>Note:&nbsp;</em></strong><em>This article contains an affiliate link. This means that if you click on it and choose to buy the resource I linked above, a small portion of your subscription fee will go to me.</em></p><p><em>However, the recommended resource is experienced by me and helped me in my data science career journey.</em></p><p></h2>", unsafe_allow_html=True)