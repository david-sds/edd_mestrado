
package avl_tree;

public class AvlTreeNode {

    /**
     * Se definen los atributos del objeto,
     * data: valor que almacena el objeto
     * balanceFactor: Factor de balanceo del nodo leftChild: Hijo izquierdo del nodo
     * rightChild: Hijo derecho del nodo
     */
    private int data;
    private int balanceFactor;
    private AvlTreeNode leftChild;
    private AvlTreeNode rightChild;

    /**
     * Constructor del objeto. 
     * inicializa los datos cada que se crea un objeto de la clase
     * @param data, valor que el nodo va a almacenar
     */
    public AvlTreeNode(int data) {
        this.data = data;
        this.balanceFactor = 1;
        this.leftChild = null;
        this.rightChild = null;
    }

    /**
     * getData()
     * Retorna el dato de un nodo
     * @return dato del nodo
     */
    public int getData() {
        return data;
    }
    
    /**
     * setData(data)
     * Asigna un dato al nodo
     * @param data, dato a insertar en el nodo
     */
    public void setData(int data) {
        this.data = data;
    }
    
    /**
     * getBalanceFactor()
     * Retorna el factor de balance de un nodo
     * @return factor de balance del nodo
     */
    public int getBalanceFactor() {
        return balanceFactor;
    }
    
    /**
     * setBalanceFactor(balanceFactor)
     * Asigna el factor de balance a un nodo
     * @param balanceFactor, valor del factor de balance del nodo
     */
    public void setBalanceFactor(int balanceFactor) {
        this.balanceFactor = balanceFactor;
    }
    
    /**
     * getLeftChild()
     * Retorna el hijo izquierdo de un nodo, null si el nodo no tiene hijo izquiero
     * @return nodo correspondiente al hijo izquierdo
     */
    public AvlTreeNode getLeftChild() {
        return leftChild;
    }
    
    /**
     * setLeftChild(leftChild)
     * Asigna un hijo izquierdo al nodo
     * @param leftChild, nodo que será el hijo izquierdo
     */
    public void setLeftChild(AvlTreeNode leftChild) {
        this.leftChild = leftChild;
    }

     /**
     * getRigthChild()
     * Retorna el hijo derecho de un nodo, null si el nodo no tiene hijo derecho
     * @return nodo correspondiente al hijo derecho
     */
    public AvlTreeNode getRigthChild() {
        return rightChild;
    }
    
    /**
     * setRigthChild(rigthChild)
     * Asigna un hijo derecho al nodo
     * @param rigthChild, nodo que será el hijo derecho
     */
    public void setRigthChild(AvlTreeNode rigthChild) {
        this.rightChild = rigthChild;
    }
}
