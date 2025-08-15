import unittest

from src.htmlnode import HtmlNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HtmlNode("This is a text node")
        node2 = HtmlNode("This is a text node")
        self.assertEqual(node, node2)

    def test_not_eq_children(self):
        p_tag = HtmlNode("p", "this is a paragraph")
        span_tag = HtmlNode("span", "the tilte", props= {'class' : 'fw-bold'})
        node = HtmlNode("div", children=[p_tag, span_tag])
        node2 = HtmlNode("div", children=[span_tag, p_tag])
        self.assertNotEqual(node, node2)

    def test_eq_children(self):
        p_tag = HtmlNode("p", "this is a paragraph")
        span_tag = HtmlNode("span", "the tilte", props= {'class' : 'fw-bold'})
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
      

if __name__ == "__main__":
    unittest.main()
