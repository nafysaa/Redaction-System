from flask import Flask, request, jsonify,render_template
import pandas as pd
import model
import redacted
import csv

app = Flask(__name__)

@app.route('/redact', methods=['POST'])
def redact_text():
    data = request.get_json() # Retrieve form data
    text = data.get('text', '')  # Get text from the form data
    entity=model.ner_text(text)
    
    redacted.inputs(text,entity)
    redacted_text, redaction_map = redacted.inputs(text,entity)

    response_data = {
        'redacted_text': redacted_text,
        'redaction_map': redaction_map
    }

    return jsonify(response_data)

@app.route('/redact-csv', methods=['POST'])
def redact_csv():
    file = request.files['file']  # Retrieve the uploaded CSV file
    # file="default.csv"
    # text = ''
    final=[["Original text","Redacted text","Place holder"]]
    
    # if file:
    #     print("yess")
    if file:
        # Read the CSV file and concatenate its content
        # chunk_size=1
        df = pd.read_csv(file)
        # text = ' '.join(df.values.flatten())
        # return jsonify(df)
        # number_columns=len(df.columns)
        # return jsonify(number_columns)
        for row in df:
            # return jsonify(row)
            # row=row
            # return str(row)
            entity=model.ner_text(str(row))
            # redacted.inputs(row,entity)
            redacted_text, redaction_map = redacted.inputs(row,entity)
            final.append([row,redacted_text, redaction_map])
        dft=pd.DataFrame(final[1:],columns=final[0])
        dft.to_csv("redacted_csv.csv",index=False)
            
            

    # redacted_text, redaction_map = redact_function(text)

    # response_data = {
    #     'redacted_text': redacted_text,
    #     'redaction_map': redaction_map
    # }
    return jsonify(final[1:])

def redact_function(text):
    # Implement your redaction logic here
    # This is just a placeholder example
    redacted_text = "[REDACTED]"
    redaction_map = {'[REDACTED]': text}
    return redacted_text, redaction_map

if __name__ == '__main__':
    app.run(debug=True)
