from src.htmlnode import HtmlNode

class ParentNode(HtmlNode):
    def __init__(
        self,
        tag: str,
        children: list["HtmlNode"], 
        props: dict[str, str] = None,
    ):
        super().__init__(tag, children=children, props= props)

    def to_html(self):
        if not self.tag:
            raise ValueError({"Error": "Parent Node must have a tag", "el": self})

        if not self.children:
            raise ValueError({"Error": "Parent Node must have childrens", "el": self})

        parent = f'<{self.tag}{self.props_to_html()}>'

        for child in self.children:
            parent += child.to_html()
        
        parent += f'</{self.tag}>'
        return parent
