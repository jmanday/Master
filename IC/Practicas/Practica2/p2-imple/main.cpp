#include <iostream>
#include <fstream>
#include <dirent.h>
#include <cstdlib>
#include <iostream>
#include <time.h>
#include <stdlib.h>
#include <vector>
#include "Datas.h"
#include "Individuo.h"

using namespace std;

#define PATH "/Users/jesusgarciamanday//Desktop/Master/IC/Practicas/Practica2/qap.datos/"
//#define PATH2 "/Users/jesusgarciamanday//Desktop/Master/IC/Practicas/Practica2/qap.datos/tai256c.dat"
#define PATH2 "/Users/jesusgarciamanday//Desktop/Master/IC/Practicas/Practica2/qap.datos/bur26a.dat"
#define NUM_SELECTED 1
#define NUM_PARENTS 2
#define NUM_REPLACE 2
#define NUM_POBLATION 10

int filesInDirectory(){

    DIR *dir;
    struct dirent *item;

    //PARA RECORRER LOS FICHEROS DENTRO DE UN DIRECTORIO
    dir = opendir(PATH);
    if (dir == NULL) {
        printf ("Error de Lectura en el Directorio \n");
        return EXIT_FAILURE;
    }


    while ((item = readdir(dir)) != NULL){
        printf ("Nombre: %s \t", item->d_name);
        //item = readdir(dir);
    }

    closedir(dir);
}


void evaluation(Individuo *poblation, vector<vector<int>> &distances, vector<vector<int>> &weights){
    int sumFitness = 0;
    Individuo *individuo;

    for(int i = 0; i < NUM_POBLATION; i++){
        individuo = &poblation[i];
        for(int j = 0; j < individuo->getNumGens(); j++){
            for(int k = 0; k < individuo->getNumGens(); k++)
                sumFitness += (weights.at(j)).at(k) * (distances.at(individuo->getCromosoma().at(j))).at(individuo->getCromosoma().at(k));
        }

        individuo->setFitness(sumFitness);
        sumFitness = 0;
    }

}


void getTheWorsts(vector<Individuo> &worsts, vector<Individuo> poblation){

    Individuo one, other;
    int pos = 0, aux = 0;

    one = poblation.at(pos);
    for(int i = 0; i < NUM_PARENTS; i++){
        for(int j = 1; j < poblation.size(); j++){
            other = poblation.at(j);
            if(other.getFitness() > one.getFitness()){
                aux = pos;
                pos = j;
                if((worsts.size() > 0) && (worsts.at(0).getFitness() == other.getFitness()))
                    pos = aux;

                one = poblation.at(pos);
            }
        }

        worsts.push_back((Individuo &&) poblation.at(pos));
        pos = 0;
        one = poblation.at(pos);
    }
}


Individuo getTheBest(vector<Individuo> poblation){

    Individuo one, other;
    int pos = 0;

    one = poblation.at(pos);
    for(int i = 0; i < poblation.size(); i++){
        other = poblation.at(i);
        if(other.getFitness() < one.getFitness()){
            pos = i;
            one = other;
        }
    }

    return poblation.at(pos);
}


void selecction(Individuo *bests, Individuo *poblation){

    Individuo one, other, *aux_poblation = poblation;
    int pos = 0, aux = 0;

    for(int i = 0; i < NUM_PARENTS; i++){
        if((i > 0) && (bests[NUM_PARENTS-1].getPosInPoblation() == pos))
            pos++;

        one = poblation[pos];

        for(int j = 1; j < NUM_POBLATION; j++){
            other = poblation[j];

            if(other.getFitness() < one.getFitness()){
                aux = other.getFitness();

                if(i > 0){
                    if(aux != bests[NUM_PARENTS-1].getFitness()){
                        one = other;
                        pos = j;
                    }

                }
                else{
                    pos = j;
                    one = other;
                }
            }
        }

        bests[i] = poblation[pos];
        pos = 0;
    }
}


bool isInVector(int n, vector<int> vector1){

    bool isValue = false;
    int i = 0;

    while((i < vector1.size()) && (isValue == false)){
        if(n == vector1.at(i))
            return true;
        i++;
    }

    return false;
}


void reproducction(vector<Individuo> &parents, vector<Individuo> &worsts, vector<Individuo> &poblation){

    int nGens = parents.at(0).getNumGens();
    int num = rand() % (nGens), j = 0, aux, aux2, k, pos;
    vector<int> cromosoma;
    vector<Individuo> vIndividuo;
    vector<vector<int>> cromosomasParents;

    cromosomasParents.push_back(parents.at(0).getCromosoma());
    cromosomasParents.push_back(parents.at(1).getCromosoma());

    // Creo los dos nuevos individuos a partir de los cromosomas de los padres
    for(int i = 0; i < parents.size(); i++){
        Individuo individuo = Individuo(nGens);

        while(j <= num){
            aux = (int &&) cromosomasParents.at(i).at(j);
            cromosoma.push_back(aux);
            j++;
        }

        while(j < nGens){
            k = (i + 1) % NUM_PARENTS;
            aux = (int &&) cromosomasParents.at(k).at(j);
            if(isInVector(aux, cromosoma) == true){
                //int m = j % num;
                int m = 0;
                while(isInVector(aux, cromosoma) == true){
                    aux = (int &&) cromosomasParents.at(k).at(m%nGens);
                    m++;
                }
                aux2 = cromosomasParents.at(k).at(j);
                cromosomasParents.at(k).at(j) = aux;
                cromosomasParents.at(k).at((m-1)%nGens) = aux2;
            }

            cromosoma.push_back(aux);
            j++;
        }

        j = 0;
        individuo.setCromosoma(cromosoma);
        vIndividuo.push_back(individuo);
        cromosoma.clear();
        cout << "HIJO : ";
        individuo.printCromosoma();
        cout << "<-------> " << individuo.getFitness() << endl;
    }


    // Introduzco los nuevos individuos en la población reemplazándolos por los dos peores
    getTheWorsts(worsts, poblation);
    cout << "PEOR: ";
    worsts.at(0).printCromosoma();
    cout << "<------> " << worsts.at(0).getFitness() << endl;
    cout << "PEOR: ";
    worsts.at(1).printCromosoma();
    cout << "<------> " << worsts.at(1).getFitness() << endl;
    for(int i = 0; i < NUM_PARENTS; i++){
        pos = worsts.at(i).getPosInPoblation();
        vIndividuo.at(i).setPosInPoblation(pos);
        poblation[pos] = vIndividuo.at(i);
        //poblation.push_back(vIndividuo.at(i), ) = vIndividuo.at(i);
    }
}


void makePoblation(Individuo *poblation, int n_genes){

    Individuo individuo;

    srand(time(NULL));

    for(int i = 0; i < NUM_POBLATION; i++){
        individuo = Individuo(n_genes, i, 0);
        poblation[i] = individuo;
        individuo.eraseCromosoma();
    }
}


int main() {

    int n = 0;
    Individuo poblation[NUM_POBLATION], parents[NUM_PARENTS], worsts[NUM_REPLACE];
    vector<vector<int>> distances;
    vector<vector<int>> weights;
    Individuo indiv;

    Datas datas;


    n = datas.getNumbersFactories();

    distances = datas.getDistances();
    weights = datas.getWeights();

    cout << "Número de fábricas: " << datas.getNumbersFactories() << endl;
    cout << "Número de localizaciones: " << datas.getNumbersLocations() << endl << endl << endl;

    makePoblation((Individuo*)poblation, n);
    evaluation((Individuo*)poblation, distances, weights);

    cout << "--------------PRIMERA GENERACIÓN--------------" << endl;
    for(int i = 0; i < NUM_POBLATION; i++){
        poblation[i].printCromosoma();
        cout << "----------- " << poblation[i].getFitness() << endl;
    }
/*
    for(int j = 0; j < 2; j++){
        selecction(parents, poblation);
        reproducction(parents, worsts, poblation);
        //evaluation(poblation, distances, weights);
    }
*/
    selecction((Individuo*)parents, (Individuo*)poblation);


    cout << endl << "--------------PADRES--------------" << endl;
    cout << parents[0].getFitness() << endl;
    cout << parents[1].getFitness() << endl;

/*
    getTheWorsts(worsts, poblation);
    cout << "--------------PEORES--------------" << endl;
    cout << worsts.at(0).getFitness() << endl;
    cout << worsts.at(1).getFitness() << endl; */


/*    reproducction(parents, worsts, poblation);
    evaluation(poblation, distances, weights);

    cout << endl << "--------------SEGUNDA GENERACIÓN--------------" << endl;
    for(int i = 0; i < poblation.size(); i++){
        poblation.at(i).printCromosoma();
        cout << "----------- " << poblation.at(i).getFitness() << endl;
    }
*/
/*
    cout << endl << "--------------EL MEJOR--------------" << endl;
    cout << getTheBest(poblation).getFitness() << endl;
/*    indiv = getTheBest(poblation);

    cout << poblation.size() << endl;
    cout << "Valor fitness: " << indiv.getFitness() << endl;
    cout << "Posición en la población: " << indiv.getPosInPoblation() << endl;
    cout << "Cromosoma: ";
    indiv.printCromosoma();

    /*
    indiv = poblation.at(getTheBest(resultEval).at(1));
    for(int i = 0; i < n; i++)
        cout << indiv.getCromosoma().at(i) << " ";

    */
/*
    for(int i = 0; i < poblation.size(); i++) {
        cout << "Cromosoma del individuo " << i+1 << ": ";
        poblation.at(i).printCromosoma();
        cout << "----- Resultado de la evaluación: " << resultEval.at(i);
        cout << endl;
    }
*/
    return 0;
}




