import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        sc.close();
        
        final int A = 300;
        final int B = 60;
        final int C = 10;

        int aCount=0;
        int bCount=0;
        int cCount=0;
        
        if (T >= A) {
            aCount = T / A;
            T = T % A;
        }

        if (T >= B) {
            bCount = T / B;
            T = T % B;
        }

        if (T >= C) {
            cCount = T / C;
            T = T % C;
        }

        if (T != 0) {
            System.out.println(-1);
        } else {
            System.out.printf("%d %d %d",aCount,bCount,cCount);
        }
    }
}