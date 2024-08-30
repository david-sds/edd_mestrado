
public class Node{

    private int datum;
    private Node left;
    private Node right;

    public Node(int value) {
        this.datum = value;
        left = null;
        right = null;
    }

    public int getDatum() {
        return datum;
    }

    public void setDatum(int datum) {
        this.datum = datum;
    }

    public Node getLeft() {
        return left;
    }

    public Node setLeft(Node left) {
        Node oldNode = this.left;
        this.left = left;
        return oldNode;
    }

    public Node getRight() {
        return right;
    }


    public Node setRight(Node right) {
        Node oldNode = this.right;
        this.right = right;
        return oldNode;
    }
}
