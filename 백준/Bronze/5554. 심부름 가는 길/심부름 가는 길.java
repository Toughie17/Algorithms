import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int total = (sc.nextInt() + sc.nextInt() + sc.nextInt() + sc.nextInt());
        sc.close();
        int minute = total / 60;
        int second = total % 60;
        System.out.println(minute);
        System.out.println(second);
    }
}