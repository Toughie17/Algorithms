import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int count = sc.nextInt();
        int min = sc.nextInt();
        int max = min;
        for (int i =1; i < count; i++) {
            int next = sc.nextInt();
            if (next < min) {
                min = next;
            }
            if (next > max) {
                max = next;
            }
        }
        sc.close();
        System.out.printf("%d %d", min,max);
    }
}