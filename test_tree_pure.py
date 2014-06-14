from tree_pure import BinaryTree

def test_add_right():
    tree = BinaryTree(1)
    tree.add_right(2)
    tree.add_right(3)
    assert tree.contains(1) == True
    assert tree.contains(2) == True
    assert tree.contains(3) == True
    assert tree.contains(4) == False

def test_add_left():
    tree = BinaryTree(1)
    tree.add_right(2)
    tree.add_right(3)
    assert tree.contains(1) == True
    assert tree.contains(2) == True
    assert tree.contains(3) == True
    assert tree.contains(4) == False






