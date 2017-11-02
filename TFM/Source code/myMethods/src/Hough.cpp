#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <cmath>

using namespace cv;
using namespace std;

/** @function main */
int main( int argc, char** argv )
{

	Mat src = imread(argv[1]);

  if(src.empty())
  {
      return -1;
  }


  for( size_t i = 0; i < src.rows; i++ )
  {
    for (size_t j = 0; j < src.cols; j++)
    {
      int pixel = src.at<uchar>(i, j);
      printf("%i ", pixel);
    }
  }
  
  imshow("source", src);

  waitKey(0);

  return 0;

}