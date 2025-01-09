import re
from pathlib import Path

print("This is part of the script")

data_path = Path(__file__).parent / "data" / "ml_text_raw.txt"

with open(data_path/"ml_text_raw.txt", 'r') as file:
    raw_text = file.read()
    
text_fixed_spacing = re.sub(r"\s+"," ",raw_text)

text_fixed_spacing.split(". ")

sentences = [text.strip().capitalize() for text in text_fixed_spacing.split(".")]
sentences = sentences[:-1]
sentences

clean_text = ".\n".join(sentences)
print(clean_text)

with open("data/cleaned_ml_text.txt", "w") as file:
    file.write(clean_text)