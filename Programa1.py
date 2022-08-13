import streamlit as st   
st.title("10 Cool Beginner Python Tricks That Will Make Your Life Easier") 
st.header ("Simple but effective tips for every python lovers")
st.image ('https://miro.medium.com/max/700/1*5IFgojJ4nU8f0YKTcjWDrg.jpeg')
st.caption("<h4 style='text-align: center';'>Photo by Miesha Maiden from Pexels</h4>", unsafe_allow_html=True)
st.write("<h2><p>The compactness of Python can make a developer&rsquo;s life a lot easier when writing lines and lines of code. But there are some lesser-known Python tricks that can surprise you with their amazing capabilities.</p></h2>", unsafe_allow_html=True)
st.write("<h2><p>In today’s article, I will discuss 10 Python tips and tricks that will be really helpful for beginners to write more compact code. Knowing these tips and tricks will definitely save you some valuable time.</p></h2>", unsafe_allow_html=True)

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

st.header('2. Splitting a string')
st.write("<h2><p>If you want to split the components of a string into a list you can do that easily using the split() function in python. This will make the string operations a lot easier!<p></h2>", unsafe_allow_html=True)
st.header('Example')
code = '''string = “hello world”
string.split()'''
st.code(code, language='python')
st.write("<h2><p>Output</p></h2>", unsafe_allow_html=True)
st.code("[‘hello’, ‘world’]")

st.header('3. Reversing a string')
st.write("<h2><p>If you want to reverse a given string, you can do that with only one line of code using the negative indexing of the string.<p></h2>", unsafe_allow_html=True)
st.header('Example')
code = '''str=”hello world!”
a=str[::-1]
print(a)'''
st.code(code, language='python')
st.write("<h2><p>Output</p></h2>", unsafe_allow_html=True)
st.code("[!dlrow olleh]")

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
