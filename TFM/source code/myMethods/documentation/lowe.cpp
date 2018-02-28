/*******************************************************************************************************
*** This method apply the algoritmh CLAHE to the segmentation of iris to the images's database CASIA ***  
********************************************************************************************************/
            
#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <fstream>
#include <iostream>
#include <sys/stat.h>
#include <string>
#include <cmath>
#include <boost/algorithm/string/split.hpp>
#include <vector>
#include <errno.h>

using namespace std;

/**
** Estructura que almacena las coordenadas de un punto de interés y sus características de alrededor
*/
struct datasPoint
{
  int posX;
  int posY;
  vector<int> features;
};


/**
** Estructura que almacena los datos de todos los punto de interés de un iris y las coordenadas de su centro
*/
struct fileSIFT
{
  int centerX;
  int centerY;
  vector<datasPoint> datasFile;
};

static const int BEGIN_DATAS_POINTS = 1;
static const int NUM_LINES_FEATURES = 11;
static const int NUM_COORDS_POINT = 2;


void split(string str, string sep, fileSIFT &image){
    char* cstr = const_cast<char*>(str.c_str());
    char* current;
    vector<string> arr;

    current = strtok(cstr, sep.c_str());
    while(current != NULL){
        arr.push_back(current);
        current = strtok(NULL,sep.c_str());
    }

    image.centerX = atoi(arr[0].c_str());
    image.centerY = atoi(arr[1].c_str());

}


void readFeatures(char* path, vector<fileSIFT> &images)
{
  DIR* directorio;
  DIR* diraux; 
  struct dirent* elemento;
  string pathFile, str, sep = " ";
  int ini = 0, lineFeature = 0, dataPoint = 0;
  char* cstr;
  char* current;
  bool isPoint = true;
  struct datasPoint data;
  struct fileSIFT files;


  directorio = opendir(path);
  
  if (directorio == NULL) 
    cout << "Error de Lectura en el Directorio" << endl;


  elemento = readdir(directorio); // getting the first element from directory
  while (elemento != NULL) 
  {

    pathFile = (string)path + elemento->d_name; // // getting the path's file

    diraux = opendir(pathFile.c_str());
    if (diraux == NULL) // is a file
    {
      ini = 0;
      ifstream file(pathFile.c_str()); // read the file

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
                  data.posX = atoi(current);
                else
                  data.posY = atoi(current);

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
                  data.features.push_back(atoi(current));
                  current = strtok(NULL, sep.c_str());
              }

              lineFeature++;

              if (lineFeature == NUM_LINES_FEATURES)
              {
                isPoint = true;
                lineFeature = 0;
                files.datasFile.push_back(data);
                data.features.clear();
              }
            }
              
          }

        }

        ini++;
      }

      images.push_back(files);
    }
    
    elemento = readdir (directorio); // Reading the next element from directory
    
  }
  
  closedir (directorio);

}


void readCenterIris(char* path, vector<fileSIFT> &images)
{
  DIR* directorio;
  struct dirent* elemento;
  ifstream infile;
  string type, pathFile, nameFile, line;
  int pos, i = 0;

  directorio=opendir(path);

  if (directorio == NULL) 
    cout << "Error de Lectura en el Directorio" << endl;

  elemento = readdir(directorio); // getting the first element from directory
  while (elemento != NULL) 
  {
    nameFile = elemento->d_name;
    pos = nameFile.find("."); 
    type = nameFile.substr(pos); // getting the extension's file only
    pathFile = path + nameFile; // // getting the path's file
    
    if (type == ".txt") // if the file is a "txt" then we read it 
    {
      infile.open(pathFile);
      getline(infile, line); // Saves the line in STRING.
      split(line, " ", images[i]); // Saves the line in structure "datasIris"
      infile.close();
      i++;
    }

    elemento = readdir (directorio); // Reading the next element from directory
  }

}



void printFeatures(vector<fileSIFT> images)
{
  for (int i = 0; i < images.size(); i++)
  {
    for (int j = 0; j < images[i].datasFile.size(); j++)
    {
      cout << "X: " << images[i].datasFile[j].posX << "   " << "Y: " << images[i].datasFile[j].posY << endl;
    }
  }
}


/** @function main */
int main( int argc, char** argv )
{
  vector<fileSIFT> images;
  readFeatures(argv[1], images);
  readCenterIris(argv[2], images);
  //printFeatures(images);

  return 0;
}










