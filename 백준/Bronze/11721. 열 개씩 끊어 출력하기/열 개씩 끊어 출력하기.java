import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        int lines = input.length() / 10;

        if (input.length() <= 10) {
            System.out.println(input);
        } else {
            int start = 0;
            int end = 10;
            int leftLengh = input.length();

            for (int i = 0; i < lines + 1; i++) {
                String pre = input.substring(start,end);
                System.out.println(pre);

                leftLengh -= 10;
                start += 10;

                if (leftLengh > 10) {
                    end += 10;
                } else {
                    end = start + leftLengh;
                }
            }
        }
    }
}