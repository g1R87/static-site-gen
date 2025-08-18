import unittest

from src.htmlnode import HtmlNode
from src.leafnode import LeafNode
from src.parentnode import ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HtmlNode("This is a text node")
        node2 = HtmlNode("This is a text node")
        self.assertEqual(node, node2)

    def test_not_eq_children(self):
        p_tag = HtmlNode("p", "this is a paragraph")
        span_tag = HtmlNode("span", "the tilte", props={"class": "fw-bold"})
        node = HtmlNode("div", children=[p_tag, span_tag])
        node2 = HtmlNode("div", children=[span_tag, p_tag])
        self.assertNotEqual(node, node2)

    def test_eq_children(self):
        p_tag = HtmlNode("p", "this is a paragraph")
        span_tag = HtmlNode("span", "the tilte", props={"class": "fw-bold"})
        node = HtmlNode("div", children=[span_tag, p_tag])
        node2 = HtmlNode("div", children=[span_tag, p_tag])
        self.assertEqual(node, node2)

    def test_to_html_props(self):
        node = HtmlNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HtmlNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HtmlNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HtmlNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    def test_parent_children(self):
        testResult = "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"
        p_childrens = [
            LeafNode(None, value="This is "),
            LeafNode(tag="b", value="bolded"),
            LeafNode(None, value=" paragraph text in a p tag here"),
        ]
        parent1 = ParentNode("p", p_childrens)
        p_childrens = [
            LeafNode(None,value="This is another paragraph with "),
            LeafNode(tag="i", value="italic"),
            LeafNode(None, value=" text and "),
            LeafNode(tag="code", value="code"),
            LeafNode(None, value=" here"),
        ]
        parent2 = ParentNode("p", p_childrens)
        mainParent = ParentNode('div', [parent1, parent2])

        self.assertEqual(
            mainParent.to_html(),
            testResult,
        )


if __name__ == "__main__":
    unittest.main()
