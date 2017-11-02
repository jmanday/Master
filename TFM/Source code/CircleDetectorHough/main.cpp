
#include "CircleDetectorHough.h"

int main(int argc, char **argv)
{
	if (argc != 5)
	{
		printf("No hay suficientes argumentos\n");
		return -1;
	}

	string imgSource = argv[1];
	string imgDestiny = argv[2];
	int min_r = atoi(argv[3]);
	int max_r = atoi(argv[4]);

	CircleDetectorHough cdh;
	Mat image = cdh.detect(imgSource, min_r, max_r);
}