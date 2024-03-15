import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int sum = sc.nextInt();
        int minus = sc.nextInt();

        if (sum >= minus && (sum + minus) % 2 == 0) {
            int a = (sum + minus) / 2;
            int b = sum - a;
            System.out.printf("%d %d", a,b);
        } else {
            System.out.println(-1);
        }
    }
}