import streamlit as st
import requests
import pandas as pd

def redact_request(payload):
    response = requests.post("http://localhost:5000/redact", json=payload)
        
    if response.status_code == 200:
        data = response.json()
        redacted_text = data['redacted_text']
        redaction_map = data['redaction_map']

        st.subheader("Redacted Text:")
        st.write(redacted_text)

        st.subheader("Redaction Map:")
        st.write(redaction_map)
    else:
        st.error("Error occurred while redacting text.")

st.title("Redaction Tool")
# Get the input text or CSV file from the user.
input_text_or_csv_file = st.selectbox("Input text or CSV file", ["Text", "CSV file"])

if input_text_or_csv_file == "Text":
    input_text = st.text_input("Enter the text to be redacted:")
else:
    input_csv_file = st.file_uploader("Upload the CSV file to be redacted:",type=["csv"])
    if input_csv_file is not None:
        df = pd.read_csv(input_csv_file)
        st.subheader("Uploaded CSV File:")
        st.write(df)

if st.button("Redact"):
    if input_text_or_csv_file == "Text":
        payload = {"text": input_text}
        redact_request(payload)
    else:
        payload = {"text": ""}
        if input_csv_file is not None:
            # Combine text from CSV columns
            csv_text=''
            for column in df.columns:
                csv_text = ' '.join(df[column])+' '  # Change 'Column_Name' to the actual column name
            payload["text"] += "\n" + csv_text
        redact_request(payload)
