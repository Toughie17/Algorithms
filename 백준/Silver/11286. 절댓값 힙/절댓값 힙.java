import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws NumberFormatException,IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> queue = new PriorityQueue<>((num1,num2) -> {
            int firstAbs = Math.abs(num1);
            int secondAbs = Math.abs(num2);

            if (firstAbs == secondAbs) {
                return num1 > num2 ? 1 : -1;
            }

            return firstAbs - secondAbs;
        });

        for (int i =0; i < N; i++) {
            int input = Integer.parseInt(br.readLine());
            if (input == 0) {
                if (queue.isEmpty()) {
                    System.out.println("0");
                } else {
                    System.out.println(queue.poll());
                }
            } else {
                queue.add(input);
            }
        }
        br.close();
    }
}