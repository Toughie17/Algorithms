import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;

import java.io.IOException;

public class Main {
    static boolean[] visited;
    static ArrayList<Integer>[] near;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int node = Integer.parseInt(st.nextToken());
        int edge = Integer.parseInt(st.nextToken());

        visited = new boolean[node + 1];
        near = new ArrayList[node + 1];
        for (int i = 1; i < node + 1; i++) {
            near[i] = new ArrayList<Integer>();
        }

        for (int i = 0; i < edge; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            near[start].add(end);
            near[end].add(start);
        }

        int count = 0;

        for (int i = 1; i < node + 1; i++) {
            if (!visited[i]) {
                count++;
                DFS(i);
            }
        }
        System.out.println(count);
    }

    private static void DFS(int v) {
        if (visited[v]) {
            return;
        }
        visited[v] = true;
        for (int i : near[v]) {
            if (!visited[i]) {
                DFS(i);
            }
        }
    }
}
