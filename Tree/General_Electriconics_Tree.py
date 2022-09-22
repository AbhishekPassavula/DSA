class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
    

    def get_Level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level

    def printTree(self):
        spaces=" "*self.get_Level()*3
        prefix=spaces+"|--"
        print(prefix+self.data)
        for child in self.children:
            child.printTree()





def buildTree():
    root        =   TreeNode("Electronics")
    laptop      =   TreeNode("Laptop")
    cellphones  =   TreeNode("CellPhones")
    televisions =   TreeNode("Televisions")
    root.add_child(laptop)
    root.add_child(cellphones)
    root.add_child(televisions)

    laptop.add_child(TreeNode("Dell"))
    laptop.add_child(TreeNode("HP"))
    laptop.add_child(TreeNode("Lenova"))

    cellphones.add_child(TreeNode("OnePlus"))
    cellphones.add_child(TreeNode("Samsung"))
    cellphones.add_child(TreeNode("Iphone"))


    televisions.add_child(TreeNode("LG"))
    televisions.add_child(TreeNode("VideoCon"))
    televisions.add_child(TreeNode("Sony"))

    return root





if __name__=="__main__":
    root=buildTree()
    root.printTree()
    