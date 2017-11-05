/*******************************************************************************************************
*** 					   Descriptor keypoints SIFT + detector Fast-Hessian	 					 ***
********************************************************************************************************/
            
#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <fstream>
#include <iostream>
#include <sys/stat.h>
#include <opencv2/opencv.hpp>
#include <string>
#include <cmath>
#include <boost/algorithm/string/split.hpp>
#include <vector>
#include <errno.h>

using namespace cv;
using namespace std;


/** @function main */
int main( int argc, char** argv )
{
	
  system("../../../Lip-vireo/lip-vireo -dir ../../../outputs/images_Segmented_Clahe/ -d dsurf -p SIFT -dsdir ../../../outputs/feature_extraction/Lip-vireo/dsurf/ -c ../../../Lip-vireo/lip-vireo.conf");

  return 0;
}

