import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int today = sc.nextInt() % 10;
        int count = 0;

        for (int i =0; i < 5; i++) {
            int car = sc.nextInt();
            if (today == car) {
                count++;
            }
        }
        sc.close();
        System.out.println(count);
    }
}