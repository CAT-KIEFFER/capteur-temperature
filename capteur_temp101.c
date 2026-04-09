#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {

     FILE *fichier = fopen("data.txt", "w");

     if (fichier == NULL) {
         printf("erreur ouverture fichier\n");
         return 1;
     }

     srand(time(NULL));

     for (int cycle = 1; cycle <= 10; cycle ++) {

         int temp = rand() % 101;
         char *status = "NOMINAL";

         if (temp < 15) {
             status = "LOW TEMP";
         }
         else if (temp > 80) {
             status = "WARNING";
         }

         fprintf(fichier, "Cycle %d | Temp: %d | Status: %s\n", cycle, temp, status);

     }

     fclose(fichier);

     printf("Données écrites dans le data.txt\n");

     return 0;
}
