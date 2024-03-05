import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String text = sc.nextLine();
        int index = sc.nextInt() - 1;
        System.out.println(text.charAt(index));
        sc.close();
    }
}