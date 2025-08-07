#include <stdio.h>

int main() {
    float produto_1, produto_2, produto_3;
    float mais_caro = 0, mais_barato = 999;
    char caro[20], barato[20];
    
    // Entrando com os valores dos produtos
    printf("Qual o valor do 1° produto? ");
    scanf("%f", &produto_1);
    printf("Qual o valor do 2° produto? ");
    scanf("%f", &produto_2);
    printf("Qual o valor do 3° produto? ");
    scanf("%f", &produto_3);

    // Verificando o produto mais caro
    if (produto_1 > mais_caro) {
        mais_caro = produto_1;
        snprintf(caro, sizeof(caro), "primeiro produto");
    }
    if (produto_2 > mais_caro) {
        mais_caro = produto_2;
        snprintf(caro, sizeof(caro), "segundo produto");
    }
    if (produto_3 > mais_caro) {
        mais_caro = produto_3;
        snprintf(caro, sizeof(caro), "terceiro produto");
    }

    // Verificando o produto mais barato
    if (produto_1 < mais_barato) {
        mais_barato = produto_1;
        snprintf(barato, sizeof(barato), "primeiro produto");
    }
    if (produto_2 < mais_barato) {
        mais_barato = produto_2;
        snprintf(barato, sizeof(barato), "segundo produto");
    }
    if (produto_3 < mais_barato) {
        mais_barato = produto_3;
        snprintf(barato, sizeof(barato), "terceiro produto");
    }

    // Exibindo o resultado
    printf("O produto mais caro é: %s (%.2f)\n", caro, mais_caro);
    printf("O produto mais barato é: %s (%.2f)\n", barato, mais_barato);

    return 0;
}
