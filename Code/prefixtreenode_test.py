#!python3

from prefixtreenode import PrefixTreeNode
import unittest


class PrefixTreeNodeTest(unittest.TestCase):

    def test_init_and_properties(self):
        character = 'A'
        node = PrefixTreeNode(character)
        # Verify node character
        assert isinstance(node.character, str)
        assert node.character is character
        # Verify children nodes structure
        assert isinstance(node.children, PrefixTreeNode.CHILDREN_TYPE)
        assert len(node.children) == 0
        assert node.children == PrefixTreeNode.CHILDREN_TYPE()
        # Verify terminal boolean
        assert isinstance(node.terminal, bool)
        assert node.terminal is False

    def test_child_methods(self):
        # Create node 'A' and verify it does not have any children
        node_A = PrefixTreeNode('A')
        assert node_A.num_children() == 0
        assert node_A.has_child('B') is False
        # Verify getting child from node 'A' raises error
        with self.assertRaises(ValueError):
            node_A.get_child('B')
        # Create node 'B' and add it as child to node 'A'
        node_B = PrefixTreeNode('B')
        node_A.add_child('B', node_B)
        # Verify node 'A' has node 'B' as child
        assert node_A.num_children() == 1
        assert node_A.has_child('B') is True
        child_node = node_A.get_child('B')
        assert child_node is node_B
        # Verify adding node 'B' as child to node 'A' again raises error
        with self.assertRaises(ValueError):
            node_A.add_child('B', node_B)
        node_N = PrefixTreeNode('N')
        node_A.add_child('N', node_N)
        assert node_A.num_children() == 2
        assert node_A.has_child('N') is True
        child_node = node_A.get_child('N')
        assert child_node is node_N
