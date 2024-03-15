import java.util.Scanner;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringTokenizer st = new StringTokenizer(sc.nextLine(),"/");
        int k = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int a = Integer.parseInt(st.nextToken());
        sc.close();
        if ((k+a < d) || d == 0) {
            System.out.println("hasu");
        } else {
            System.out.println("gosu");
        }
    }
}