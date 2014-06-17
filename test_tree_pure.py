from tree_pure import BinaryTree

def test_insert():
    bt = BinaryTree(1)
    bt.insert(2)
    bt.insert(3)
    bt.insert(4)
    assert bt.contains(1) == True
    assert bt.contains(2) == True
    assert bt.contains(3) == True
    assert bt.contains(4) == True
    assert bt.contains(5) == False









