#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <cmath>
#include <iostream>
#include <fstream>

using namespace cv;
using namespace std;

// Set threshold and maxValue
double minValue = 0; 
double maxValue = 255; 
int NUM = 3;

Mat exampleAreaMat()
{
	Mat test;
    test = Mat::zeros(4, 4, CV_8UC1);

    test.at<uchar>(0,2) = 255;
   /*	test.at<uchar>(1,1) = 255;
    test.at<uchar>(1,2) = 255;
    test.at<uchar>(2,1) = 255;
    test.at<uchar>(2,2) = 255;
    test.at<uchar>(4,2) = 255;
    test.at<uchar>(4,3) = 255;
    test.at<uchar>(4,4) = 255;
    test.at<uchar>(4,5) = 255;
    test.at<uchar>(5,2) = 255;
    test.at<uchar>(5,3) = 255;
    test.at<uchar>(5,4) = 255;
    test.at<uchar>(5,5) = 255;
    test.at<uchar>(6,2) = 255;
    test.at<uchar>(6,3) = 255;
    test.at<uchar>(6,4) = 255;
    test.at<uchar>(6,5) = 255;
    test.at<uchar>(7,2) = 255;
    test.at<uchar>(7,3) = 255;
    test.at<uchar>(7,4) = 255;
    test.at<uchar>(7,5) = 255; */


    for(int y = 0; y < test.rows; y++ )
    {
    	for( int x = 0; x < test.cols; x++ )
      	{
     		uchar pixel = test.at<uchar>(y, x);
     		printf("%i  ", pixel);
      	}

      	printf("\n");
    }

    return test;
}

int checkValue(Mat bin, int begin1, int begin2)
{
	if ((begin1 < bin.rows) && (begin2 < bin.cols))
	{
		if (bin.at<uchar>(begin1, begin2) == 255)
			return 1;
		else 
			return 0;
	}
}

int regions_pupil(Mat bin, int begin1, int begin2)
{
	int numValueMax = 0, numValueMin = 0, num = 0, k, z;

	for (int i = begin1; i < bin.rows; i++)
    {
    	for (int j = begin2; j < bin.cols; j++)
    	{
    		uchar pixel = bin.at<uchar>(i, j);
    		
        	if (pixel == 255)
        	{
        		k = i, z = j;
        		numValueMax++;

        		num += checkValue(bin, k, z+1);
        		num += checkValue(bin, k+1, z);
        		num += checkValue(bin, k+1, z+1);

        		if (num%3 == 0)
        		{
        			numValueMax += num;
        			k++;
        			z++;
        		}
        	}
        	else
        	{
        		//printf("numValueMax: %i\n", numValueMax);
        		//numValueMax = 0;
        	}
    	}
    	printf("\n");
    } 
    //printf("numValueMax: %i\n", numValueMax);
    //printf("numValueMin: %i\n ", numValueMin);
    return numValueMax;
}

/** @function main */
int main( int argc, char** argv )
{

	//Mat m = exampleAreaMat();
	//int num = regions_pupil(m, 0, 0);
  	//printf("Numero: %i\n", num);


	Mat image, bin, erod;
	ofstream ficheroSalida;
	int erosion_size = 6, num_aux = 0, k = 0, z = 0, vecino = 0, centerX = 0, centerY = 0, radius = 0, aux = 0, end = 0, ini = 0;
	image = imread(argv[1]);

	if(image.empty())
	{
		return -1;
	}

	// 1. We apply binarization
	threshold(image, bin, 130, maxValue, THRESH_BINARY_INV);
	//ficheroSalida.open ("ficheroTexto.txt");

	vector<Vec2i> pupil;
	for(int y = 0; y < bin.rows; y++ )
    {
    	int num = 0;
    	for( int x = 0; x < bin.cols; x++ )
      	{
     		uchar pixel = bin.at<uchar>(y, x);
     		//printf("%i  ", pixel);
     		//ficheroSalida << int(pixel) << " ";
     		if (pixel == 255)
     			num++;
      	}

      	pupil.push_back(Vec2i(y, num));
    }

    vector<Vec3i> regions;
    for (int i = 0; i < pupil.size(); i++)
    {
    	if (pupil[i][1] != 0)
    	{
    		k ++;
    		num_aux++;
    	}
    	else
    	{
    		regions.push_back(Vec3i(i-num_aux, i, num_aux));
    		num_aux = 0;
    		k = 0;
    	}
    }

    // cálculo del radio del primer borde
    vector<Vec2i> pos;
    for (int i = 0; i < regions.size(); i++)
    {
    	if ((regions[i][2] != 0) && (aux < 5))
    	{
    		pos.push_back(Vec2i(regions[i][0], regions[i][1]));
    		radius += regions[i][2];
    		aux = 0;
    	}
    	else
    		if (pos.size() != 0)
    			aux++;

    	printf("Filas con blanco(%i-%i): %i\n", regions[i][0], regions[i][1], regions[i][2]);
    }
    printf("%lu\n", pos.size());
    centerY = (pos[pos.size()-1][1] + pos[0][0]) / 2 + (radius / 2);
    printf("Valor radio: %i\n", radius);
    printf("Valor center: %i\n", pos[0][0]);
    printf("Valor center: %i\n", pos[pos.size()-1][1]);
    printf("Valor centerY: %i\n", centerY);
    circle(image, Point(185, centerY-20), radius/3+10, Scalar(255,255,255), 1);
    circle(image, Point(185, centerY-34), radius/2+55, Scalar(255,255,255), 1);
    //ficheroSalida.close();
/*
	

	// 2. We apply erosion
  	Mat element = getStructuringElement(MORPH_CROSS, Size(2 * erosion_size + 1, 2 * erosion_size + 1), Point(erosion_size, erosion_size));
 
    // Apply erosion or dilation on the image
    //erode(bin,erod,element);

  	//int num = regions_pupil(bin, 0, 0);
  	//printf("Numero: %i\n", num);
*/

    vector<int> compression_params;
    compression_params.push_back(CV_IMWRITE_PNG_COMPRESSION);
    compression_params.push_back(9);

    imwrite("test2.png", image, compression_params);

	// crea una ventana 
    namedWindow("Display Image", WINDOW_AUTOSIZE );

    // muestra la imagen en la ventana creada  
    imshow("Display Image", image);

  	waitKey(0);

  	return 0;
}	