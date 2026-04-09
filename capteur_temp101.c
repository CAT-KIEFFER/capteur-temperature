#include <stdio.h>
#include <stdlib.h>

int main(void) {

     char *status = "NOMINAL";

     for (int cycle = 1; cycle <= 10; cycle ++) {

         int temp = rand() % 101;

         if (temp < 15) {
             status = "LOW TEMP";
         }
         else if (temp <= 80) {
             status = "NOMINAL";
         }
         else {
             status = "WARNING";
         }

         printf("Cycle %d | Temp: %d | Status: %s\n", cycle, temp, status);

     }

     return 0;
}
