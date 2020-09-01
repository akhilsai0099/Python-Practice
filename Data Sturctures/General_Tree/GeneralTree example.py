class TreeNode:
    def __init__(self , name , designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None
    
    def add_child(self , child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self , property_name):
        if property_name == "both":
            value = self.name + f" ({self.designation})"
        elif property_name == "name":
            value = self.name
        else:
            value = self.designation


        prefix =   " " * self.get_level() * 4 + "|___" if self.parent else ""
        print(prefix + value) 
        if self.children:
            for child in self.children:
                child.print_tree(property_name)
                

def build_management_tree():
    infra_head = TreeNode("Vishwa" , "Infrastructual head")
    infra_head.add_child(TreeNode("Dhaval" , "cloud Manager"))
    infra_head.add_child(TreeNode("Abhijit" , "Application Manager"))

    CTO = TreeNode("chinmay" , "CTO")
    CTO.add_child(infra_head)
    CTO.add_child(TreeNode("Aamir" , "Application Head"))

    HR_HEAD = TreeNode("Gels" , "HR HEAD")
    HR_HEAD.add_child(TreeNode("peter" , "Recruitment Manager"))
    HR_HEAD.add_child(TreeNode("Waqas" , "Policy Manager"))

    CEO = TreeNode("Nilupul" , "CEO")
    CEO.add_child(CTO)
    CEO.add_child(HR_HEAD)

    return CEO

if __name__ == '__main__':
    root_node = build_management_tree()

    root_node.print_tree("name") # prints only name hierarchy
    print('')
    print()
    print()
    root_node.print_tree("designation") # prints only designation hierarchy
    print()
    print()
    print()
    root_node.print_tree("both") # prints both (name and designation) hierarchy

    
