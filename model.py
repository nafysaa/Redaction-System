import spacy
import json

# Load the fine-tuned spaCy NER model
nlp = spacy.load('fine_tuned_ner_model')
def ner_text(text):

    list=[]

    # Process the text
    doc = nlp(text)
    # Print recognized named entities
    for ent in doc.ents:
        list.append([ent.label_,ent.text])
    return list
    # print(list)
# ner_text("Hello, my name is John Doe, and I work at XYZ Corp in New York")
