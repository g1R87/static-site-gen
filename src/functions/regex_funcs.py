import re

# Markdown Links
# This is a paragraph with a [link](https://www.google.com).
#
# Markdown Images
# ![alt text for image](url/of/image.jpg)


# text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

def extract_markdown_images(text: str):
    # matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text: str):
    # matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches
