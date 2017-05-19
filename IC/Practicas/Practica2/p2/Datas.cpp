//
// Created by Jesús García Manday on 31/12/16.
//

#include "Datas.h"
#include <iostream>
#include <fstream>

#define PATH "/Users/jesusgarciamanday//Desktop/Master/IC/Practicas/Practica2/qap.datos/"
//#define PATH2 "/Users/jesusgarciamanday//Desktop/Master/IC/Practicas/Practica2/qap.datos/tai256c.dat"
#define PATH2 "/Users/jesusgarciamanday//Desktop/Master/IC/Practicas/Practica2/qap.datos/bur26a.dat"

/*
 * Constructor sin parámetros: construye un tipo "Datas" a partir de cargar el contenido de los ficheros .dat en las matrices que tiene como propiedades
 *
 */
Datas::Datas(){
    vector<int> vDatas;
    ifstream file;
    string s, saux = "";
    int j = 1;

    file.open(PATH2);
    while(!file.eof()){
        getline(file, s);

        if(s.length() != 0){
            for(int i = 0; i < s.length(); i++){
                if(s.at(i) != ' ')
                    saux += s.at(i);
                else{
                    while(s.at(i) == ' ')
                        i++;
                    i--;
                    //cout << saux << " ";
                    if(saux.length() != 0)
                        vDatas.push_back(stoi(saux));
                    saux = "";
                }
            }

            //cout << saux << endl;
            vDatas.push_back(stoi(saux));
            saux = "";
        }
    }

    //cout << vDatas.size() << endl;
    n = vDatas.at(0);
    for(int k = 0; k < n; k++) {
        vector<int> auxVDistances, auxVWeights;
        for (int t = 0; t < n; t++, j++) {
            auxVDistances.push_back((int &&) vDatas.at(j));
            auxVWeights.push_back((int &&) vDatas.at(j + (n * n)));
        }
        vDistances.push_back(auxVDistances);
        vWeights.push_back(auxVWeights);
    }
}

/*
 * Método que devuelve el número de fábricas
 *
 */
int Datas::getNumbersFactories() {
    return n;
}

/*
 * Método que devuelve el número de localizaciones
 */
int Datas::getNumbersLocations() {
    return n;
}

/*
 * Método que devuelve la matriz de distancias entre las fábricas y las instalaciones
 */
vector<vector<int>> Datas::getDistances() {
    return vDistances;
}

/*
 * Método que devuelve la matriz de pesos entre las fábricas y las instalaciones
 */
vector<vector<int>> Datas::getWeights() {
    return vWeights;
}

/*
 * Método que devuelve un vector con todas las distancias a las localizaciones de una fábrica
 */
vector<int> Datas::getDistancesFactoryLocation(int n) {
    return vDistances.at(n);
}

/*
 * Método que devuelve un vector con todos los pesos a las localizaciones de una fábrica
 */
vector<int> Datas::getWeightsFactoryLocation(int n) {
    return vWeights.at(n);
}
