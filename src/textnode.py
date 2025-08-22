from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

    def get_tag(self):
        match self:
            case self.BOLD:
                return 'b'
            case self.TEXT:
                return ''
            case self.ITALIC:
                return 'i'
            case self.CODE:
                return 'code'
            case self.LINK:
                return 'a'
            case self.IMAGE:
                return 'img'
            # case _:
            #     print("It's neither 10 nor 20")
            #
    def get_delimiter(self):
        match self:
            case self.BOLD:
                return '**'
            case self.TEXT:
                return ''
            case self.ITALIC:
                return '_'
            case self.CODE:
                return '`'
            case self.LINK:
                return 'a'
            case self.IMAGE:
                return 'img'
            # case _:
            #     print("It's neither 10 nor 20")


class TextNode:
    def __init__(self, text:str, text_type: TextType, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, node):
        return (
            (self.text == node.text)
            and (self.text_type == node.text_type)
            and (self.url == node.url)
        )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.text}, {self.text_type.value}, {self.url})"
