/*******************************************************************************************************
*** This method apply the algoritmh CLAHE to the segmentation of iris to the images's database CASIA ***  
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

	Mat src;
  DIR* directorio;
  DIR* diraux; 
  struct dirent* elemento;
  string nameFile, type, onlyName, pathFile;
  int pos1, pos2;
  Mat image, dst;


  directorio = opendir(argv[1]);
  
  if (directorio == NULL) 
  {
    cout << "Error de Lectura en el Directorio" << endl;
    return 0;
    
  }

  elemento = readdir(directorio); // getting the first element from directory
  while (elemento != NULL) 
  {
    string nameFile = elemento->d_name; // getting the name's file with extension
    pathFile = (string)argv[1] + nameFile; // // getting the path's file

    diraux = opendir(pathFile.c_str());
    if(diraux == NULL) // is a file
    {
      pos1 = nameFile.find("-"); 
      pos2 = nameFile.find("."); 
      onlyName = nameFile.substr(pos1, pos2); // getting the name's file only
      
      image = imread(pathFile, CV_LOAD_IMAGE_GRAYSCALE); // Loading the image in a matrix Mat
      
      if (!image.data)
      {
        cout << "Image not loaded" << endl;
      }
      else
      {
        Ptr<CLAHE> clahe = createCLAHE();
        clahe->setClipLimit(4);

        clahe->apply(image,dst);

        vector<int> compression_params;
        compression_params.push_back(CV_IMWRITE_PNG_COMPRESSION);
        compression_params.push_back(9);

        string nameImageSegmented = "../../../outputs/images_Segmented_Clahe/clahe" + onlyName + ".jpg";
        imwrite(nameImageSegmented, dst, compression_params); // Saving the new matrix in an image jpg
      }
    }
  
    elemento = readdir (directorio); // Reading the next element from directory
    
  }
  
  closedir (directorio);
  	

  return 0;
}


