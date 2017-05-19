//
// Created by Jesús García Manday on 19/1/17.
//

#include <cstdlib>
#include <iostream>
#include <time.h>
#include <stdlib.h>
#include "Individuo.h"


/*
 * Constructor por defecto
 *
 */
Individuo::Individuo() {}


/*
 * Constructor por parámetros: el número de genes que tendrá el cromosoma del individuo
 *
 */
Individuo::Individuo(int num_Gens) {

    posInPoblation = -1;
    rFitness = -1;
    numGens = num_Gens;
}


/*
 * Constructor por parámetros: el número de genes que tendrá el cromosoma del individuo, la posición en la población y el valor de la función fitness
 *
 */
Individuo::Individuo(int num_Gens, int posPobl, int vFitness){

    int num = 0;

    posInPoblation = posPobl;
    rFitness = vFitness;
    numGens = num_Gens;

    for(int i = 0; i < numGens; i++) {
        num = rand() % (numGens);
        if (i > 0) {
            while (find(cromosoma.begin(), cromosoma.end(), num) != cromosoma.end())
                num = 0 + rand() % (numGens);
        }

        cromosoma.push_back(num);
    }
}


/*
 * Constructor por parámetros: el cromosoma
 *
 */
Individuo::Individuo(vector<int> newCromosoma) {
    cromosoma = newCromosoma;
}


/*
 * Método para devolver el conjunto de genes de un cromosoma
 *
 */
vector<int> Individuo::getCromosoma() {
    return cromosoma;
}


/*
 * Método para modificar un cromosoma
 *
 */
void Individuo::setCromosoma(vector<int> newCromosoma) {

    for(int i = 0; i < newCromosoma.size(); i++)
        cromosoma.push_back((int &&) newCromosoma.at(i));
}


/*
 * Método para devolver el número de genes de un cromosoma
 *
 */
int Individuo::getNumGens() {
    return numGens;
}


/*
 * Método para imprimir los genes de un cromosoma
 *
 */
void Individuo::printCromosoma(){

    for(int i = 0; i < numGens; i++)
        cout << cromosoma.at(i) << " ";
};


/*
 * Método para borrar los genes de un cromosoma
 *
 */
void Individuo::eraseCromosoma(){
    cromosoma.clear();
};


/*
 * Método para devolver el valor de la función fitness sobre el individuo
 *
 */
int Individuo::getFitness() {
    return rFitness;
}


/*
 * Método para establecer el valor de la función fitness sobre el individuo
 *
 */
void Individuo::setFitness(int valueF) {
    rFitness = valueF;
}


/*
 * Método para devolver la posición del individuo en la población
 *
 */
int Individuo::getPosInPoblation() {
    return posInPoblation;
}


/*
 * Método para establecer la posición de un individuo en la población
 *
 */
void Individuo::setPosInPoblation(int valuePos) {
    posInPoblation = valuePos;
}