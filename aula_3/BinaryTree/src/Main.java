public class Main {

    static TreePrinter<Node> printer = new TreePrinter<>(n -> ("" + n.getDatum()), n -> n.getLeft(), n -> n.getRight());

    public static void main(String[] args) {

        BinaryTree bt1 = new BinaryTree();
        BinaryTree bt2 = new BinaryTree();

        // Árvore Infernal sendo balanceada
        bt1.insert(100, true);
        bt1.insert(56, true);
        bt1.insert(32, true);
        bt1.insert(80, true);
        bt1.insert(127, true);
        bt1.insert(115, true);
        bt1.remove(32, true);
        bt1.insert(85, true);
        bt1.insert(130, true);
        bt1.insert(82, true);
        bt1.insert(90, true);
        bt1.insert(120, true);
        bt1.remove(80, true);
        bt1.insert(95, true);
        bt1.remove(127, true);
        bt1.insert(40, true);
        bt1.insert(68, true);
        bt1.remove(56, true);
        bt1.remove(40, true);
        bt1.remove(82, true);
        bt1.insert(50, true);
        bt1.insert(17, true);
        bt1.insert(27, true);
        bt1.insert(89, true);
        bt1.insert(14, true);
        bt1.insert(33, true);
        bt1.insert(31, true);
        bt1.insert(52, true);
        bt1.insert(10, true);
        bt1.insert(18, true);
        bt1.insert(15, true);
        bt1.insert(5, true);
        bt1.insert(7, true);
        bt1.insert(6, true);
        bt1.insert(11, true);
        bt1.insert(12, true);
        bt1.insert(8, true);

        // Árvore Infernal sem balancear
        bt2.insert(100, false);
        bt2.insert(56, false);
        bt2.insert(32, false);
        bt2.insert(80, false);
        bt2.insert(127, false);
        bt2.insert(115, false);
        bt2.remove(32, false);
        bt2.insert(85, false);
        bt2.insert(130, false);
        bt2.insert(82, false);
        bt2.insert(90, false);
        bt2.insert(120, false);
        bt2.remove(80, false);
        bt2.insert(95, false);
        bt2.remove(127, false);
        bt2.insert(40, false);
        bt2.insert(68, false);
        bt2.remove(56, false);
        bt2.remove(40, false);
        bt2.remove(82, false);
        bt2.insert(50, false);
        bt2.insert(17, false);
        bt2.insert(27, false);
        bt2.insert(89, false);
        bt2.insert(14, false);
        bt2.insert(33, false);
        bt2.insert(31, false);
        bt2.insert(52, false);
        bt2.insert(10, false);
        bt2.insert(18, false);
        bt2.insert(15, false);
        bt2.insert(5, false);
        bt2.insert(7, false);
        bt2.insert(6, false);
        bt2.insert(11, false);
        bt2.insert(12, false);
        bt2.insert(8, false);


        printer.setHspace(3);
        printer.setSquareBranches(true);
        
        System.out.println("\nTreePrinter - bt1:\n");
        printer.printTree(bt1.getRoot());

        System.out.println("\nTreePrinter - bt2:\n");
        printer.printTree(bt2.getRoot());

        System.out.println("\nA ÁRVORE DO VILMAR ESTÁ NO INÍCIO\n");

    }

}
