import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int count = scanner.nextInt();
        String input = scanner.next();
        int sum = 0;
        for (int i =0; i < count; i++) {
            sum += Character.getNumericValue(input.charAt(i));
        }

        System.out.println(sum);
    }
}