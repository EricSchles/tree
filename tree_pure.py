class Node:
    def __init__(self,item,left=None,right=None):
        self.item = item
        self.left = left
        self.right = right

    def __str__(self):
        return repr(self.item)
class BinaryTree:
    def __init__(self,item=None,left=None,right=None):
        self.root = Node(item)
        self.root.left = left
        self.root.right = right

    def insert(self,item):
        self._insert(item,0,self.root)
         
    def _insert(self,item,counter,curr):
        if curr.left == None:
            node = Node(item)
            curr.left = node
        elif curr.right == None:
            node = Node(item)
            curr.right = node
        else:
            if counter % 2 == 0:
                self._insert(item,counter+1,curr.left)
            else:
                self._insert(item,counter+1,curr.right)
                           
    def contains(self,val):
        return self._contains(val,self.root)
    
    def _contains(self,val,start):
        if start.item == val:
            return True

        curr_left = None
        curr_right = None
        left = start.left
        right = start.right
        #while left != None or right != None:
        if left != None:
            if left.item == val:
                return True
            else:
                curr_left = left
                left = left.left
                while left:
                    if left.item == val:
                        return True
                    else:
                        left = left.left
        if right != None:
            if right.item == val:
                return True
            else:
                curr_right = right
                right = right.right
                while right:
                    if right.item == val:
                        return True
                    else:
                        right = right.right
        if curr_left != None:
            if curr_left.right != None:
                left = curr_left.right
                return self._contains(val,left)
        if curr_right != None:
            if curr_right.left != None:
                right = curr_right.left
                return self._contains(val,right)
        else:
            return False
        
            
    # def _contains(self,val,curr):
    #     #print curr.item
    #     if curr.item == val: return True
    #     else:
    #         if curr.left != None: 
    #             return self._contains(val,curr.left)
    #         else:
    #             if curr.right != None: 
    #                 return self._contains(val,curr.right)
    #             else: return False
            

    def pretty_print(self):
        self._pretty_print(self.root,0)
        
    def _pretty_print(self,node,count):
        count += 1
        if node == None:
            return
        self._pretty_print(node.left,count)
        print ("\t"*count) + "level"+str(count)+"->"+str(node.item) 
        self._pretty_print(node.right,count)


    def second_highest_node(self,node):
        if node.right != None:
            return self._second_highest_node(node)
        else:
            return None

    def _second_highest_node(self,curr):
        next_node = curr.right
        if next_node.right != None:
            return self._second_highest_node(next_node)
        else:
            return curr

    def highest(self,node):
        return self._highest(node)
        
    def _highest(self,curr):
        if curr.right != None:
            return self._highest(curr.right)
        else:
            return curr.item
    
    def second_lowest_node(self,node):
        if node.left != None:
            return self._second_lowest_node(node)
        else:
            return None
    def _second_lowest_node(self,curr):
        next_node = curr.left
        if next_node.left != None:
            return self._second_highest_node(next_node)
        else:
            return curr

    def lowest(self,node):
        return self._lowest(node)

    def _lowest(self,curr):
        if curr.left != None:
            return self._lowest(curr.left)
        else:
            return curr.item

    def delete(self,value):
        return self._delete(self.root,value,None)

    def _delete(self,curr,value,parent):
        if value == curr.item:
            if curr.left != None:
                curr.item = self.highest(curr.left)
                second_largest_node = self.second_highest_node(curr.left)
                if second_largest_node != None:
                    second_largest_node.right = None
                    return value
                else:
                    curr.left = None
                    return value 

            elif curr.right != None:
                curr.item = self.lowest(curr.right)
                second_smallest_node = self.second_lowest_node(curr.right)
                if second_smallest_node != None:
                    second_smallest_node.left = None
                    return value
                else:
                    curr.right = None
                    return value
            else:
                if parent.left.item == value:
                    parent.left = None
                    return value
                else:
                    parent.right = None
                    return value
                
        else:
            is_not_in_tree = True
            if curr.left != None:
                is_not_in_tree = False
                self._delete(curr.left,value,curr)
            if curr.right != None:
                is_not_in_tree = False
                self._delete(curr.right,value,curr)
            if is_not_in_tree:
                return None

                    
                
            

