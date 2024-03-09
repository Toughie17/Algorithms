import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int receiptTotal = sc.nextInt();
        int productCount = sc.nextInt();
        int correctTotal = 0;
        for (int i = 0; i < productCount; i++) {
            int prod = sc.nextInt();
            int price = sc.nextInt();
            correctTotal += (prod * price);
        }
        if (receiptTotal == correctTotal) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
        sc.close();
    }
}