import java.util.*;

public class WaterJug {
    static class State {
        int a, b;

        State(int a, int b) {
            this.a = a;
            this.b = b;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter capacity of Jug A: ");
        int capA = sc.nextInt();

        System.out.print("Enter capacity of Jug B: ");
        int capB = sc.nextInt();

        System.out.print("Enter target amount: ");
        int target = sc.nextInt();

        if (capA <= 0 || capB <= 0 ||
            target < 0 || target > Math.max(capA, capB)) {
            System.out.println("Invalid input.");
            sc.close();
            return;
        }

        Queue<State> queue = new LinkedList<>();
        Map<String, String> parent = new HashMap<>();
        Map<String, State> states = new HashMap<>();

        State start = new State(0, 0);
        String startKey = "0,0";

        queue.add(start);
        parent.put(startKey, null);
        states.put(startKey, start);

        String goalKey = null;

        while (!queue.isEmpty()) {
            State cur = queue.poll();
            int a = cur.a, b = cur.b;
            String key = a + "," + b;

            if (a == target || b == target) {
                goalKey = key;
                break;
            }

            int[][] next = {
                {capA, b},       // Fill A
                {a, capB},       // Fill B
                {0, b},          // Empty A
                {a, 0},          // Empty B
                {a - Math.min(a, capB - b),
                 b + Math.min(a, capB - b)}, // A to B
                {a + Math.min(b, capA - a),
                 b - Math.min(b, capA - a)}  // B to A
            };

            for (int[] n : next) {
                String nk = n[0] + "," + n[1];

                if (!parent.containsKey(nk)) {
                    State ns = new State(n[0], n[1]);
                    queue.add(ns);
                    parent.put(nk, key);
                    states.put(nk, ns);
                }
            }
        }

        if (goalKey == null) {
            System.out.println("Target cannot be measured.");
        } else {
            List<State> path = new ArrayList<>();

            for (String k = goalKey; k != null; k = parent.get(k)) {
                path.add(states.get(k));
            }

            Collections.reverse(path);

            System.out.println("\nSolution:");
            for (int i = 0; i < path.size(); i++) {
                State s = path.get(i);
                System.out.println("Step " + i +
                    ": Jug A = " + s.a +
                    ", Jug B = " + s.b);
            }

            System.out.println("Total operations: " +
                (path.size() - 1));
        }

        sc.close();
    }
}
