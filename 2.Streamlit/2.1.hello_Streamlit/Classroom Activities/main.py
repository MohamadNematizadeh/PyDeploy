import streamlit as st
st.title("my Streamlit App")
with st.sidebar :
     agree = st.checkbox("App streamlit")
col1,col2 = st.columns(2)
with col1:
    st.write("Hello world")
    my_btn = st.button("click my")
    if my_btn:
        st.write("سلام")
    else:
        st.write("خداحافظ")
    st.text_input("FirstName")
    st.text_input("lastName")
with col2:
    weight = st.number_input("Enter yore weight (kg)")
    height = st.number_input("Enter yore height (cm)")
    btn_calculate_bmi = st.button("calculate bmi ")
    if btn_calculate_bmi:
        bmi = weight / ((height/100)**2)
        st.info(bmi)
        if bmi < 18.5:
            st.write("لاغر")
        elif 18.5 < bmi < 25:
                st.write("وزن ایده عالی داری")
        elif 25 < bmi < 30:
                st.write("چاق")        
