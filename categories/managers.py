from treebeard.ns_tree import NS_NodeManager


class CategoryManager(NS_NodeManager):

    def get_by_natural_key(self, name, depth):
        return self.get(name=name, depth=depth)