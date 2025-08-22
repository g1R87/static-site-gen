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
