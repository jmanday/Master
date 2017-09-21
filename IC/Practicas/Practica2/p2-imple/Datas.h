//
// Created by Jesús García Manday on 31/12/16.
//

#ifndef P2_DATAS_H
#define P2_DATAS_H

#include <vector>

using namespace std;

class Datas {
    private:
        int n;
        vector<vector<int>> vDistances;
        vector<vector<int>> vWeights;
    public:
        Datas();
        int getNumbersFactories();
        int getNumbersLocations();
        vector<vector<int>> getDistances();
        vector<vector<int>> getWeights();
        vector<int> getDistancesFactoryLocation(int n);
        vector<int> getWeightsFactoryLocation(int n);
};


#endif //P2_DATAS_H
