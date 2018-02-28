/*******************************************************************************************************
*** This method apply the algoritmh CLAHE to the segmentation of iris to the images's database CASIA ***  
********************************************************************************************************/


#include "datasImage.h" 
#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <fstream>
#include <iostream>
#include <sys/stat.h>
#include <cmath>
#include <boost/algorithm/string/split.hpp>
#include <vector>
#include <errno.h>

static const int BEGIN_DATAS_POINTS = 1;
static const int NUM_LINES_FEATURES = 11;
static const int NUM_COORDS_POINT = 2;

void datasImage::readFeatures(const char* pathFile)
{
  string pathFile2, str, sep = " ";
  int ini = 0, lineFeature = 0, dataPoint = 0;
  char* cstr;
  char* current;
  bool isPoint = true;
/*
  ifstream file(pathFile); // read the file

  while (getline(file, str))
  {
    if (ini >= BEGIN_DATAS_POINTS) // se comienza donde inicia los datos de los puntos
    {
      if (isPoint) // coordenadas del punto
      {
        dataPoint = 0;
        cstr = const_cast<char*>(str.c_str());
        current = strtok(cstr, sep.c_str());

        while(current != NULL && dataPoint < NUM_COORDS_POINT){
            if (dataPoint == 0)
              posX = atoi(current);
            else
              posY = atoi(current);

            current = strtok(NULL, sep.c_str());
            dataPoint++;
        }

        isPoint = false;
      }
      else // características de cada punto
      {
        if (lineFeature < NUM_LINES_FEATURES)
        {
          cstr = const_cast<char*>(str.c_str());
          current = strtok(cstr, sep.c_str());

          while(current != NULL){
              features.push_back(atoi(current));
              current = strtok(NULL, sep.c_str());
          }

          lineFeature++;

          if (lineFeature == NUM_LINES_FEATURES)
          {
            isPoint = true;
            lineFeature = 0;
          }
        }
          
      }

    }

    ini++;
  }*/
}

int datasImage::getPosX()
{
  return posX;
}

int datasImage::getPosY()
{
  return posY;
}

vector<int> datasImage::getFeatures()
{
  return posX;
}


