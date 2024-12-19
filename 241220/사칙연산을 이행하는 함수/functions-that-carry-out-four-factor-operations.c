#include <stdio.h>

void plus(int x, int y);
void minus(int x, int y);
void mult(int x, int y);
void div(int x, int y);

int main() {
    int x, y;
    char a;

    scanf("%d %c %d", &x, &a, &y);

    if (a == '+') {
        plus(x, y);
    }
    else if (a == '-') {
        minus(x, y);
    }
    else if (a == '*') {
        mult(x, y);
    }
    else {
        div(x, y);
    }
    return 0;
}

void plus(int x, int y)
{
    printf("%d + %d = %d", x, y, x+y);
}

void minus(int x, int y)
{
    printf("%d - %d = %d", x, y, x-y);
}

void mult(int x, int y)
{
    printf("%d * %d = %d", x, y, x*y);
}

void div(int x, int y)
{
    printf("%d / %d = %d", x, y, x/y);
}
