import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String input = sc.nextLine();
        String result = "";

        for (int i = 0; i < input.length(); i++) {
            if (input.charAt(i) >= 97) {
                result += String.valueOf(input.charAt(i)).toUpperCase();
            } else {
                result += String.valueOf(input.charAt(i)).toLowerCase();
            }
        }
        System.out.println(result);
        sc.close();
    }
}