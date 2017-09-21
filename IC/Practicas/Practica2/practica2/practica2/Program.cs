using System;
using System.Linq;
using System.IO;
using System.Timers;
using System.Collections.Generic;   




namespace practica2
{

    public enum Replace
    {
        TYPE_SGA = 0,
        TYPE_SSGA = 1,
    };


	public enum Cross
	{
		ONE_POINT = 0,
		N_POINTS = 1,
	};


    public enum Probability
	{
		DEFAULT = -1,
        WINDOWING = 0,
		RANKING_LINEAL = 1,
		RANKING_EXPO = 2,
    }


	public enum Selection
	{
		RULETTE = 0,
		SUS = 1,
        TOURNEO = 2,
	};


    public enum Variante
    {
        BALDWINIANA = 1,
        LAMARCKIANA = 2,
    };

    public enum Optimization
    {
        NEARESTNEIGHBOR = 1,
        OPT2 = 2,
    };


	class MainClass
	{
		private static string PATH = "/Users/jesusgarciamanday/Documents/Master/IC/Practicas/Practica2/practica2/resultados.dat";
		private static string PATH2 = "/Users/jesusgarciamanday/Documents/Master/IC/Practicas/Practica2/qap.datos/tai256c.dat";
		private static string PATH3 = "/Users/jesusgarciamanday/Documents/Master/IC/Practicas/Practica2/qap.datos/bur26a.dat";
		private static int NUM_PARENTS = 10;
		private static int NUM_POBLATION = 100;
		private static int NUM_GENERATIONS = 100;
		private static int NUM_GENS = 0;
        private static int PROB_MUTATION = 1000000;
        private static int NUM_SONS_TO_PARENST = 2;
        private static int NUM_SONS = 10;
        private static int NPOINTS = 2;
		private static int INDEX = 0;
        private static Random RND;
        private static int[][] MDISTANCES, MWEIGHTS;



		/*
         * @Name: calculeProbabilityDefault
         * @Params: {Individuo[]} poblation, {int} totalFitness
         * @Description: método por defecto que calcula la probabilidad para cada individuo de la población en función del fitness
         */
		private static void calculeProbabilityDefault(List<Individuo> poblation, int totalFitness)
        {
            double aux = 0.0;

			for (int j = 0; j < NUM_POBLATION; j++)
			{
				aux = (NUM_POBLATION * (double)poblation[j].getFitness()) / (double)((double)totalFitness * NUM_POBLATION);
                //Console.WriteLine("aux: " + (double)poblation[j].getFitness());
				poblation[j].setProbability(aux);
			}
        }


		/*
         * @Name: calculateProbabilityRanking
         * @Params: {Individuo[]} poblation, {int} typeRanking
         * @Description: método que calcula la probabilidad para cada individuo de la población en función del fitness aplicando el ranking lineal de Baker o
         *              el ranking exponencial
         */
        private static void calculateProbabilityRanking(List<Individuo> poblation, int typeRanking)
        {
			Dictionary<Individuo, int> lIndividuos = new Dictionary<Individuo, int>();
            double max = 2.0, min = 2.0 - max, prob = 0.0, e = Math.E;
			int rank = 1;

			for (int i = 0; i < NUM_POBLATION; i++)
				lIndividuos.Add(poblation[i], poblation[i].getFitness());

			// ordeno los individuos de mayor a menor valor del fitness
			var lIndividuosSorted = lIndividuos.OrderByDescending(pair => pair.Value);


            if (typeRanking == (int)Probability.RANKING_LINEAL)
			{
				// le establezco a cada individuo su probabilidad con el ranking lineal
				foreach (var pair in lIndividuosSorted)
				{
					prob = (double)(1.0 / NUM_POBLATION) * (min + (max - min) * ((double)(rank - 1) / (double)(NUM_POBLATION - 1)));
					pair.Key.setProbability(prob);
					rank++;
				}
			}
            else 
            {
                if (typeRanking == (int)Probability.RANKING_EXPO)
                {
					// le establezco a cada individuo su probabilidad con el ranking exponencial
					foreach (var pair in lIndividuosSorted)
					{
						prob = (double)(1.0 - Math.Pow(e, -rank)) / (double)NUM_POBLATION;
						pair.Key.setProbability(prob);
						rank++;
					}
                }   
            }

		}


		/*
         * @Name: calculateProbabilityWindowing
         * @Params: {Individuo[]} poblation, {int} totalFitness
         * @Description: método que calcula la probabilidad para cada individuo de la población en función del fitness aplicando el método windowing
         */
		private static void calculateProbabilityWindowing(List<Individuo> poblation, int totalFitness)
        {
            List<int> lFitness = new List<int>();
            int worstFitness = 0;
            double aux = 0.0;

            for (int i = 0; i < NUM_POBLATION; i++)
				lFitness.Add(poblation[i].getFitness());
                

            // obtengo el peor fitness
			lFitness.Sort();
			worstFitness = lFitness.Last();

			for (int j = 0; j < NUM_POBLATION; j++)
			{
				aux = (NUM_POBLATION * ((double)poblation[j].getFitness() - (double)worstFitness)) / (double)((double)totalFitness * NUM_POBLATION);
				poblation[j].setProbability(Math.Abs(aux));
			}
        }


		/*
         * @Name: calculateProbability
         * @Params: {Individuo[]} poblation, {int} type_prob
         * @Description: método que calcula la probabilidad para cada individuo de la población en función del fitness
         */
		private static void calculateProbability(List<Individuo> poblation, int type_prob)
        {
            int totalFitness = 0;

            for (int i = 0; i < NUM_POBLATION; i++)
                totalFitness += poblation[i].getFitness();

            switch(type_prob)
            {
                case (int)Probability.WINDOWING:
                    calculateProbabilityWindowing(poblation, totalFitness);
                    break; 
                case (int)Probability.RANKING_LINEAL:
                case (int)Probability.RANKING_EXPO:     
                    calculateProbabilityRanking(poblation, type_prob);
                    break;
                default:
                    calculeProbabilityDefault(poblation, totalFitness);
                    break;
            }

        }


        /*
         * @Name: selectionSUS
         * @Params: {List<Individuo>} poblation
         * @Description: método que selecciona a individuos de la población para realizar el cruce aplicando el algoritmo SUS de James Baker
         * @Return: {List<int>} indexParents (devuelve una lista con el índice de los individuos que serán utilizados para el cruce - sin ordenar)
         */
		private static List<int> selectionSUS(List<Individuo> poblation)
        {
            List<int> indexParents = new List<int>();
            double vRulette = RND.NextDouble(), sumProb = 0, eDistance = RND.NextDouble();
            int p = -1, k = 0;
            bool found = false;

            // obtengo el indice del individuo que tenga esa probabilidad acumulada
            while ((sumProb < vRulette) && (k < NUM_POBLATION))
            {
                sumProb += poblation[k].getProbability();
                k++;
            }

            p = k - 1;
            indexParents.Add(p);

            // obtengo el resto de los índices con los individuos que tengan una probabilidad equidistante del primer individudo seleccionado
            for (int i = 0; i < NUM_PARENTS - 1; i++)
            {
                found = false;
                for (int j = 0; j < NUM_POBLATION && !found; j++)
                {
                    if (Math.Abs(poblation[i].getProbability() - poblation[p].getProbability()) < eDistance) 
                    {
                        indexParents.Add(i);
                        found = true;
                    }
                       
                }

            }

            // si no se encuentran individuos que se situen equidistantes se ponen otra vez los que ya estan
            if (indexParents.Count() < NUM_PARENTS)
            {
                int tam = indexParents.Count();
                for (int i = 0; i < NUM_PARENTS - tam; i++)
                    indexParents.Add(indexParents[i]);
                
            }

            return indexParents;
        }


		/*
         * @Name: selectionRulette
         * @Params: {List<Individuo>} poblation
         * @Description: método que selecciona a individuos de la población para realizar el cruce aplicando el algoritmo de la ruleta
         * @Return: {List<int>} indexParents (devuelve una lista con el índice de los individuos que serán utilizados para el cruce - sin ordenar)
         */
		private static List<int> selectionRulette(List<Individuo> poblation)
        {
            List<int> indexParents = new List<int>();
            List<double> ranges = new List<double>();

			int k;
			double sumProb, totalProb = 0.0, raux;

            //obtengo la suma maxima de probabilidades para
            for (int i = 0; i < NUM_POBLATION; i++)
                totalProb += poblation[i].getProbability();
            
			// creo los rangos de probabilidad para seleccionar a los padres
            for (int i = 0; i < NUM_PARENTS; i++)
            {
                raux = RND.NextDouble();
                while (raux > totalProb)
                    raux = RND.NextDouble();
                    
                ranges.Add(raux);
            }	
			

			// selecciono los índices de los individuos que se van a cruzar en función a su probabilidad de fitness
			for (int j = 0; j < NUM_PARENTS; j++)
			{
				k = 0;
				sumProb = 0.0;
				while (sumProb < ranges[j])
				{
					sumProb += poblation[k].getProbability();
					k++;
				}

				k = k - 1;
				if (j == 0)
				{
					indexParents.Add(k);
				}
				else
				{
					if (indexParents.Contains(k))
						indexParents.Add((k + 1) % NUM_POBLATION);
					else
						indexParents.Add(k);
				}

			}

			return indexParents;
        }


		/*
         * @Name: selectionTourneo
         * @Params: {List<Individuo>} poblation
         * @Description: método que selecciona a individuos de la población para realizar el cruce aplicando el algoritmo de selección por torneo
         * @Return: {List<int>} indexParents (devuelve una lista con el índice de los individuos que serán utilizados para el cruce - sin ordenar)
         */
        private static List<int> selectionTourneo(List<Individuo> poblation)
        {
            List<KeyValuePair<int, int>> daux = new List<KeyValuePair<int, int>>();
            List<int> indexParents = new List<int>(); 
            int k = 0, m = 0;

            for (int i = 0; i < NUM_PARENTS; i++)
            {
                // selecciono el número de individuos al azar
				do
				{
					k = RND.Next(0, NUM_POBLATION);

				} while (k == 0);

                // selecciono los individuos al azar
                for (int j = 0; j < k; j++)
                {
                    m = RND.Next(0, NUM_POBLATION);
                    KeyValuePair<int, int> myItem = new KeyValuePair<int, int>(m, poblation[m].getFitness());
                    daux.Add(myItem);
                }

                // escojo el mejor individuo
                var dauxSorted = daux.OrderBy(pair => pair.Value);
                indexParents.Add(dauxSorted.First().Key);

                daux.Clear();

			}

            return indexParents;
        }


		/*
         * @Name: selecction
         * @Params: {List<Individuo>} poblation, {int} type
         * @Description: método general para seleccionar a los individuos de la población para realizar el cruce
         * @Return: {List<int>} indexParents (devuelve una lista con el índice de los individuos que serán utilizados para el cruce - sin ordenar)
         */
		private static List<int> selection(List<Individuo> poblation, int type, int type_prob){
            calculateProbability(poblation, type_prob);

            List<int> indexParents = null;

            switch(type){
                case (int)Selection.RULETTE:
                    indexParents = selectionRulette(poblation);
                    break;
                case (int)Selection.SUS:
                    indexParents = selectionSUS(poblation);
                    break;
                case (int)Selection.TOURNEO:
                    indexParents = selectionTourneo(poblation);
                    break;
                default:
                    break;
            }

            return indexParents;
    
        }


		/*
         * @Name: optimization2opt
         * @Params: {Individuo[]} poblation, {int} typeVariante
         * @Description:  método de optimización local que emplea
         *              la estrategia 2-opt para buscar la mejor 
         *              solución en un individuo. Para variante baldwiniana 
         *              o lamarckiana
         */
		private static void optimization2opt(List<Individuo> poblation, int typeVariante)
        {
			int sumFitness = 0, auxFitness = 0, aux = 0;
            bool stopped = false;
			Individuo individuo;
			int[] auxCromosoma = new int[NUM_GENS], cromosomaIndiv;

            for (int i = 0; i < NUM_POBLATION; i++)
            {
				individuo = poblation[i];
				cromosomaIndiv = individuo.getCromosoma();
                for (int j = 0; j < NUM_GENS; j++)
                    auxCromosoma[j] = cromosomaIndiv[j];
				
                auxFitness = individuo.getFitness();
                stopped = false;

                for (int j = 0; j < NUM_GENS && stopped == false; j++)
                {
                    for (int k = j + 1; k < NUM_GENS && stopped == false; k++)
                    {
                        aux = auxCromosoma[k % NUM_GENS];
                        auxCromosoma[k % NUM_GENS] = auxCromosoma[j];
                        auxCromosoma[j] = aux;
                        sumFitness = 0;

						for (int x = 0; x < NUM_GENS; x++)
                            for (int z = 0; z < NUM_GENS; z++)
								sumFitness += (MWEIGHTS[x][z]) * (MDISTANCES[auxCromosoma[x]][auxCromosoma[z]]);
						
                        if (sumFitness < auxFitness)
                        {
							individuo.setFitness(sumFitness);
                            stopped = true;
                            if (typeVariante == (int)Variante.LAMARCKIANA)
								individuo.setCromosoma(auxCromosoma);
                        }
                    }
                }
            }
        }


		/*
         * @Name: optimizationNearestNeighbor
         * @Params: {Individuo[]} poblation, {int} typeVariante
         * @Description: método de optimización local que emplea
         *              la estrategia del vecino mas cercano para 
         *              buscar la mejor solución en un individuo. 
         *              Para variante baldwiniana o lamarckiana
         */
		private static void optimizationNearestNeighbor(List<Individuo> poblation, int typeVariante)
        {
            int sumFitness = 0, auxFitness = 0, auxWeight = 0, mWeight = 0, instal = 0, auxDistance = 0, mDistance = 99999999, localiz = 0;
            Individuo individuo;
            int[] auxCromosoma = new int[NUM_GENS], cromosomaIndiv;

            for (int i = 0; i < NUM_POBLATION; i++)
            {
                individuo = poblation[i];
                cromosomaIndiv = individuo.getCromosoma();
                auxFitness = individuo.getFitness();


                // genero la solución local del individuo
                for (int k = 0; k < NUM_GENS; k++)
                {
                    // busco la instalación j que tenga mayor peso de transporte con k
                    for (int j = k + 1; j < NUM_GENS; j++)
                    {
                        auxWeight = MWEIGHTS[k][j % NUM_GENS];
                        if (auxWeight > mWeight)
                        {
                            mWeight = auxWeight;
                            instal = j;
                        }
                    }

                    // busco la localización más cerca a p(k) donde se construirá la instalación j
                    for (int j = k + 1; j < NUM_GENS; j++)
                    {
                        auxDistance = MDISTANCES[cromosomaIndiv[k]][cromosomaIndiv[j % NUM_GENS]];
                        if (auxWeight < mDistance)
                        {
                            mDistance = auxDistance;
                            localiz = cromosomaIndiv[j % NUM_GENS];
                        }
                    }

                    auxCromosoma[instal] = localiz;
                    localiz = instal = 0;
                }

                // se calcula el nuevo valor de la función fitness y se actualiza al individuo
                for (int j = 0; j < NUM_GENS; j++)
                    for (int k = 0; k < NUM_GENS; k++)
                        sumFitness += (MWEIGHTS[j][k]) * (MDISTANCES[auxCromosoma[j]][auxCromosoma[k]]);
                
                if (sumFitness < auxFitness)
                {
                    individuo.setFitness(sumFitness);
                    if (typeVariante == (int)Variante.LAMARCKIANA)
                        individuo.setCromosoma(auxCromosoma);
                }

                sumFitness = 0;
            }
        }

		/*
         * @Name: optimization
         * @Params: {Individuo[]} poblation, {int} typeOptimization, {int} typeVariante
         * @Description:  método de optimización local general
         */
		private static void optimization(List<Individuo> poblation, int typeOptimization, int typeVariante)
        {
            switch(typeOptimization){
                case (int)Optimization.NEARESTNEIGHBOR:
                    optimizationNearestNeighbor(poblation, typeVariante);
                    break;
                case (int)Optimization.OPT2:
                    optimization2opt(poblation, typeVariante);
                    break;
                default:
                    break;
            }
        }



		/*
		 * @Name: evaluation
		 * @Params: {Individuo[]} poblation
		 * @Description: método que calcula el fitness para cada individuo de la población (algoritmo estándar)
		 */
		private static void evaluation(List<Individuo> poblation)
		{
			int sumFitness = 0;
			Individuo individuo;
            int[] cromosoma;

            for (int i = 0; i < NUM_POBLATION; i++)
			{
				individuo = poblation[i];
                cromosoma = individuo.getCromosoma();
				for (int j = 0; j < NUM_GENS; j++)
					for (int k = 0; k < NUM_GENS; k++)
						    sumFitness += (MWEIGHTS[j][k]) * (MDISTANCES[cromosoma[j]][cromosoma[k]]);


				individuo.setFitness(sumFitness);
				sumFitness = 0;
			}
		}


		/*
         * @Name: crossingOnePoint
         * @Params: {int[][]} cromSons, {int[][]} cromParents
         * @Description: método que cruza los indidivuos seleccionados como padres para crear nuevos. De cada
         *              par de individuos padres se crearán dos individuos hijos
         * @Type: cruce en un punto
         * @Return: {int[][]} cromSons (devuelve una matriz con los cromosomas de los nuevos individuos)
         */
		private static void crossingOnePoint(int[][] cromSons, int[][] cromParents)
		{
			int pos, k = 0, c = 0;
			bool found = true;

			pos = RND.Next(INDEX, NUM_GENS); // punto de corte

			// creo los cromosomas de los hijos
			for (int i = 0; i < cromSons.Count(); i += 2)
			{

				// creo los cromosomas para los hijos hasta el punto de cruce
				for (int x = i; x < (i + NUM_SONS_TO_PARENST); x++)
				{
					for (int j = 0; j < pos; j++)
						cromSons[x][j] = cromParents[x][j];
				}


				// continuo creando el cromosoma del primer hijo desde el punto de cruce sin que se repitan los genes
				for (int x = i; x < (i + NUM_SONS_TO_PARENST); x++)
				{
					// controlo los índices
					if (((x + 1) % NUM_SONS_TO_PARENST) == 0)
						c = x - 1;
					else
						c = x + 1;
                    
					for (int j = pos; j < NUM_GENS; j++)
					{
						if (cromSons[x].Contains(cromParents[c][j]))
						{
							k = 0;
							found = true;
							while ((found == true) && (k < pos))
							{
								if (cromSons[x].Contains(cromParents[c][k]))
								{
									k++;
								}
								else
								{
									cromSons[x][j] = cromParents[c][k];
									found = false;
								}
							}
						}
						else
						{
							cromSons[x][j] = cromParents[c][j];
						}
					}
				}

			}
		}


		/*
         * @Name: crossingNPoints
         * @Params: {int[][]} cromSons, {int[][]} cromParents
         * @Description: método que cruza los indidivuos seleccionados como padres para crear nuevos. De cada
         *              par de individuos padres se crearán dos individuos hijos
         * @Type: cruce en un punto
         * @Return: {int[][]} cromSons (devuelve una matriz con los cromosomas de los nuevos individuos)
         */
		private static void crossingNPoints(int[][] cromSons, int[][] cromParents)
		{
            List<int> lPos = new List<int>();
            int k = 0, c = 0, ini = 0, end = 0;
			bool found = true;

            // cálculo de los puntos de corte
            for (int i = 0; i < NPOINTS; i++){
                k = RND.Next(INDEX, NUM_GENS);

                if (i != 0){
                    while(lPos.Contains(k))
                        k = RND.Next(INDEX, NUM_GENS);

                    lPos.Add(k);
                }
                else
                    lPos.Add(k);
            }
               
            lPos.Sort();

			// introduzco todos los genes en los cromosomas de los hijos
            for (int i = 0; i < cromSons.Count(); i += 2)
            {
				// introduzco los genes desde la posición 0 a p1 y desde p2 al final en los cromosomas de los hijos
				for (int x = i; x < (i + NUM_SONS_TO_PARENST); x++)
				{
                    ini = 0;
                    for (int y = 0; y < lPos.Count(); y++)
                    {
                        end = lPos[y] + ((NUM_GENS - lPos[y]) * y);
                        ini = lPos[y] * y;
						for (; ini < end; ini++)
							cromSons[x][ini] = cromParents[x][ini];
                        
                    }
				}


				// introduzco los genes que existen entre la posición p1 y p2
                for (int x = i; x < (i + NUM_SONS_TO_PARENST); x++)
                {
                    // controlo los índices
                    if (((x + 1) % NUM_SONS_TO_PARENST) == 0)
                        c = x - 1;
                    else
                        c = x + 1;
                    
                    for (int j = lPos.First(); j < lPos.Last(); j++)
                    {
                        if (cromSons[x].Contains(cromParents[c][j]))
                        {
							found = true;
                            for (int y = 0; y < lPos.Count() && found == true; y++)
                            {
                                end = lPos[y] + ((NUM_GENS - lPos[y]) * y);
                                ini = lPos[y] * y;
                                for (; ini < end; ini++){
                                    if (!cromSons[x].Contains(cromParents[c][ini])){
										cromSons[x][j] = cromParents[c][ini];
										found = false;
                                    }
                                }
                            }
                        }
                        else 
                        {
                            cromSons[x][j] = cromParents[c][j];
                        }
                    }
                }
			}

		}


		/*
         * @Name: crossing
         * @Params: {List<int>} indexIndividuosSelected, {List<Individuo>} poblation
         * @Description: método que cruza los indidivuos seleccionados como padres para crear nuevos. De cada
         *              par de individuos padres se crearán dos individuos hijos
         * @Type: cruce en un punto
         * @Return: {int[][]} cromSons (devuelve una matriz con los cromosomas de los nuevos individuos)
         */
		private static int[][] crossing(List<Individuo> poblation, List<int> indexIndividuosSelected, int type){
            int pInd = 0, pos = 0;
            int[][] cromSons = new int[NUM_SONS][];
            int[][] cromParents = new int[NUM_PARENTS][];

            // creo un cromosoma para cada uno de los hijos con valores -1
            for (int i = 0; i < NUM_SONS; i++){
                cromSons[i] = new int[NUM_GENS];
                for (int j = 0; j < NUM_GENS; j++)
                    cromSons[i][j] = -1;
            }

       
            // obtengo los cromosomas de los individuos seleccionados como padres
            for (int i = 0; i < NUM_PARENTS; i++){
                pInd = indexIndividuosSelected[i];
                cromParents[i] = poblation[pInd].getCromosoma();
            }


            // choosing type of cross
            switch(type){
                case (int)Cross.ONE_POINT:
                    crossingOnePoint(cromSons, cromParents);
                    break;
                case (int)Cross.N_POINTS:
                    crossingNPoints(cromSons, cromParents);
                    break;
                default:
                    break;
			}



            // se le aplica mutación a los cromosomas de los nuevos individuos
            for (int i = 0; i < cromSons.Count(); i++){
                int auxC;
                int[] auxCrom = cromSons[i];
                List<int> lPosMut = new List<int>();

                // por cada gen del cromosoma obtengo una probabilidad de que sea mutado
                for (int j = 0; j < auxCrom.Count(); j++){
                    pos = RND.Next(INDEX, PROB_MUTATION); // probabilidad de mutación
                    if (pos < auxCrom.Count()){
                        lPosMut.Add(pos);
                    }
				}

                // se mutan los genes si hay mas de uno para mutar
                if (lPosMut.Count() > 1) {
                    for (int c = 0; (c + 1) < lPosMut.Count(); c++){
                        auxC = auxCrom[c];
                        auxCrom[c] = auxCrom[c + 1];
                        auxCrom[c + 1] = auxC;
                    }
                }
            }

            // devulve los cromosomas de los nuevos individuos    
            return cromSons;
               
        }


		/*
         * @Name: replace_SGA
         * @Params: {List<Individuo>} poblation, {List<int>} individuosSelected, {int[][]} cromIndividuos
         * @Description: método que reemplaza a los padres por los hijos
         */
		private static void replace_SGA(List<Individuo> poblation, List<int> individuosSelected, int[][] cromIndividuos){
            for (int i = 0; i < cromIndividuos.Count(); i++){
                int pos = individuosSelected[i];
                poblation[pos].setCromosoma(cromIndividuos[i]);
            }

        }



		/*
         * @Name: replace_SSGA
         * @Params: {List<Individuo>} poblation, {int[][]} cromIndividuos
         * @Description: método que reemplaza un descendiente en cada generación por 
         *              el individuo que tenga peor fitness de la población
         */
		private static void replace_SSGA(List<Individuo> poblation, int[][] cromIndividuos){
            Dictionary<int, int> lIndividuos = new Dictionary<int, int>();
            List<int> individuosToReplace = new List<int>();

            // creo un diccionario con el valor de la función fitnnes y su índice de cada individuo
            for (int i = 0; i < NUM_POBLATION; i++){
                lIndividuos.Add(i, poblation[i].getFitness());
            }

            // ordeno el diccionario descendentemente y obtengo el índice de los que tengan el mayor fitness
            var lIndividuosSorted = lIndividuos.OrderByDescending(pair => pair.Value);
			foreach (var pair in lIndividuosSorted)
			{
                int key = pair.Key;
                individuosToReplace.Add(key);
				
			}

            // reemplazo los individuos
            for (int i = 0; i < cromIndividuos.Count(); i++){
                int p = individuosToReplace[i];
                poblation[p].setCromosoma(cromIndividuos[i]);
            }

        }


		/*
         * @Name: replace
         * @Params: {List<Individuo>} poblation, {List<int>} individuosSelected, {int[][]} cromIndividuos
         * @Description: método que introduce en la población a los nuevos individuos
         *              que sustituyen a otros que ya están
         */
		private static void replace(List<Individuo> poblation, List<int> individuosSelected, int[][] cromIndividuos, int type){
            switch(type){
                case (int)Replace.TYPE_SGA:
                    replace_SGA(poblation, individuosSelected, cromIndividuos);
                    break;
                case (int)Replace.TYPE_SSGA:
                    replace_SSGA(poblation, cromIndividuos);
                    break;
                default:
                    break;    
            }

        }


		/*
         * @Name: verChilds
         * @Params: {List<Individuo>} poblation, {int[][]} cromIndividuos
         * @Description: método que visualiza los cromosomas de los individuos hijos
         */
		private static void verChilds(List<Individuo> poblation, int[][] cromIndividuos)
        {
			Console.WriteLine();
			Console.WriteLine("HIJOS");
			for (int i = 0; i < cromIndividuos.Count(); i++)
			{
				for (int j = 0; j < cromIndividuos[i].Count(); j++)
					Console.Write(" " + cromIndividuos[i][j]);

				Console.WriteLine();
			}

			Console.WriteLine();
        }


		/*
         * @Name: verParents
         * @Params: {List<Individuo>} poblation, {List<int>} indexIndividuosSelected
         * @Description: método que visualiza los cromosomas de los individuos seleccionados como padres
         */
		private static void verParents(List<Individuo> poblation, List<int> indexIndividuosSelected)
		{
			Console.WriteLine();
			Console.WriteLine("PADRES");
			for (int i = 0; i < indexIndividuosSelected.Count(); i++)
			{
				for (int j = 0; j < poblation[indexIndividuosSelected[i]].getCromosoma().Count(); j++)
					Console.Write(" " + poblation[indexIndividuosSelected[i]].getCromosoma()[j]);

				Console.WriteLine();
			}

			Console.WriteLine();
		}


		/*
         * @Name: verPoblation
         * @Params: {List<Individuo>} poblation
         * @Description: método que visualiza los cromosomas de la población actual
         */
		private static void verPoblation(List<Individuo> poblation){
            Console.WriteLine("POBLACIÓN");
            for (int i = 0; i < poblation.Count(); i++){
                for (int j = 0; j < poblation[i].getCromosoma().Count(); j++)
                    Console.Write(" " + poblation[i].getCromosoma()[j]); 

                Console.Write(" --- " + poblation[i].getFitness());
				Console.WriteLine();
            }

            Console.WriteLine();
        }


		/*
         * @Name: obteinBestFitness
         * @Params: {List<Individuo>} poblation
         * @Description: método que obtiene el mejor fitness de la población actual
         */
		private static void obteinBestFitness(List<Individuo> poblation){
            Dictionary<int[], int> lIndividuos = new Dictionary<int[], int>();

            for (int i = 0; i < poblation.Count(); i++){
                lIndividuos.Add(poblation[i].getCromosoma(), poblation[i].getFitness());
            }

			// ordeno el diccionario ascendentemente y obtengo el índice de los que tengan el mayor fitness
            var lIndividuosSorted = lIndividuos.OrderBy(pair => pair.Value);

            Console.WriteLine("Mejor coste: " + lIndividuosSorted.First().Value);
            Console.Write("Solución encontrada: ");
            for (int i = 0; i < lIndividuosSorted.First().Key.Count(); i++)
                Console.Write(" " + lIndividuosSorted.First().Key[i]);

            Console.WriteLine();
			Console.WriteLine();
        }


		/*
         * @Name: printCabecera
         * @Params: 
         * @Description: método visualiza por pantalla los parámetros correspondientes al tipo 
         *                 algoritmo, de selección, etc, de la prueba ejecutada
         */
        private static void printHeader()
        {
            Console.WriteLine("Algoritmo genético empleado: Variante Lamarckiana");
            Console.WriteLine("Tamaño de la población: " + NUM_POBLATION);
            Console.WriteLine("Número de generaciones: " + NUM_GENERATIONS);
            Console.WriteLine("Mecanismo de selección: selección proporcional - Ruleta");
            Console.WriteLine("Mecanismo de reemplazo: Modelo generacional (SSGA)");
            Console.WriteLine("Operador de cruce: Cruce en n puntos");
            Console.WriteLine("Operador de mutación: Mutación estándar");
            Console.WriteLine("Optimización local: 2-opt");
        }


		/*
         * @Name: makePoblation
         * @Params: {List<Individuo> poblation}, {int} n
         * @Description: método para crear la población inicial de individuos
         */
		private static void makePoblation(List<Individuo> poblation, int n)
		{
			Individuo individuo;

			for (int i = 0; i < NUM_POBLATION; i++)
			{
				individuo = new Individuo(n, i, -1, RND);
				poblation.Add(individuo);
			}
		}


		private static void saveResults(List<int> listFit)
		{
			DateTime thisDay = DateTime.Today;
			StreamWriter file;

			listFit.Sort();
			String result = "Resultado de la función de evaluación para " + NUM_POBLATION + " individuos y " + NUM_GENERATIONS + " generaciones: " + listFit[0].ToString() + " a fecha: " + thisDay.ToString();
			Console.WriteLine("Resultado de la función de evaluación para " + NUM_POBLATION + " individuos y " + NUM_GENERATIONS + " generaciones: " + listFit[0].ToString() + " a fecha: " + thisDay.ToString());

			file = new StreamWriter(PATH,true);
			file.WriteLine(result);
			file.Close();

		}


		public static void Main(string[] args)
		{
            List<Individuo> poblation = new List<Individuo>();
            List<int> indexIndividuosSelected;
            int[][] cromIndividuos;

			ParseDat p = new ParseDat(PATH2);
			NUM_GENS = p.getGens();
			MDISTANCES = p.getDistances();
			MWEIGHTS = p.getWeights();

			RND = new Random();

			makePoblation(poblation, NUM_GENS);
            evaluation(poblation);

            //verPoblation(poblation);
            //obteinBestFitness(poblation);

            for (int z = 0; z < NUM_GENERATIONS; z++)
            {
                Console.WriteLine("Generacion: " + z);
                indexIndividuosSelected = selection(poblation, (int)Selection.RULETTE, (int)Probability.DEFAULT); // obtengo el índice de los individuos seleccionados para ser cruzados, es decir, los padres
                cromIndividuos = crossing(poblation, indexIndividuosSelected, (int)Cross.N_POINTS); // cruce de los individuos
                replace(poblation, indexIndividuosSelected, cromIndividuos, (int)Replace.TYPE_SSGA); // se introducen los nuevos individuos en la población
                optimization(poblation, (int)Optimization.OPT2, (int)Variante.BALDWINIANA); // método de optimización local
                evaluation(poblation);
				//verPoblation(poblation);
				//obteinBestFitness(poblation);
			}

            printHeader();
            obteinBestFitness(poblation);
			//saveResults(listResult);
		}
	}
}
