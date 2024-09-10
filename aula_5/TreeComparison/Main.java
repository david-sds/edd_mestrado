import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Random;
import java.util.Set;
import java.util.stream.LongStream;

import avl_tree.AvlTree;

public class Main {

    static Random random = new Random();

    public static void main(String[] args) {
        Random random = new Random();

        int numberOfItems = 1000000;
        Set<Integer> set = new HashSet<Integer>();

        // Generate random numbers until we have 'n' unique numbers
        while (set.size() < numberOfItems) {
            int randomNumber = random.nextInt(numberOfItems * 1000);
            set.add(randomNumber);
        }
        
        List<Integer> list = new ArrayList<>(set);

        AvlTree
         avlTree = new AvlTree();
        RedBlackTree<Integer> redBlackTree = new RedBlackTree<Integer>();

        for (Integer num : list) {
            avlTree.insertData(num);
            redBlackTree.insert(num);
        }

        int numberOfSearchs = 10000;
        int[] searchValues = new int[numberOfSearchs];
        long[] elepsedTimesRBT = new long[numberOfSearchs];
        long[] elepsedTimesBT = new long[numberOfSearchs];
        
        for (int i = 0; i < searchValues.length; i++) {
            int randomIndex = random.nextInt(list.size());
            searchValues[i] = list.get(randomIndex);
        }

        for (int i = 0; i < searchValues.length; i++) {
            int value = searchValues[i];
            long start, end, elapsed;
            
            start = System.nanoTime();
            avlTree.searchData(value);
            end = System.nanoTime();
            elapsed = end - start;
            elepsedTimesBT[i] = elapsed;
            
            start = System.nanoTime();
            redBlackTree.search(value);
            end = System.nanoTime();
            elapsed = end - start;
            elepsedTimesRBT[i] = elapsed;

            System.out.println(
                "Search " + (i + 1) + ": " + value + "; " +
                "(BT, RBT) => (" + elepsedTimesBT[i] + "ns, " + elepsedTimesRBT[i] + "ns)."
            );
        }
        
        System.out.println();
        System.out.println("Average search times:");
        System.out.println("> Red Black Tree: " + LongStream.of(elepsedTimesRBT).average().getAsDouble() + "ns.");
        System.out.println("> Binary Tree: " + LongStream.of(elepsedTimesBT).average().getAsDouble() + "ns.");
    }

}
