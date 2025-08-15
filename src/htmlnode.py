# HTMLNode in it.
# The HTMLNode class should have 4 data members set in the constructor:
# tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
# value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
# children - A list of HTMLNode objects representing the children of this node
# props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
# Perhaps counterintuitively, every data member should be optional and default to None:
# An HTMLNode without a tag will just render as raw text
# An HTMLNode without a value will be assumed to have children
# An HTMLNode without children will be assumed to have a value
# An HTMLNode without props simply won't have any attributes
# Add a to_html(self) method. For now, it should just raise a NotImplementedError. Child classes will override this method to render themselves as HTML.
# Add a props_to_html(self) method. It should return a string that represents the HTML attributes of the node. For example, if self.props is:
# {
#     "href": "https://www.google.com",
#     "target": "_blank",
# }
#
# Then self.props_to_html() should return:
#
#  href="https://www.google.com" target="_blank"
#
# Notice the leading space character before href and before target. This is important. HTML attributes are always separated by spaces.
#
# Add a __repr__(self) method. Give yourself a way to print an HTMLNode object and see its tag, value, children, and props. This will be useful for your debugging.
# Create some tests for the HTMLNode class (at least 3). I used a new file called src/test_htmlnode.py. Create a few nodes and make sure the props_to_html method works as expected.


class HtmlNode:
    def __init__(
        self,
        tag: str = None,
        value: str = None,
        children: list["HtmlNode"] = None, 
        props: dict[str, str] = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        appr = ""

        if self.props is None:
            return appr

        for key, value in self.props.items():
            appr += f' {key}="{value}"'
        return appr

    def __eq__(self, node: "HtmlNode"):
        return (
            (self.tag == node.tag)
            and (self.value == node.value)
            and (self.children == node.children)
            and (self.props == node.props)
        )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.tag}, {self.value}, children: {self.children}, {self.props})"
        # children = ""
        # for child in self.children:
        #     children += child.__repr__()
        # return f"{self.__class__.__name__}({self.tag}, {self.value}, [{children}], {self.props})"
