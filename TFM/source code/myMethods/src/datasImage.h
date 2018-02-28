/*******************************************************************************************************
*** This method apply the algoritmh CLAHE to the segmentation of iris to the images's database CASIA ***  
********************************************************************************************************/

#ifndef DATASIMAGE_H           
#define DATASIMAGE_H     
                       
#include <vector>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <iostream>

using namespace std;

class datasImage
{
  private:
    int posX;
    int posY;
    vector<int> features;

  public:
    datasImage(){};
    ~datasImage(){};
    void readFeatures(const char* pathFile);
    int getPosX();
    int getPosY();
    vector<int> getFeatures();
  
};

#endif