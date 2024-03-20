import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x1 = sc.nextInt();
        int y1 = sc.nextInt();

        int x2 = sc.nextInt();
        int y2 = sc.nextInt();

        int x3 = sc.nextInt();
        int y3 = sc.nextInt();

        sc.close();
        
        int rx;
        int ry;

        if (x1 == x2) {
            rx = x3;
        } else if (x2 == x3) {
            rx = x1;
        } else {
            rx = x2;
        }

        if (y1 == y2) {
            ry = y3;
        } else if (y2 == y3) {
            ry = y1;
        } else {
            ry = y2;
        }
        System.out.printf("%d %d",rx,ry);
    }
}