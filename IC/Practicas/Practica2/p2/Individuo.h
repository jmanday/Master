//
// Created by Jesús García Manday on 31/12/16.
//

#ifndef P2_INDIVIDUO_H
#define P2_INDIVIDUO_H

#include <vector>

using namespace std;

class Individuo {
    private:
        int numGens;
        int rFitness;
        int posInPoblation;
        vector<int> cromosoma;
    public:
        Individuo();
        Individuo(int numGens);
        Individuo(int numGens, int postPobl, int vFitness);
        Individuo(vector<int> gens);
        vector<int> getCromosoma();
        void setCromosoma(vector<int> gens);
        int getNumGens();
        void printCromosoma();
        void eraseCromosoma();
        int getFitness();
        void setFitness(int valueF);
        int getPosInPoblation();
        void setPosInPoblation(int valuesPos);
};


#endif //P2_INDIVIDUO_H
