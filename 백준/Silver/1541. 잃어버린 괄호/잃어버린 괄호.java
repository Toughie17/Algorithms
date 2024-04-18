import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] target = input.split("-");
        sc.close();
        int total = 0;
        for(int i =0; i < target.length; i++) {
            if(i == 0) {
                total += sumS(target[i]);
            } else {
                total -= sumS(target[i]);
            }
        }
        System.out.println(total);
    }

    private static int sumS(String input) {
        String[] target = input.split("\\+");
        int total = 0;
        for(String n : target) {
            total += Integer.parseInt(n);
        }
        return total;
    }
}