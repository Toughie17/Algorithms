import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int count = sc.nextInt();
        for (int i =0; i < count; i++) {
            String input = sc.next();
            int len = input.length();
            System.out.printf("%c%c\n",input.charAt(0),input.charAt(len - 1));
        }
    }
}