import streamlit as st

# Title of the app
st.title("Discover Streamlit: The Easiest Way to Build Web Apps")

# Introduction
st.write("""
**Streamlit** is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. 
In just a few minutes you can build and deploy powerful data apps.
""")

# Reasons to use Streamlit
st.header("Why You Should Give Streamlit a Try")
st.write("""
### Easy to Use
If you can write Python scripts, you can build web apps with Streamlit. No web development skills required!
""")

st.write("""
### Rapid Development
Quickly prototype and deploy your applications, allowing for more iterative and collaborative work.
""")

st.write("""
### Interactive Widgets
Streamlit offers a range of widgets to make your apps interactive, from sliders and buttons to file uploads and maps.
""")

st.write("""
### Real-time Updates
Your app updates in real-time as you tweak your code, making the development process seamless and fun.
""")

# Example widget
st.header("Try It Yourself")
st.write("Move the slider to see Streamlit in action!")

# Slider widget
slider_value = st.slider("Slide me!", 0, 100, 50)
st.write(f"The slider value is: {slider_value}")

# File uploader widget
st.write("Upload a file to see how easy it is to work with files in Streamlit:")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)
    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)
    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)
    # Can be used wherever a file-like object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

# Closing note
st.write("""
Explore more about Streamlit at [streamlit.io](https://streamlit.io) and start building your own web apps today!
""")
