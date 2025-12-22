import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 변수 선언
        int n;
        
        // 입력
        n = sc.nextInt();
        
        // 출력
        if(n >= 3000)
            System.out.println("book");
        else if(n >= 1000)
            System.out.println("mask");
        else
            System.out.println("no");
    }
}
