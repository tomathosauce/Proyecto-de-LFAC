from enum import Enum

NodeType = Enum(
    "NodeType", [
        'InfixBinaryExpression',
        'PostFixBinaryExpression',
        'UnaryExpression',
        'AssignmentStatement',
        'IfStatement',
        'LanguageFunctionCall',
        'Value',
        'Variable'
    ]
)

class Node:
    def __init__(self,type,children=None,leaf=None):
         self.type = type
         if children:
              self.children = children
         else:
              self.children = []
         self.leaf = leaf
    
    @property
    def has_children(self):
        return len(self.children) > 0