import java.util.*;

public class MissionariesCannibals {
    static class State {
        int m, c, boat;

        State(int m, int c, int boat) {
            this.m = m;
            this.c = c;
            this.boat = boat;
        }
    }

    static boolean safe(int m, int c) {
        int mr = 3 - m;
        int cr = 3 - c;

        return m >= 0 && m <= 3 &&
               c >= 0 && c <= 3 &&
               (m == 0 || m >= c) &&
               (mr == 0 || mr >= cr);
    }

    static String key(State s) {
        return s.m + "," + s.c + "," + s.boat;
    }

    public static void main(String[] args) {
        Queue<State> q = new LinkedList<>();
        Map<String, String> parent = new HashMap<>();
        Map<String, State> states = new HashMap<>();

        State start = new State(3, 3, 0);
        String startKey = key(start);

        q.add(start);
        parent.put(startKey, null);
        states.put(startKey, start);

        int[][] moves = {
            {1, 0}, {2, 0}, {0, 1},
            {0, 2}, {1, 1}
        };

        String goalKey = null;

        while (!q.isEmpty()) {
            State cur = q.poll();
            String ck = key(cur);

            if (cur.m == 0 && cur.c == 0 && cur.boat == 1) {
                goalKey = ck;
                break;
            }

            for (int[] move : moves) {
                int nm, nc;

                if (cur.boat == 0) {
                    nm = cur.m - move[0];
                    nc = cur.c - move[1];
                } else {
                    nm = cur.m + move[0];
                    nc = cur.c + move[1];
                }

                if (!safe(nm, nc))
                    continue;

                int nb = 1 - cur.boat;
                State ns = new State(nm, nc, nb);
                String nk = key(ns);

                if (!parent.containsKey(nk)) {
                    parent.put(nk, ck);
                    states.put(nk, ns);
                    q.add(ns);
                }
            }
        }

        if (goalKey == null) {
            System.out.println("No solution found.");
            return;
        }

        List<State> path = new ArrayList<>();

        for (String k = goalKey; k != null; k = parent.get(k))
            path.add(states.get(k));

        Collections.reverse(path);

        for (int i = 0; i < path.size(); i++) {
            State s = path.get(i);
            String side = s.boat == 0 ? "Left" : "Right";

            System.out.println("Step " + i +
                ": Left bank M=" + s.m +
                ", C=" + s.c +
                " | Right bank M=" + (3 - s.m) +
                ", C=" + (3 - s.c) +
                " | Boat: " + side);
        }

        System.out.println("Total crossings: " + (path.size() - 1));
    }
}
