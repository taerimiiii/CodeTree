import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 변수 선언
        int gender, age;
        
        // 입력
        gender = sc.nextInt();
        age = sc.nextInt();

        // gender가 0인지 1인지 판단하기
        if(gender == 0) {
            // gender가 0일 때, age가 19이상이면 MAN이, 19보다 작다면 BOY가 됩니다.
            if(age >= 19)
                System.out.println("MAN");
            else
                System.out.println("BOY");
        }
        else {
            // gender가 1일 때, age가 19이상이면 WOMAN이, 19보다 작다면 GIRL이 됩니다.
            if(age >= 19)
                System.out.println("WOMAN");
            else
                System.out.println("GIRL");
        }
    }
}
