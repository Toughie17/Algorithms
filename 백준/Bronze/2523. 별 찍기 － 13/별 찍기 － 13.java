import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();
        
        for(int i = 1; i <= 2 * n - 1; i++) {
            int star = i <= n ? i : 2 * n - i;
            for(int j = 0; j < star; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}