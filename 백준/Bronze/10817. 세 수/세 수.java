import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
//        int[] numbers = new int[3];
//        for(int i =0; i < 3; i++) {
//            numbers[i] = sc.nextInt();
//        }
//        // 버블 정렬 쓰기: 내림차순 정렬하고 중간 값 뽑아내자.
//        for(int i = 0; i < numbers.length -1; i++) {
//            for (int j =0; j<numbers.length -1 - i; j++) {
//                 if(numbers[j] < numbers[j+1]) {
//                     int tmp = numbers[j];
//                     numbers[j] = numbers[j+1];
//                     numbers[j+1] = tmp;
//                 }
//            }
//        }
//        System.out.println(numbers[1]);

        //조건문 몸빵
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        sc.close();
        //a가 두번째로 큰 경우 b a c , c a b
        if (a >= b && a <= c || a >= c && a <= b) {
            System.out.println(a);

            //b가 두번째로 큰 경우 a b c, c b a
        } else if (b >= a && b <= c || b >= c && b <= a) {
            System.out.println(b);
        } else {
            System.out.println(c);
        }
    }
}