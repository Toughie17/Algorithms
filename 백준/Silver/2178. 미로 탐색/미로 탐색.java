import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
    static int[] dx = {0,0,-1,1};
    static int[] dy = {-1,1,0,0};
    static int[][] A;
    static boolean[][] visited;
    static int n,m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        A = new int[n][m];
        visited = new boolean[n][m];

        for(int i =0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String line = st.nextToken();
            for (int j =0; j < m; j++) {
                A[i][j] = Integer.parseInt(line.substring(j,j+1));
            }
        }

        BFS(0,0);
        System.out.println(A[n-1][m-1]);
    }

    private static void BFS(int i, int j) {
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[] {i,j});
        while(!queue.isEmpty()) {
            int[] now = queue.poll();
            visited[i][j] = true;

            for(int k =0; k < dx.length; k++) {
                int nearX = now[0] + dx[k];
                int nearY = now[1] + dy[k];

                if(nearX >=0 && nearY >=0 && nearX < n && nearY < m) {
                    if(A[nearX][nearY] != 0 && !visited[nearX][nearY]) {
                        visited[nearX][nearY] = true;
                        A[nearX][nearY] = A[now[0]][now[1]] + 1;
                        queue.add(new int[] {nearX, nearY});
                    }
                }
            }
        }
    }
}