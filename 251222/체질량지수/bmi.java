import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 변수 선언
        int h, w;
        
        // 입력
        h = sc.nextInt();
        w = sc.nextInt();

        // 키(cm)에서 키(m)로 단위 환산을 한 뒤 
        // 체질량지수 계산 식에 넣어야 함에 유의합니다.
        int bmi = w * 100 * 100 / (h * h);
        
        // 출력
        System.out.println(bmi);
        if(bmi >= 25)
	    System.out.println("Obesity");
    }
}

