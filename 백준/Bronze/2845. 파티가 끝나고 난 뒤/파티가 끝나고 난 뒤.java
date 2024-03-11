import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int correct = (sc.nextInt() * sc.nextInt());
        for(int i =0; i < 5; i++) {
            int x = sc.nextInt();
            System.out.printf("%d ",(x - correct));
        }
    }
}