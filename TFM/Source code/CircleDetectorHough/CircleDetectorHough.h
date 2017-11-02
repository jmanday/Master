/****************************************************************************
**
** For Copyright & Licensing information, see COPYRIGHT in project root
**
****************************************************************************/

#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <cmath>

using namespace std;
using namespace cv;

typedef vector<unsigned int> IntArray;
typedef vector<IntArray>     Image;

class CircleDetectorHough
{
  public: /* class */
  
    CircleDetectorHough() {}
   ~CircleDetectorHough() {}
  
  public: /* methods */
  
  	Mat detect(string source, int min_r, int max_r);
  
  private: /* methods */
    
    Mat edges(Mat source);
};