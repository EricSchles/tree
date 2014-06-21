from tree_pure import BinaryTree

bt = BinaryTree(1)
for i in xrange(100):
    bt.insert(i)
bt.pretty_print()
#bt.delete(99)
print bt.contains(99)
