import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int line =sc.nextInt();
        sc.nextLine();
        for (int i = 0; i < line; i++) {
            String input = sc.nextLine();
            System.out.printf("%d. %s\n",(i+1),input);
        }
    }
}