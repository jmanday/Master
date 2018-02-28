/******************************************************************************************************
*** This method performs the segmentation of iris to the images's database CASIA with the datas     ***
***    of the circles (cordinate "x" to the two circles, cordinate "y" to the two circles and radio ***
***    also to the two circles)                                                                     ***   
******************************************************************************************************/
            
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

using namespace cv;
using namespace std;

struct datasIris{
  int xCircleInt;
  int yCircleInt;
  int rCircleInt;
  int xCircleExt;
  int yCircleExt;
  int rCircleExt;
};

struct datasIris split(string str, string sep){
    char* cstr = const_cast<char*>(str.c_str());
    char* current;
    vector<string> arr;
    struct datasIris datas;

    current = strtok(cstr, sep.c_str());
    while(current != NULL){
        arr.push_back(current);
        current = strtok(NULL,sep.c_str());
    }

    datas.xCircleInt = atoi(arr[0].c_str());
    datas.yCircleInt = atoi(arr[1].c_str());
    datas.rCircleInt = atoi(arr[2].c_str());
    datas.xCircleExt = atoi(arr[3].c_str());
    datas.yCircleExt = atoi(arr[4].c_str());
    datas.rCircleExt = atoi(arr[5].c_str());

    return datas;
}

/** @function main */
int main( int argc, char** argv )
{

	Mat src;
  DIR* directorio; 
  struct dirent* elemento;
  ifstream infile;
  string nameFile, type, onlyName, pathFile, line;
  int pos = 0;
  struct datasIris datas;
  Mat image;

  directorio=opendir(argv[1]);
  
  if (directorio == NULL) 
  {
    //printf ("Error de Lectura en el Directorio \n");
    cout << "Error de Lectura en el Directorio" << endl;
    return 0;
    
  }

  elemento = readdir(directorio); // getting the first element from directory
  while (elemento != NULL) 
  {
    string nameFile = elemento->d_name; // getting the name's file with extension
    pos = nameFile.find("."); 
    type = nameFile.substr(pos); // getting the extension's file only
    onlyName = nameFile.substr(0, pos); // getting the name's file only
    pathFile = (string)argv[1] + nameFile; // // getting the path's file

    if (type == ".txt") // if the file is a "txt" then we read it 
    {
      infile.open(pathFile);
      getline(infile, line); // Saves the line in STRING.
      datas = split(line, " "); // Saves the line in structure "datasIris"
      infile.close();

      if(image.data)
      {
        Rect roi(datas.xCircleExt-datas.rCircleExt, datas.yCircleExt-datas.rCircleExt, datas.rCircleExt*2,datas.rCircleExt*2); // Making the region to the segmentation of iris
        
        if (0 <= roi.x && 0 <= roi.width && roi.x + roi.width <= image.cols && 0 <= roi.y && 0 <= roi.height && roi.y + roi.height <= image.rows)
        {
          Mat segIris(image, roi); // Making a matrix with the size region "roi"

          vector<int> compression_params;
          compression_params.push_back(CV_IMWRITE_PNG_COMPRESSION);
          compression_params.push_back(9);
          
          string nameImageSegmented = "../../../outputs/images_Segmented/seg-" + onlyName + ".jpg";
          imwrite(nameImageSegmented, segIris, compression_params); // Saving the new matrix in an image jpg
        }

      }
      else
        cout << "Image not loaded";
    }
    else if (type == ".jpg") // if the file is a "jpg" then we load it
    {
      image = imread(pathFile); // Loading the image in a matrix Mat
      if (!image.data)
      {
        cout << "Image not loaded";
        return -1;
      }
    }
    
    elemento = readdir (directorio); // Reading the next element from directory
    
  }
  
  closedir (directorio);
  	

  return 0;
}

