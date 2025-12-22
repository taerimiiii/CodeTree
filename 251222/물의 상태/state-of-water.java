import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 변수 선언
        int temp;
        
        // 입력
        temp = sc.nextInt();
        
        // 출력
        if(temp < 0)
            System.out.println("ice");
        else if(temp >= 100)
            System.out.println("vapor");
        else
            System.out.println("water");
    }
}
