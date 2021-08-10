#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {

    // int version = argv[1];

    system("touch deploy.py");

    FILE *python;

    python = fopen("deploy.py", "a+");

    fputc(*"import sys, os\n", python);
    fputc(*"version = sys.argv[1]\n", python);
    fputc(*"os.system(f'fandogh image publish --version v{version}')\n", python);
    fputc(*"os.system(f'fandogh service deploy --version v{version} --image bot --name bot')\n", python);

    fclose(python);
}