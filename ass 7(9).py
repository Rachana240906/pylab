import re

def tokenize(text):
    patterns = {
        "url": r"https?://(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}",
        "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "date": r"\b(?:\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}|\d{4}[-/.]\d{1,2}[-/.]\d{1,2})\b",
        "number": r"\b(?:\d{1,3}(?:,\d{3})*|\d+\.\d+|\d+/\d+)\b",
        "social_handle": r"@[a-zA-Z0-9_]+",
        "punctuation": r"[.,!?;:()\[\]{}]",
        "word": r"[\w\u0C00-\u0C7F]+"
    }
    
    combined_pattern = "|".join(f"(?P<{key}>{pattern})" for key, pattern in patterns.items())
    
    tokens = []
    for match in re.finditer(combined_pattern, text):
        for key, value in match.groupdict().items():
            if value:
                tokens.append((key, value))
    
    return tokens

text = input("Enter Telugu text to tokenize: ")
tokens = tokenize(text)
print(tokens)
