using System;

class Node
{
    public int Value;
    public Node Left, Right;

    public Node(int value)
    {
        Value = value;
        Left = Right = null;
    }
}

class BinaryTree
{
    private Node root;

    public BinaryTree()
    {
        root = null;
    }

    public void Insert(int value)
    {
        root = InsertRec(root, value);
    }

    private Node InsertRec(Node root, int value)
    {
        if (root == null)
        {
            root = new Node(value);
            return root;
        }

        if (value < root.Value)
            root.Left = InsertRec(root.Left, value);
        else if (value > root.Value)
            root.Right = InsertRec(root.Right, value);

        return root;
    }

    public bool Search(int value)
    {
        return SearchRec(root, value);
    }

    private bool SearchRec(Node root, int value)
    {
        if (root == null)
            return false;

        if (root.Value == value)
            return true;

        return value < root.Value ? SearchRec(root.Left, value) : SearchRec(root.Right, value);
    }

    public void PrintInOrder()
    {
        InOrderRec(root);
        Console.WriteLine();
    }

    private void InOrderRec(Node root)
    {
        if (root != null)
        {
            InOrderRec(root.Left);
            Console.Write(root.Value + " ");
            InOrderRec(root.Right);
        }
    }
}

class Program
{
    static void Main()
    {
        BinaryTree tree = new BinaryTree();
        
        tree.Insert(50);
        tree.Insert(30);
        tree.Insert(70);
        tree.Insert(20);
        tree.Insert(40);
        tree.Insert(60);
        tree.Insert(80);

        //---------------------------------------------------------------- 
        //---------------------------------------------------------------- 
        
        Console.WriteLine($"Árbol en orden ascendente:\n");
        tree.PrintInOrder();
    }
}