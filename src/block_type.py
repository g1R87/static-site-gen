from enum import Enum
from src.parentnode import ParentNode


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading",
    CODE = "code",
    QUOTE= "quote",
    UNORDERED_LIST = "unordered_list",
    ORDERED_LIST = "ordered_list",

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
            #
