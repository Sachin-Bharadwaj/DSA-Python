
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self, child):
        # check for duplicates if you dont want to add dups
        child.parent = self
        self.children.append(child)

    def get_level(self, node, curr_level=0):
        '''
        return the level of a node in tree
        root has level 0
        root.children has level 1 and so on ...
        '''
        if node.parent is None:
            return curr_level
        else:
            return 1 + node.get_level(node.parent, curr_level)

    def print_tree(self):
        curr_level = self.get_level(self)
        print(" "*(curr_level)*4, self.data)
        for child in self.children:
            child.print_tree()

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("MacBook"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("ThinkPad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Samsung Galaxy"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root

if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree()
    # get level of a node
    #tmp = root.children[0]
    #print(tmp.children[0].data)
    #print(root.get_level(tmp.children[0]))