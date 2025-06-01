import streamlit as st

def table_to_str(table_text):
    rows = table_text.strip().split('\n')
    split_rows = [row.split('\t') for row in rows]
    joined_rows = ['&'.join(cols) for cols in split_rows]
    result = '@'.join(joined_rows)
    return f'[■({result})]'

st.title("Excel spreadsheet -> Word matrix :)")

user_input = st.text_area("Paste your table here (paste from excel):", height=200)

if st.button("Format"):
    if user_input.strip():
        formatted = table_to_str(user_input)
        st.code(formatted, language="text")
    else:
        st.warning("Please enter some data.")

st.write('simply paste into word equation editor and press space')
st.write('tip: use the copy button at the end of the textbox to copy without format(recommended)')
st.write('Love from 11C')
