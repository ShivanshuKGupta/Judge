#include <stdio.h>

int main() {
    char str[50];
    scanf("%s", str);
    int len;
    for (len = 0; str[len] != '\0'; ++len)
        ;
    printf("%d", len + 1);
    return 0;
}