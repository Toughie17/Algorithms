import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int vacation = sc.nextInt();

        int koreanTotal = sc.nextInt();
        int mathTotal = sc.nextInt();

        int dailyKorean = sc.nextInt();
        int dailyMath = sc.nextInt();

        int koreanDay;
        if (koreanTotal % dailyKorean == 0) {
            koreanDay = koreanTotal/dailyKorean;
        } else {
            koreanDay = koreanTotal/dailyKorean + 1;
        }

        int mathDay;
        if (mathTotal % dailyMath == 0) {
            mathDay = mathTotal/dailyMath;
        } else {
            mathDay = mathTotal/dailyMath + 1;
        }

        System.out.println(vacation - Math.max(koreanDay,mathDay));
    }
}