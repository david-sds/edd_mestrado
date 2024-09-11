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
        long[] numbers = {4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216};
        for (int j = 0; j < numbers.length; j++) {
            Random random = new Random(j);
            long numberOfItems = numbers[j];

            Set<Long> set = new HashSet<Long>();

            // Generate random numbers until we have 'n' unique numbers
            while (set.size() < numberOfItems) {
                long randomNumber = random.nextLong(numberOfItems * 1000);
                set.add(randomNumber);
            }
            
            List<Long> list = new ArrayList<>(set);

            AvlTree avlTree = new AvlTree();
            RedBlackTree<Long> redBlackTree = new RedBlackTree<Long>();

            for (Long num : list) {
                avlTree.insertData(num);
                redBlackTree.insert(num);
            }

            int numberOfSearchs = 10000;
            long[] searchValues = new long[numberOfSearchs];
            long[] elepsedTimesRBT = new long[numberOfSearchs];
            long[] elepsedTimesBT = new long[numberOfSearchs];
            
            for (int i = 0; i < searchValues.length; i++) {
                int randomIndex = random.nextInt(list.size());
                searchValues[i] = list.get(randomIndex);
            }

            for (int i = 0; i < searchValues.length; i++) {
                long value = searchValues[i];
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

                // System.out.println(
                //     "Search " + (i + 1) + ": " + value + "; " +
                //     "(BT, RBT) => (" + elepsedTimesBT[i] + "ns, " + elepsedTimesRBT[i] + "ns)."
                // );
            }
            
            System.out.println("\nNumber of items: " + numberOfItems);
            System.out.println("Average search times:");
            System.out.println("> Red Black Tree: " + LongStream.of(elepsedTimesRBT).average().getAsDouble() + "ns.");
            System.out.println("> Binary Tree: " + LongStream.of(elepsedTimesBT).average().getAsDouble() + "ns.");
        }
    }

}
