from tree_pure import BinaryTree

bt = BinaryTree(1)
for i in xrange(100):
    bt.insert(i)
bt.pretty_print()

print bt.contains(99)
