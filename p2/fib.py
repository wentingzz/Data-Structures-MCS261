# explanations for member functions are provided in requirements.py
from __future__ import annotations
class FibNode:
    def __init__(self, val: int):
        self.val = val
        self.parent = None
        self.children = []
        self.flag = False

    def get_value_in_node(self):
        return self.val

    def get_children(self):
        return self.children

    def get_flag(self):
        return self.flag

    def __eq__(self, other):
        return isinstance(other, FibNode) and self.val == other.val

    def removeChild(self, c):
        self.children.remove(c)
class FibHeap:
    def __init__(self):
        # you may define any additional member variables you need
        self.roots = []
        pass

    def get_roots(self) -> list:
        return self.roots

    def insert(self, val: int) -> FibNode:
        n = FibNode(val)
        self.roots.append(n)
        return n
        
    def delete_min(self) -> None:
        #merge
        n = self.find_min()
        for c in n.children:
            c.parent = None
            c.flag = False
        self.roots.remove(n)
        #improve
        self.roots += n.children
        res = {}
        while self.roots:
            cur = self.roots.pop(0)
            cl = len(cur.children)
            if cl not in res:
                res[cl] = cur
            else:
                tmp = None
                if cur.val < res[cl].val:
                    cur.children.append(res[cl])
                    res[cl].parent = cur
                    tmp = cur
                    
                else:
                    res[cl].children.append(cur)
                    cur.parent = res[cl]
                    tmp = res[cl]
                self.roots.append(tmp)
                del res[cl]
        self.roots = [x for x in res.values()]

    def find_min(self) -> FibNode:
        res = None
        for c in self.roots:
            if not res or res.val > c.val:
                res = c
        return res
    def promote(self, node):
        if node not in self.roots:
            par, node.parent = node.parent, None
            self.roots.append(node)
            node.flag = False
            if par:
                par.removeChild(node)
                if par.flag:
                    self.promote(par)
                elif par not in self.roots:
                    par.flag = True
    def decrease_priority(self, node: FibNode, new_val: int) -> None:
        self.promote(node)
        node.val = new_val