#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <cmath>

using namespace cv;
using namespace std;

double alpha = 0.8; /**< Simple contrast control */
int beta = 5;  /**< Simple brightness control */

int main(int argc, char** argv )
{
    Mat image, blur, borde, new_image, dst;
    Point center;
    
    if ( argc != 2 )
    {
        printf("usage: ./DisplayImage <Image_Path>\n");
        return -1;
    }

    
    image = imread(argv[1], CV_LOAD_IMAGE_GRAYSCALE);
    center.x = 192;
    center.y = 159;

    //Dibuja el segundo círculo perteneciente al borde exterior
    circle(image, center, 107, Scalar(230,230,255), 2);

    vector<int> compression_params;
    compression_params.push_back(CV_IMWRITE_PNG_COMPRESSION);
    compression_params.push_back(9);

    imwrite("test2.png", image, compression_params);
    
    // crea una ventana 
    namedWindow("Display Image", WINDOW_AUTOSIZE );

    // muestra la imagen en la ventana creada  
    imshow("Display Image", image);

    // pausa la ejecución del programa
    waitKey(0);

    return 0;
}