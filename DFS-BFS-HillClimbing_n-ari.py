import sys
import datetime


#
# BFS Algorithm
#
def BFS(root):

    nodes = []
    stack = [root] #ponemos el root en la cola
    
    #el primer nodo sera el maximo y el minimo a la vez
    min_node = stack[0]
    max_node = stack[0]
    
    while stack:
        cur_node = stack[0]
        print "Visiting node",str(cur_node), " with value", cur_node.value
        if cur_node.value < min_node.value:
            min_node = cur_node
        if cur_node.value > max_node.value:
            max_node = cur_node
        
        stack = stack[1:]
        nodes.append(cur_node)
        #add sus hijos a la cola
        for child in cur_node.get_children():
            stack.append(child)

    print '\nThe min value is: ', min_node.value, 'of the node: ', str(min_node)
    print 'The max value is: ', max_node.value, 'of the node: ', str(max_node)

    return nodes

#
# DFS Algorithm
#
def DFS(root):
    
    nodes = []
    stack = [root]#ponemos el root en la cola
    
    #el primer nodo sera el maximo y el minimo a la vez
    min_node = stack[0]
    max_node = stack[0]
    
    while stack:
        cur_node = stack[0]
        print "Visiting node",str(cur_node), " with value", cur_node.value
        if cur_node.value < min_node.value:
            min_node = cur_node
        if cur_node.value > max_node.value:
            max_node = cur_node
        
        stack = stack[1:]
        nodes.append(cur_node)
        #add sus hijos a la cola
        for child in cur_node.get_rev_children():
            stack.insert(0, child)

    print '\nThe min value is: ', min_node.value, 'of the node: ', str(min_node)
    print 'The max value is: ', max_node.value, 'of the node: ', str(max_node)

    return nodes


#
# Hill climbing Algorithm -> implementado para que siga simpre el nodo con mayor valor si el siguiente nodo es mayor
#
def HillClimbingMax(root):
    end = 0
    max_value = root.value
    cur_node = root

    #siguiendo el camino donde el siguiente nodo es el mas grande
    for child in root.get_rev_children():
        print "Visiting node",str(child), " with value", child.value
        if max_value < child.value:
            cur_node = child


    if cur_node == root:
        print 'The max value is: ', cur_node.value, 'of the node: ', str(cur_node)
        end = 1

    if end == 0:
        HillClimbingMax(cur_node)

    return end

#
# Hill climbing Algorithm -> implementado para que siga simpre el nodo con menor valor si el siguiente nodo es menor
#
def HillClimbingMin(root):
    end = 0
    min_value = root.value
    cur_node = root
    
    #siguiendo el camino donde el siguiente nodo es el mas grande
    for child in root.get_rev_children():
        print "Visiting node",str(child), " with value", child.value
        if min_value > child.value:
            cur_node = child


    if cur_node == root:
        print 'The min value is: ', cur_node.value, 'of the node: ', str(cur_node)
        end = 1
    
    if end == 0:
        HillClimbingMin(cur_node)

    return end

#
# The tree
#
class TreeNode(object):
    def __init__(self, id_, value):
        self.id = id_
        self.children = []
        self.value = value
    
    def __repr__(self):
        return "[%s]" % self.id
    
    def add_child(self, node):
        self.children.append(node)
    
    def get_children(self):
        return self.children
    
    def get_rev_children(self):
        children = self.children[:]
        children.reverse()
        return children

#
# Test tree
#
def get_example_tree():
    
    #create nodes
    root = TreeNode("a0",12323)
    
    b0 = TreeNode("b0",13224)
    b1 = TreeNode("b1",3456)
    b2 = TreeNode("b2",2134)
    
    c0 = TreeNode("c0",42345)
    c1 = TreeNode("c1",522)
    c2 = TreeNode("c2",624123)
    
    d0 = TreeNode("d0",6243)
    d1 = TreeNode("d1",62143)
    
    e0 = TreeNode("e0",6143)

    
    #add nodes
    root.add_child(b0)
    root.add_child(b1)
    root.add_child(b2)
    
    b0.add_child(c0)
    b0.add_child(c1)
    
    b1.add_child(c2)
    
    c0.add_child(d0)
    
    c2.add_child(d1)
    
    d1.add_child(e0)
    
    return root


#
# The main
#
if __name__ == "__main__":
    
    root = get_example_tree() #the tree
    
    print "\n------------------------- BFS -------------------------\n"
    start = datetime.datetime.now()
    BFS(root)
    done = datetime.datetime.now()
    elapsed = done - start
    print "\nFinished in ", elapsed.microseconds , " microseconds"
    
    print "\n------------------------- DFS -------------------------\n"
    start = datetime.datetime.now()
    DFS(root)
    done = datetime.datetime.now()
    elapsed = done - start
    print "\nFinished in ", elapsed.microseconds , " microseconds"
    
    print "\n------------------- HillClimbingMax -------------------\n"
    start = datetime.datetime.now()
    HillClimbingMax(root)
    done = datetime.datetime.now()
    elapsed = done - start
    print "\nFinished in ", elapsed.microseconds , " microseconds"
    
    print "\n------------------- HillClimbingMin -------------------\n"
    start = datetime.datetime.now()
    HillClimbingMin(root)
    done = datetime.datetime.now()
    elapsed = done - start
    print "\nFinished in ", elapsed.microseconds , " microseconds\n"


