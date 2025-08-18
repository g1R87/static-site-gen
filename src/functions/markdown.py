
import re

def extract_title(markdown):
    matches = re.findall(r"# (.*)", markdown)
    if not matches:
        raise ValueError("Markdown has no title")

    return matches[0]
    
