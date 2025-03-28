import streamlit as st 
st.set_page_config(page_title="growth midset project")
st.title ("🚀✨Growth Midset Challenge: Web App with streamlit✨🚀")

st.header(" Wellcome to your Growth Journey!")
st.write ("Embrace challenges, learn from mistake, and unlock your fulll potential. this AI-powered app help You build A growth mindset with reflection, challenges and achievement!✨🪄💫")

st.header("Today Growth Mindset Quote ")
st.write("success is not final, failure is not fatal: it is the courage to continue that counts")
st.header("Whats Your Challenge Today?")
user_input =st.text_input("describe a challenge your facing:")

if user_input:
    st.succcess(f"you facing: {user_input}. keep pushing forword toword your goal!")
else:     
    st.waring =("Tell Us About Your Challenge To Get Started!")

st.header("Reflect On Your Learning")
reflection= st.text_area ("Write Your Reflections Here:")


if reflection:
    st.success("great insight! your reflection :{reflection}")
else:
    st.info("reflecting on past experience help you grow! share your difficulties")                   

st.header("🎉celebrate your wins!🎉")
acheivment =st.text_input ("share something you recently accomplished:")
if acheivment:
    st.success("amazing you acheivment:{acheivment}")
else:
    st.info("😎big or small, every acheivment counts! share one now😎")

st.write("-------")    
st.write("😇keep believing in yourself growth is journey, not a destination!😇")
st.write("Build with ❤️ by [LEEZA](https://github.com/LeezaSarwar)")

