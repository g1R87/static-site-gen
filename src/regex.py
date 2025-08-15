import re
from src.functions.regex_funcs import extract_markdown_images, extract_markdown_links


def main():
    # text = "I'm a little teapot, short and stout. Here is my handle, here is my spout."
    # matches = re.findall(r"a", text)
    # print(matches) # ['teapot']

    text = "My phone number is 555-555-5555 and my friend's number is 555-555-5556. And this is an incorrect number 897676-123-1"
    matches = re.findall(r"\d{3}-\d{3}-\d{4}", text)
    # matches = re.findall(r"\d+-\d+-\d+", text)
    # print(matches) # ['555-555-5555', '555-555-5556']

    print("\n")
    # Regex for Text Between Parentheses
    text = "I have a (cat) and a (dog)"
    matches = re.findall(r"\((.*?)\)", text)
    print(matches)  # ['cat', 'dog']
    print("\n")

    # email
    text = "My email is lane@example.com and my friend's email is hunter@example.com"
    matches = re.findall(r"(\w+)@(\w+\.\w+)", text)
    # matches = re.findall(r"\w+@\w+\.\w+", text)
    print(matches)  # [('lane', 'example.com'), ('hunter', 'example.com')]
    print("\n")

    # test 1
    text = "the format of name john-doe is firstname-lastname"
    matches = re.findall(r"\w+-\w+", text)
    print(matches)
    print("\n")

    # test 2 : need to match []
    text = "[hello world] from the regex.py file. [happy coding]"
    matches = re.findall(r"(\[.*?\])", text)
    matches = re.findall(r"\[(.*?)\]", text)
    print(matches)
    print("\n")

    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))
    print("\n")

    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_links(text))
    print("\n")


if __name__ == "__main__":
    main()
