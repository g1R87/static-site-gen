from src.htmlnode import HtmlNode

class LeafNode(HtmlNode):
    def __init__(
        self,
        tag: str | None,
        value: str,
        props: dict[str, str] = None,
    ):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")

        if not self.tag:
            return self.value
        
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

