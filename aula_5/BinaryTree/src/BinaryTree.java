
public class BinaryTree {

    private Node root;

    public Node getRoot() {
        return root;
    }

    public void setRoot(Node root) {
        this.root = root;
    }

    public BinaryTree() {
        root = null;
    }

    public boolean isEmpty() {
        return root == null;
    }



    /* INSERT */
    private void insert(Node node, Node aux) // Método recursivo
    {
        if(node.getDatum() < aux.getDatum()) {
            if(aux.getLeft() == null)
                aux.setLeft(node);
            else
                insert(node, aux.getLeft());
        }
        if(node.getDatum() > aux.getDatum()) {
            if(aux.getRight() == null)
                aux.setRight(node);
            else
                insert(node, aux.getRight());
        }
    }
    public void insert(int value, boolean shouldBalance) // Escolhe balanceamento + Verificações únicas
    {
        Node node = new Node(value);
        if(!isEmpty()) {
            if(search(value) == null) {
                insert(node, root);
                if(shouldBalance)
                    searchUnbalance();
            } else {
                System.out.println("There is already a node with value " + value + ".");
            }
        } else
            setRoot(node);
    }



    /* SEARCH */
    private Node search(int value, Node node)
    {
        if(node != null && value != node.getDatum())
            if(value >= node.getDatum())
                return search(value, node.getRight());
            else
                return search(value, node.getLeft());
        return node;
    }
    public Node search(int value) { // Só valor de parametro
        return search(value, root);
    }

    /* SEARCH PARENT */
    private Node searchParent(int value, Node aux)
    {
        if(aux != null) {
            if (aux.getLeft() != null)
                if (aux.getLeft().getDatum() == value)
                    return aux;

            if (aux.getRight() != null)
                if (aux.getRight().getDatum() == value)
                    return aux;

            if (value >= aux.getDatum())
                return searchParent(value, aux.getRight());
            else
                return searchParent(value, aux.getLeft());
        }
        return null;
    }
    public Node searchParent(int value) { // Só valor de parametro, verifica se valor == raiz
        if(value == root.getDatum())
            return null;
        return searchParent(value, root);
    }
    


    /* GET BIGGEST/SMALLEST NODE */
    public Node getBiggestNode(Node root) { // Retorno o maior node da branch
        if(root.getRight() != null)
            return getBiggestNode(root.getRight());
        return root;
    }

    public Node getSmallestNode(Node node) { // Retorna o menor node da branch
        if(node.getLeft() != null)
            return getSmallestNode(node.getLeft());
        return node;
    }



    /* REMOVE */
    private Node remove(Node node)
    {
        if(node.getLeft() == null && node.getRight() == null)
            return null;
        else if(node.getLeft() == null)
            return node.getRight();
        else if(node.getRight() == null)
            return node.getLeft();
        else
        {
            int estValue = remove(getBiggestNode(node.getLeft()).getDatum(), false).getDatum();
            node.setDatum(estValue);
            return node;
        }
    }
    private Node remove(int value, Node node)
    {
        if(node != null) {
            if (node.getLeft() != null)
                if (node.getLeft().getDatum() == value)
                    return node.setLeft(remove(node.getLeft()));
            if (node.getRight() != null)
                if (node.getRight().getDatum() == value)
                    return node.setRight(remove(node.getRight()));

            if (value < node.getDatum())
                return remove(value, node.getLeft());
            if (value > node.getDatum())
                return remove(value, node.getRight());
        }
        return node;
    }
    public Node remove(int value, boolean shouldBalance)
    {
        if(isEmpty()) return null;

        if(value == root.getDatum())
            return root = remove(root);
        
        Node removed = remove(value, root);
        if(shouldBalance)
            searchUnbalance();
        return removed;
    }



    /* BALANCE */
    public int calcHeight(Node node)
    {
        if(node == null)
            return -1;
        int left = calcHeight(node.getLeft());
        int right = calcHeight(node.getRight());
        if(left > right)
            return 1 + left;
        return 1 + right;
    }

    public int calcBalance(Node node) {
        return calcHeight(node.getLeft()) - calcHeight(node.getRight());
    }

    private Node spinRight(Node root) {
        Node newRoot = root.getLeft();
        Node temp = newRoot.getRight();
        newRoot.setRight(root);
        root.setLeft(temp);
        return newRoot;
    }

    private Node spinLeft(Node root) {
        Node newRoot = root.getRight();
        Node temp = newRoot.getLeft();
        newRoot.setLeft(root);
        root.setRight(temp);
        return newRoot;
    }

    /* SEARCH UNBALANCE */
    private boolean searchUnbalance(Node node)
    {
        if(node != null) {
            searchUnbalance(node.getLeft());
            searchUnbalance(node.getRight());

            int nBalance = calcBalance(node);
            if (nBalance < -1 || nBalance > 1) {
                if (node.equals(root)) {
                    root = balanceNode(node);
                    return true;
                }
                Node nodeParent = searchParent(node.getDatum());
                if (node.getDatum() < nodeParent.getDatum())
                    nodeParent.setLeft(balanceNode(node));
                else
                    nodeParent.setRight(balanceNode(node));
                return true;
            }
        }
        return false;
    }
    public boolean searchUnbalance() {
        if(!isEmpty())
            return searchUnbalance(root);
        return false;
    }

    /* BALANCE NODE */
    public Node balanceNode(Node node) {
        Node nodeChild;
        int bNum = calcBalance(node);

        int bNumChild = calcHeight(node.getLeft()) > calcHeight(node.getRight())
                ? calcBalance(nodeChild = node.getLeft())
                : calcBalance(nodeChild = node.getRight());

        if(bNum == 2) {
            if(bNumChild == -1)
                node.setLeft(spinLeft(nodeChild));
            return spinRight(node);
        }
        if(bNum == -2) {
            if(bNumChild == 1)
                node.setRight(spinRight(nodeChild));
            return spinLeft(node);
        }

        System.out.println("Error: Something went wrong. (" + bNum +":"+bNumChild + ")");
        return node;
    }



    /* PRINT IN-ORDER */
    private void printInOrder(Node node)
    {
        if(node != null)
        {
            printInOrder(node.getLeft());
            System.out.print(node.getDatum() + "|");
            printInOrder(node.getRight());
        }
    }
    public void printInOrder() {
        System.out.print("InOrder:   |");
        printInOrder(root);
        System.out.print("\n");
    }


    /* PRINT PRE-ORDER */
    private void printPreOrder(Node node)
    {
        if(node != null)
        {
            System.out.print(node.getDatum() + "|");
            printPreOrder(node.getLeft());
            printPreOrder(node.getRight());
        }
    }
    public void printPreOrder() {
        System.out.print("PreOrder:  |");
        printPreOrder(root);
        System.out.print("\n");
    }


    /* PRINT POST-ORDER */
    private void printPostOrder(Node node)
    {
        if(node != null)
        {
            printPostOrder(node.getLeft());
            printPostOrder(node.getRight());
            System.out.print(node.getDatum() + "|");
        }
    }
    public void printPostOrder() {
        System.out.print("PostOrder: |");
        printPostOrder(root);
        System.out.print("\n");
    }
}
