import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int test = sc.nextInt();

        for (int i =0; i < test; i++) {
            int h = sc.nextInt();
            int w = sc.nextInt();
            int c = sc.nextInt(); //얘가 몇호에 가는가

            int floor = c % h;
            int room = (c / h) + 1;

            if (floor == 0) {
                floor = h;
                room--;
            }

            System.out.println(floor * 100 + room);
        }
    }
}