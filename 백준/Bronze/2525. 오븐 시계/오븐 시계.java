import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();
        int m = sc.nextInt();
        int t = sc.nextInt();
        sc.close();

        if (m + t >= 60) {
            h = h + (m+t) / 60;
            m = (m + t) % 60;
            if (h >=24) {
                h -= 24;
            }
        } else {
            m = m+t;
        }
        System.out.printf("%d %d", h,m);
    }
}