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
  int quadrant;
  vector<int> features;
};


/**
** Estructura que almacena los datos de todos los punto de interés de un iris y las coordenadas de su centro
*/
struct image
{
  int centerX;
  int centerY;
  int radio;
  vector<datasPoint> datasFile;
};

static const int BEGIN_DATAS_POINTS = 1;
static const int NUM_LINES_FEATURES = 11;
static const int NUM_COORDS_POINT = 2;


void setValuesIris(string str, string sep, image &image){
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
    image.radio = atoi(arr[5].c_str());
}


/**
** Método que lee los fichero puntos de interes de cada imagen
**  y los almacena en la estructura correspondiente "image"
*/
void readFeatures(char* path, vector<image> &images)
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
  struct image files;


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

/**
** Método que lee el fichero de propiedades del iris y le establece a cada imagen
**  las coordenas de su centro y el radio
*/
void readCenterIris(char* path, vector<image> &images)
{
  DIR* directorio;
  struct dirent* elemento;
  ifstream infile;
  string type, pathFile, nameFile, line;
  int pos, i = 0;

  directorio = opendir(path);

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
      setValuesIris(line, " ", images[i]); // Saves the line in structure "datasIris"
      infile.close();
      i++;
    }

    elemento = readdir (directorio); // Reading the next element from directory
  }

}


/**
** Método que le establece a los puntos de interés de cada imagen el cuadrante al que 
**  pertenece en función de sus coordenadas
*/
void setQuadrant(vector<image> &images)
{
  struct image img;
  int pX, pY, cX, cY,r;
 
  
  for (int i = 0; i < images.size(); i++)
  {
    cX = images[i].centerX;
    cY = images[i].centerY;
    r = images[i].radio;
    //cout << "cX: " << cX << "  " << "cY: " << cY << "   " << "r: " << r << endl;
    for (int j = 0; j < images[i].datasFile.size(); j++)
    {
      pX = images[i].datasFile[j].posX;
      pY = images[i].datasFile[j].posY;

      if (((pX > cX) && (pX < (cX + r))) && ((pY > cY) && (pY < (cY + r))))
        images[i].datasFile[j].quadrant = 1;
      else
      {
        if (((pX < cX) && (pX > (cX - r))) && ((pY > cY) && (pY < (cY + r))))
          images[i].datasFile[j].quadrant = 2;
        else
        {
          if (((pX < cX) && (pX > (cX - r))) && ((pY < cY) && (pY > (cY - r))))
            images[i].datasFile[j].quadrant = 3;
          else
            if (((pX > cX) && (pX < (cX + r))) && ((pY < cY) && (pY > (cY - r))))
              images[i].datasFile[j].quadrant = 4;
        }
      }
    }
  } 

}


/**
** Método que imprime por pantalla los datos de los puntos de interés de cada imagen
*/
void printFeatures(vector<image> images)
{
  for (int i = 0; i < images.size(); i++)
  {
    for (int j = 0; j < images[i].datasFile.size(); j++)
    {
      cout << "X: " << images[i].datasFile[j].posX << "   " << "Y: " << images[i].datasFile[j].posY << "    " << "cuadrante: " << images[i].datasFile[j].quadrant << endl;
    }
  }
}


/** @function main */
int main( int argc, char** argv )
{
  vector<image> images;
  readFeatures(argv[1], images);
  readCenterIris(argv[2], images);
  setQuadrant(images);
  //cout << images.size() << endl;
  printFeatures(images);

  return 0;
}










