class TreeNode:
    def __init__(self,name,designation):
        self.data=(name,designation)
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

    def printTree(self,propertyName):
        if propertyName=='both':
            spaces=" "*self.get_Level()*3
            prefix=spaces+"|--"
            print(prefix+self.data[0]+'  '+'('+self.data[1]+')')
            for child in self.children:
                child.printTree(propertyName)


        if propertyName=='name':
            spaces=" "*self.get_Level()*3
            prefix=spaces+"|--"
            print(prefix+self.data[0])
            for child in self.children:
                child.printTree(propertyName)


        if propertyName=='designation':
            spaces=" "*self.get_Level()*3
            prefix=spaces+"|--"
            print(prefix+self.data[1])
            for child in self.children:
                child.printTree(propertyName)




def buildTree():
    root        =   TreeNode("Nilupul","CEO")
    #cto
    cto         =   TreeNode("Chinmay","CTO")
    infra       =    TreeNode("Vishwa","Infrastructure Head")
    infra.add_child(TreeNode("Dhaval","Cloud Manager"))
    infra.add_child(TreeNode("Abhijit","App Manager"))
    cto.add_child(infra)
    cto.add_child(TreeNode("Aamir","Application Head"))
    #Hr head
    hr          =   TreeNode("Gels","Hr Head")
    hr.add_child(TreeNode("Peter","Recruitment Manager"))
    hr.add_child(TreeNode("Waqus","Policy Manager"))
    root.add_child(cto)
    root.add_child(hr)
    return root





if __name__=="__main__":
    root=buildTree()
    # root.printTree("both")
    
#     |--Nilupul  (CEO)
#    |--Chinmay  (CTO)
#       |--Vishwa  (Infrastructure Head)
#          |--Dhaval  (Cloud Manager)
#          |--Abhijit  (App Manager)
#       |--Aamir  (Application Head)
#    |--Gels  (Hr Head)
#       |--Peter  (Recruitment Manager)
#       |--Waqus  (Policy Manager)

    # root.printTree("name")

# |--Nilupul
#    |--Chinmay
#       |--Vishwa
#          |--Dhaval
#          |--Abhijit
#       |--Aamir
#    |--Gels
#       |--Peter
#       |--Waqus

    root.printTree("designation")
    
# |--CEO
#    |--CTO
#       |--Infrastructure Head
#          |--Cloud Manager
#          |--App Manager
#       |--Application Head
#    |--Hr Head
#       |--Recruitment Manager
#       |--Policy Manager
