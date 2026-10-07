import streamlit as st
from knowledge_base import BUDGET_OPTIONS,USAGE_OPTIONS,RAM_OPTIONS,STORAGE_OPTIONS,GRAPHICS_OPTIONS,get_all_rules_text
from inference_engine import run_inference

st.set_page_config(page_title="Laptop Selection Expert System",page_icon="💻",layout="wide")

st.title("Laptop Selection Expert System")
st.write("Find the right laptop category based on your requirements.")

st.divider()

left,right=st.columns(2)

with left:
    st.subheader("Your Requirements")

    budget=st.selectbox("Budget",["-- Select Budget --"]+BUDGET_OPTIONS)
    usage=st.selectbox("Primary Usage",["-- Select Usage --"]+USAGE_OPTIONS)
    ram=st.selectbox("RAM Requirement",["-- Select RAM --"]+RAM_OPTIONS)
    storage=st.selectbox("Storage Requirement",["-- Select Storage --"]+STORAGE_OPTIONS)
    graphics=st.selectbox("Graphics Requirement",["-- Select Graphics --"]+GRAPHICS_OPTIONS)

    recommend=st.button("Get Recommendation",use_container_width=True)

    if st.button("Reset",use_container_width=True):
        st.rerun()

with right:
    st.subheader("Laptop Recommendation")

    if recommend:
        if "--" in budget or "--" in usage or "--" in ram or "--" in storage or "--" in graphics:
            st.warning("Please select all requirements.")
        else:
            user_inputs={
                "budget":budget,
                "usage":usage,
                "ram":ram,
                "storage":storage,
                "graphics":graphics
            }

            result=run_inference(user_inputs)

            st.success(result["category"])

            st.write("### Rule Applied")
            st.code(result["matched_rule_id"])

            st.write("### Explanation")
            st.write(result["reason"])

st.divider()

st.subheader("Knowledge Base")

with st.expander("View Knowledge Base Rules"):
    st.text(get_all_rules_text())

st.caption("Rule-based expert system using predefined IF-THEN rules and forward chaining.")