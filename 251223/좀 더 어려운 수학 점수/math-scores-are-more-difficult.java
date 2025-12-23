import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 변수 선언
        int a_math, a_eng;
        int b_math, b_eng;
        
        // 입력
        a_math = sc.nextInt();
        a_eng = sc.nextInt();
        b_math = sc.nextInt();
        b_eng = sc.nextInt();

        // 출력
        if(a_math > b_math || (a_math == b_math && a_eng > b_eng))
            System.out.println("A");
        else
            System.out.println("B");
    }
}
