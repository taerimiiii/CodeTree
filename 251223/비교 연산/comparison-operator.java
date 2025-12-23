import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 변수 선언
        int a, b;
        
        // 입력
        a = sc.nextInt();
        b = sc.nextInt();

        System.out.println(a >= b ? 1 : 0);
        System.out.println(a > b ? 1 : 0);
        System.out.println(a <= b ? 1 : 0);
        System.out.println(a < b ? 1 : 0);
        System.out.println(a == b ? 1 : 0);
        System.out.println(a != b ? 1 : 0);
    }
}
