from src.textnode import TextNode, TextType
from src.htmlnode import HtmlNode
from src.leafnode import LeafNode
from src.parentnode import ParentNode
from src.functions import transform
from src.functions import node_split
from src.functions.text_to_textnodes import text_to_textnodes
import src.functions.block as md
from pprint import pprint


def main():
#     heading = "##### Heading 3"
#     print(md.is_heading_block(heading))
#     ordered_list_block = """1. First item
# 2. Second item
# 3. Third item"""
#     print(md.is_ordered_block(ordered_list_block))
#

    markdown_block = "``` this is a bad code block ``"
    print(md.block_to_block_type(markdown_block))
    return

    codeblock = """```

print(md.is_ordered_block(ordered_list_block))
print(md.is_unordered_block(unordered_list_block))
return
```"""
    print(md.is_code_block(codeblock))
    return



    unordered_list_block = """- First item
- Second item
- Third item"""
    print(md.is_unordered_block(unordered_list_block))
    return








    # text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    # nodes = text_to_textnodes(text)
    # print(nodes)
    # return
    #
    # node = TextNode(
    #     "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    #     TextType.TEXT,
    # )
    # print(node)
    # new_nodes = node_split.split_nodes_link([node])
    # print(new_nodes)
    # return
    # [
    #     textnode("this is text with a link ", texttype.text),
    #     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
    #     TextNode(" and ", TextType.TEXT),
    #     TextNode(
    #         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
    #     ),
    # ]



    text = "`This is` text with a `code block` word"
    # text = "This is text with a `code block` word"
    c = "`"
    # print(text.split(c))
    # print(0 % 2)

    # parts = []
    # parts = node_split.split_partition(text, c)
    # print(parts)
    # print(text.count(c))
    # print(node_split.get_filtered_list(text, c))
    #
    # node = TextNode("This is text with a `code block` word", TextType.TEXT)
    # node = TextNode( "This is text with a **bolded** word and **another**", TextType.TEXT)
    # # # print(node_split.split_nodes_delimiter([node], c, TextType.CODE))
    # c = "**"
    # print(node_split.split_nodes_delimiter([node], c, TextType.BOLD))



# text = "This is some anchor text"
# url = "https://www.boot.dev"
# text_node = TextNode(text, TextType.TEXT, url)
# print(text_node)

# checking htmlnode
# html_node3 = HtmlNode('p', 'this is a line of text', [], {"class": "text-decoration-none"})
# html_node2 = HtmlNode('div', "the heading", children=[html_node3], props={"class": "header"})
# html_node = HtmlNode('div', 'this is the heading', [html_node2], {"class": "fw-bold", "data-user" : "Admin User"})
# print(html_node.props_to_html())
# print(html_node)

# checking leaf
# node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
# # "<a href="https://www.google.com">Click me!</a>"
# print(node)

# checking parent
# node = ParentNode(
#     "p",
#     [
#         LeafNode("b", "Bold text"),
#         LeafNode(None, "Normal text"),
#         LeafNode("i", "italic text"),
#         LeafNode(None, "Normal text"),
#     ],
# )
# print(node.to_html())

# node = TextNode("This is a text node", TextType.LINK, 'www.google.com')
# html_node = transform.text_node_to_html_node(node)
# print(html_node.to_html())


main()
