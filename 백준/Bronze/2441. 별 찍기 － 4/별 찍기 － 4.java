import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int count = sc.nextInt();
        for(int i = 0; i < count; i++) {
            //공백
            for(int k = 0; k < i; k++) {
                System.out.print(" ");
            }
            //별
            for(int j = count - i; j > 0; j-- ) {
                System.out.print("*");
            }
            System.out.println();
        }

    }
}