
public class BinaryTree {

    private Node root;

    public Node getRoot() {
        return root;
    }

    public BinaryTree() {
        root = null;
    }

    public boolean isEmpty() {
        return root == null;
    }



    /* INSERT */
    private void insert(Node node, Node aux)
    {
        // Se o valor é menor que o node verificado.
        if(node.getDatum() < aux.getDatum()) {
            // Caso a esquerda do node verificado esteja vazia:
            // - O node é inserido na esquerda.
            // Caso a esquerda do node verificado não esteja vazia:
            // - O método recursivo de inserção é chamado novamente.
            if(aux.getLeft() == null)
                aux.setLeft(node);
            else
                insert(node, aux.getLeft());
        }
        // Se o valor é maior que o node verificado.
        if(node.getDatum() > aux.getDatum()) {
            // Caso a direita do node verificado esteja vazia:
            // - O node é inserido na direita.
            // Caso a direita do node verificado não esteja vazia:
            // - O método recursivo de inserção é chamado novamente.
            if(aux.getRight() == null)
                aux.setRight(node);
            else
                insert(node, aux.getRight());
        }
    }
    public void insert(int value, boolean shouldBalance)
    {
        Node node = new Node(value);
        if (!isEmpty()) { 
            // Procura o valor na árvore.
            if(search(value) == null) {
                // Caso o valor não seja achado, é inserido.
                insert(node, root);
                if(shouldBalance) // A árvore é balanceada caso desejado.
                    searchUnbalance();
            } else {
                // Se o valor é achado não será inserido novamente.
                System.out.println("There is already a node with value " + value + ".");
            }
        } else {
            // Determina como raiz da árvore.
            root = node;
        }
    }



    /* SEARCH */
    private Node search(int value, Node node)
    {
        // Caso o node atual seja diferente de null e não seja o valor procurado.
        if(node != null && value != node.getDatum())
            // Caso o valor procurado seja maior ou igual ao node atual.
            if(value >= node.getDatum())
                // Repetimos a verificação no galho direito.
                return search(value, node.getRight());
            else
                // Repetimos a verificação no galho esquerdo.
                return search(value, node.getLeft());
        // Se o node atual for diferente de null o valor foi encontrado.
        // Se o node atual for igual a null o valor não está presente na árvore.
        return node;
    }
    public Node search(int value) {
        // Procura um valor desde a raiz.
        return search(value, root);
    }

    /* SEARCH PARENT */
    private Node searchParent(int value, Node aux)
    {
        // Caso o node atual seja diferente de null.
        if(aux != null) {
            // Verifica se o filho esquerdo é o valor, caso sim retorna o pai.
            if (aux.getLeft() != null)
                if (aux.getLeft().getDatum() == value)
                    return aux;

            // Verifica se o filho direito é o valor, caso sim retorna o pai.
            if (aux.getRight() != null)
                if (aux.getRight().getDatum() == value)
                    return aux;

            // Caso o node atual não seja pai do valor inserido
            // e o valor inserido é maior que o node atual.
            if (value >= aux.getDatum())
                // Repetimos o processo no galho direito.
                return searchParent(value, aux.getRight());
            else
                // Repetimos o processo no galho esquerdo.
                return searchParent(value, aux.getLeft());
        }
        return null;
    }
    public Node searchParent(int value) {
        // Caso a raiz exista procuramos o pai do valor inserido.
        if(value == root.getDatum())
            return null;
        return searchParent(value, root);
    }
    


    /* GET BIGGEST/SMALLEST NODE */
    public Node getBiggestNode(Node root) {
        // O maior node é o que está na extremidade direita.
        if(root.getRight() != null)
            return getBiggestNode(root.getRight());
        return root;
    }

    public Node getSmallestNode(Node node) {
        // O menor node é o que está na extremidade esquerda.
        if(node.getLeft() != null)
            return getSmallestNode(node.getLeft());
        return node;
    }



    /* REMOVE */
    private Node remove(Node node)
    {   
        // Se o node sendo removido:
        // - Não possui filhos: retornamos null.
        if(node.getLeft() == null && node.getRight() == null)
            return null;
        // - Possúi apenas o galho direto: Retornamos o galho direito.
        else if(node.getLeft() == null)
            return node.getRight();
        // - Possúi apenas o galho esquerdo: Retornamos o galho esquerdo.
        else if(node.getRight() == null)
            return node.getLeft();
        else
        {
            // Caso os dois filhos sejam diferentes de null,
            // Retornamos o maior node da sub-árvore esquerda
            // Essa ação é feita para se manter a estrutura da árvore intacta
            // O menor nó da sub-árvore direita também poderia ter sido utilizado. 
            int estValue = remove(getBiggestNode(node.getLeft()).getDatum(), false).getDatum();
            node.setDatum(estValue);
            return node;
        }
    }
    private Node remove(int value, Node node)
    {
        if(node != null) {
            // Caso o filho esquerdo seja o valor procurado ele é substituido.
            if (node.getLeft() != null)
                if (node.getLeft().getDatum() == value)
                    return node.setLeft(remove(node.getLeft()));
            // Caso o filho direito seja o valor procurado ele é substituido.
            if (node.getRight() != null)
                if (node.getRight().getDatum() == value)
                    return node.setRight(remove(node.getRight()));

            // Caso o valor procurado seja menor que o valor atual.
            if (value < node.getDatum())
                // A busca continua na sub-árvore esquerda.
                return remove(value, node.getLeft());
            if (value > node.getDatum())
                // A busca continua na sub-árvore direita.
                return remove(value, node.getRight());
        }
        return node;
    }
    public Node remove(int value, boolean shouldBalance)
    {
        // Caso a árvore esteja vazia não fazemos nada.
        if(isEmpty()) return null;

        // Caso o valor seja a raiz removemos ela.
        if(value == root.getDatum())
            return root = remove(root);
        
        // Fazemos a chamada para a busca e remoção recursiva.
        Node removed = remove(value, root);

        // Balanceamos caso seja desejado.
        if(shouldBalance)
            searchUnbalance();
        
        // O valor removido é retornado.
        return removed;
    }



    /* BALANCE */
    public int calcHeight(Node node)
    {
        // Se o node é null retornamos -1
        if(node == null)
            return -1;
        // Definimos o contador da esquerda como a altura da sub-árvore esquerda.
        int left = calcHeight(node.getLeft());
        // Definimos o contador da direita como a altura da sub-árvore direita.
        int right = calcHeight(node.getRight());
        // Caso o contador esquerdo seja maior.
        if(left > right)
            // Incrementamos o contador esquerdo e o retornamos.
            return 1 + left;
        // Incrementamos o contador direito e o retornamos.
        return 1 + right;
    }

    public int calcBalance(Node node) {
        // Calculamos o balanceamento como a diferença da
        // altura da sub-árvore esquerda com a altura da sub-árvore direita.
        return calcHeight(node.getLeft()) - calcHeight(node.getRight());
    }

    private Node spinRight(Node root) {
        // Definimos a nova raiz como a raiz da sub-árvore esquerda.
        Node newRoot = root.getLeft();
        // Salvamos a sub-árvore direita da nova raiz na memória.
        Node temp = newRoot.getRight();
        // Mudamos a direita da nova raiz como a raiz antiga.
        newRoot.setRight(root);
        // Mudamos a esquerda da raiz antiga como o valor salvo na memória.
        root.setLeft(temp);
        // Retornamos a nova raiz.
        return newRoot;
    }

    private Node spinLeft(Node root) {
        Node newRoot = root.getRight();
        // Definimos a nova raiz como a raiz da sub-árvore direita.
        Node temp = newRoot.getLeft();
        // Salvamos a sub-árvore esquerda da nova raiz na memória.
        newRoot.setLeft(root);
        // Mudamos a esquerda da nova raiz como a raiz antiga.
        root.setRight(temp);
        // Retornamos a nova raiz.
        return newRoot;
    }

    /* SEARCH UNBALANCE */
    private boolean searchUnbalance(Node node)
    {
        if(node != null) {
            // Procura recursivamente nodes a esquerda.
            searchUnbalance(node.getLeft());
            // Procura recursivamente nodes a direita.
            searchUnbalance(node.getRight());

            int nBalance = calcBalance(node);
            // Cada node tem o número de sua balança calculada.
            // Caso esteja desbalanceada:
            if (nBalance < -1 || nBalance > 1) {
                // Caso a raiz seja o node desbalanceado balanceamos a árvore
                // inteira e setamos uma nova raiz.
                if (node.equals(root)) {
                    root = balanceNode(node);
                    return true;
                }
                // Caso não seja a raiz sabemos e o node possúi um node pai.
                // Achamos esse node pai.
                Node nodeParent = searchParent(node.getDatum());
                if (node.getDatum() < nodeParent.getDatum())
                    // A sub-árvore esquerda é balanceada e um novo node
                    // é setado como sua raiz.
                    nodeParent.setLeft(balanceNode(node));
                else
                    // A sub-árvore direita é balanceada e um novo node
                    // é setado como sua raiz.
                    nodeParent.setRight(balanceNode(node));
                return true;
            }
        }
        return false;
    }
    public boolean searchUnbalance() {
        if(!isEmpty()) // Caso a árvore não esteja vazia ocorre o balanceamento.
            return searchUnbalance(root);
        return false;
    }

    /* BALANCE NODE */
    public Node balanceNode(Node node) {
        // Para realizarmos o balanceamento precisamos pegar o:
        // Node filho com a maior altura.
        Node nodeChild;
        // O número do balanceamento da raiz da árvore desbalanceada.
        int bNum = calcBalance(node);

        // O número do balanceamento do filho com a maior altura.
        int bNumChild = calcHeight(node.getLeft()) > calcHeight(node.getRight())
                ? calcBalance(nodeChild = node.getLeft())
                : calcBalance(nodeChild = node.getRight());

        // Se a árvore está com o valor 2 positivo, ela está desbalanceada
        // para a esquerda, então giramos a sub-árvore esquerda dela para
        // a esquerda e giramos a árvore para a direita.
        if(bNum == 2) {
            if(bNumChild == -1)
                node.setLeft(spinLeft(nodeChild));
            return spinRight(node);
        }
        // Se a árvore está com o valor 2 negativo, ela está desbalanceada
        // para a direita, então giramos a sub-árvore direita dela para
        // a direita e giramos a árvore para a esquerda.
        if(bNum == -2) {
            if(bNumChild == 1)
                node.setRight(spinRight(nodeChild));
            return spinLeft(node);
        }
        // O código parte do pressuposto que a árvore vai ser balanceada
        // a cada inserção ou não vai ser balanceada em nenhuma inserção.
        // Portanto se ela estiver sendo balanceada toda vez o número
        // do balanceamento não sera maior que 2 ou menos que -2.
        // Qualquer situação que esse seja diferente desses valores
        // indica algo de errado no algoritmo.
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
