import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int sum = a + b + c;

        if (sum != 180) {
            System.out.println("Error");
            return;
        }
        if (a == b && b == c) {
            System.out.println("Equilateral");
        } else if (a == b || b == c || c == a) {
            System.out.println("Isosceles");
        } else {
            System.out.println("Scalene");
        }
    }
}