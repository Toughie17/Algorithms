import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int d = sc.nextInt();
        int worst = Math.min(Math.min(a,b),Math.min(c,d));

        int e = sc.nextInt();
        int f = sc.nextInt();

        sc.close();
        System.out.println((a+b+c+d -worst + Math.max(e,f)));
    }
}