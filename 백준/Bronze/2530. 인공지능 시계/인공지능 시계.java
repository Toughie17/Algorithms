import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int hour = sc.nextInt();
        int minute = sc.nextInt();
        int second = sc.nextInt();

        int total = sc.nextInt();

        total += (second + minute * 60 + hour * 3600);

        hour = (total / 3600) % 24;
        minute = (total % 3600) / 60;
        second = total % 60;

        System.out.printf("%d %d %d", hour, minute, second);
    }
}