import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine();
        String b = sc.nextLine();
        sc.close();
        
        int a1 = Integer.parseInt(a) * Character.getNumericValue(b.charAt(2));
        int a2 = Integer.parseInt(a) * Character.getNumericValue(b.charAt(1));
        int a3 = Integer.parseInt(a) * Character.getNumericValue(b.charAt(0));
        System.out.println(a1);
        System.out.println(a2);
        System.out.println(a3);
        System.out.println(a1 + 10 * a2 + a3 * 100);
    }
}