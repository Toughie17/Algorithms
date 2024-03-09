import java.util.Scanner;
import java.lang.Math;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int prize;

        if (a == b && b == c) {
            prize = 10000 + (a * 1000);
            System.out.println(prize);
        } else if (a == b || b == c || c == a) {
            int sameNum = (a == b) ? a : c;
            prize = 1000 + sameNum * 100;
            System.out.println(prize);
        } else {
            int max = Math.max(a, Math.max(b,c));
            prize = max * 100;
            System.out.println(prize);
        }
        sc.close();
    }
}