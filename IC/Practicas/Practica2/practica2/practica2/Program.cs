using System;
using System.IO;
using System.Timers;
using System.Collections.Generic;




namespace practica2
{	
	class MainClass
	{
		private static string PATH = "/Users/jesusgarciamanday/Desktop/Master/IC/Practicas/Practica2/practica2/resultados.dat";
		private static string PATH2 = "/Users/jesusgarciamanday/Desktop/Master/IC/Practicas/Practica2/qap.datos/tai256c.dat";
		private static string PATH3 = "/Users/jesusgarciamanday//Desktop/Master/IC/Practicas/Practica2/qap.datos/bur26a.dat";
		private static int NUM_PARENTS = 2;
		private static int NUM_INDIVIDUOS_TO_CRUCE = 50;
		private static int NUM_POBLATION = 100;
		private static int NUM_ALET_REPRO = 10;
		private static int NUM_GENERATIONS = 100;
		private static int NUM_GENS = 0;
		private static int INDEX = 0;
		private static Random rnd;
		private static int[][] VDISTANCES, VWEIGHTS;


		/*
		 * @Name: selecctionRussianRoulette
		 * @Params: 
		 * @Description: los padres se seleccionan de acuerdo a su fitness. Se calcula la suma acumulada de todos los fitnnes y con un número aleatorio se selecciona el individuo,
		 * 				a mayor fitness mas posibilidad de ser escogido
		 */
		public static void selecctionRussianRoulette(Individuo[] poblation)
		{
			int sumTotFitness = 0, num, cont = 0, i;

			// cálculo del fitness total acumulado de toda la población
			for (i = 0; i < NUM_POBLATION; i++)
				sumTotFitness += poblation[i].getFitness();

			num = rnd.Next(INDEX, sumTotFitness);

			i = 0;
			while (cont < num)
			{
				cont += poblation[i].getFitness();
				i++;
			}

			Console.WriteLine("Total fitnnes: " + sumTotFitness);
			Console.WriteLine("Numero aleatorio: " + cont);
			Console.WriteLine("Se ha seleccionado el individuo: " + i);
		}


		public static void selecctionWorsts(Individuo[] poblation, Individuo[] worsts)
		{
			List<int> worstFitness = new List<int>();
			int[] auxFitness = new int[NUM_POBLATION];
			int i = 0, k = 0;

			for (i = 0; i < NUM_POBLATION; i++)
				worstFitness.Add(poblation[i].getFitness());

			worstFitness.Sort();
			worstFitness.Reverse();

			i = 0;
			foreach (int m in worstFitness)
			{
				auxFitness[i] = m;
				i++;
			}

			for (int j = 0; j < NUM_POBLATION; j++)
			{
				for (k = 0; k < NUM_POBLATION; k++)
					if (auxFitness[j] == poblation[k].getFitness())
						worsts[j] = poblation[k];	
			}
		}


		public static void selecction(Individuo[] poblation, Individuo[] bests)
		{
			List<int> bestsFitness = new List<int>();
			int[] auxFitness = new int[NUM_POBLATION];
			int i =0, k = 0;

			for (i = 0; i < NUM_POBLATION; i++)
				bestsFitness.Add(poblation[i].getFitness());

			bestsFitness.Sort();

			// el valor del fitness lo paso a vector
			i = 0;
			foreach (int m in bestsFitness)
			{
				auxFitness[i] = m;
				i++;
			}

			// selecciono los mejores
			for (int j = 0; j < NUM_INDIVIDUOS_TO_CRUCE; j++)
			{
				for (k = 0; k < NUM_POBLATION; k++)
				{
					if (auxFitness[j] == poblation[k].getFitness())
						bests[j] = poblation[k];
				}
			}
		}


		/*
		 * @Name: evaluation
		 * @Params: {Individuo[]} poblation
		 * @Description: método que calcula el fitness para cada individuo de la población
		 */
		public static void evaluation(Individuo[] poblation)
		{
			int sumFitness = 0;
			Individuo individuo;

			for (int i = 0; i < poblation.Length; i++)
			{
				individuo = poblation[i];
				for (int j = 0; j < NUM_GENS; j++)
				{
					for (int k = 0; k < NUM_GENS; k++)
						sumFitness += (VWEIGHTS[j][k]) * (VDISTANCES[individuo.getCromosoma()[j]][individuo.getCromosoma()[k]]);
				}

				individuo.setFitness(sumFitness);
				sumFitness = 0;
			}

		}


		public static int evaluation2(int[] cromosoma)
		{
			int sumFitness = 0;

			for (int j = 0; j < NUM_GENS; j++)
			{
				for (int k = 0; k < NUM_GENS; k++)
					sumFitness += (VWEIGHTS[j][k]) * (VDISTANCES[cromosoma[j]][cromosoma[k]]);
			}

			return sumFitness;

		}


		public static void mutacion(Individuo[] nIndividuos)
		{
			int num = 0, orig = 0, dest = 0, aux = 0;
			Individuo individuo;

			for (int i = 0; i < NUM_PARENTS; i++) 
			{
				individuo = nIndividuos[i];
				for (int j = 0; j < NUM_GENS; j++)
				{
					num = rnd.Next(INDEX, NUM_PARENTS);

					if (num == 1) // hay mutación del gen que ocupa la posición j
					{
						orig = rnd.Next(INDEX, NUM_GENS);
						do
						{
							dest = rnd.Next(INDEX, NUM_GENS);

						} while (orig == dest);
						Console.WriteLine(orig + "----" + dest);
						aux = individuo.getCromosoma()[orig];
						individuo.muteGen(orig, individuo.getCromosoma()[dest]);
						individuo.muteGen(dest, aux);
					}
				}
			}
				
		}


		/*
		 * Name: método de mutación
		 * Description: muta los genes de un individuo
		 * Sinopsis: para cada individuo se mutan un número aleatorio de genes
		 */
		public static void mutacion2(Individuo[] nIndividuos)
		{
			int num = 0, pos1 = 0, pos2 = 0, aux = 0;
			Individuo individuo;
			List<int> num_Muted = new List<int>();

			for (int i = 0; i < NUM_INDIVIDUOS_TO_CRUCE; i++)
			{
				individuo = nIndividuos[i];
				num = rnd.Next(INDEX, NUM_GENS);
				for (int j = 0; j < num; j += 2)
				{
					do
					{
						pos1 = rnd.Next(INDEX, NUM_GENS);
						pos2 = rnd.Next(INDEX, NUM_GENS);

					} while ((pos1 == pos2) && (num_Muted.Contains(pos1) == true));

					num_Muted.Add(pos1);
					num_Muted.Add(pos2);
					aux = individuo.getCromosoma()[pos1];
					individuo.muteGen(pos1, individuo.getCromosoma()[pos2]);
					individuo.muteGen(pos2, aux);
				}

				num_Muted.Clear();
			}

		}


		/*
		 * Name: método de mutacion estandar
		 * Description: 
		 * Sinopsis: 
		 */
		public static void mutation_standar(int[][] nCromosomas)
		{
			int i, j, num, pos1, pos2, aux;


			for (i = 0; i < NUM_INDIVIDUOS_TO_CRUCE; i++)
			{
				num = rnd.Next(INDEX, NUM_GENS);
				for (j = 0; j < num; j++)
				{
					pos1 = rnd.Next(INDEX, NUM_GENS);
					pos2 = rnd.Next(INDEX, NUM_GENS);

					aux = nCromosomas[i][pos1];
					nCromosomas[i][pos1] = nCromosomas[i][pos2];
					nCromosomas[i][pos2] = aux;
				}
			}
		}


		/*
		 * Name: método de mutacion baldwiana
		 * Description: 
		 * Sinopsis: 
		 */
		public static void mutation_baldwiniana(int[][] nCromosomas)
		{
			int i, j, num, pos1, pos2, aux;
			int[][] auxCromosomas = new int[nCromosomas.Length][];

			// Creo la copia de los cromosomas de la nueva poblacion
			for (i = 0; i < nCromosomas.Length; i++)
			{
				auxCromosomas[i] = new int[NUM_GENS];
				for (j = 0; j < NUM_GENS; j++)
					auxCromosomas[i][j] = nCromosomas[i][j];
			}

			// Cruzo un número aleatorio de genes
			for (i = 0; i < NUM_INDIVIDUOS_TO_CRUCE; i++)
			{
				num = rnd.Next(INDEX, NUM_GENS);
				for (j = 0; j < num; j++)
				{
					do
					{
						pos1 = rnd.Next(INDEX, NUM_GENS);
						pos2 = rnd.Next(INDEX, NUM_GENS);

					} while (pos1 == pos2);

					aux = auxCromosomas[i][pos1];
					auxCromosomas[i][pos1] = auxCromosomas[i][pos2];
					auxCromosomas[i][pos2] = aux;

					//Console.WriteLine(evaluation2(auxCromosomas[i]) + "------" + evaluation2(nCromosomas[i]));
					if ((evaluation2(auxCromosomas[i])) > (evaluation2(nCromosomas[i])))
					{
						aux = nCromosomas[i][pos1];
						nCromosomas[i][pos1] = nCromosomas[i][pos2];
						nCromosomas[i][pos2] = aux;
					}
					else
					{
						auxCromosomas[i][pos1] = nCromosomas[i][pos1];
						auxCromosomas[i][pos2] = nCromosomas[i][pos2];
					}
				}
			}
		}


		/*
		 * Name: método de reproducción uniforme
		 * Description: cruza todos los genes con porcentaje del padre y la madre en función del valor del fitness
		 * Sinopsis: cruzo los 20 mejores y creo 40 individuos, luego los intercambios por los 40 peores como máximo
		 */
		public static void reproduction2(Individuo[] poblation, Individuo[] bests, Individuo[] worsts)
		{
			int p1 = 0, p2 = 0, f1 = 0, f2 = 0, aux = 0, v = 0, w = 0, num1 = 0, num2 = 0;
			List<List<int>> listGensChilds = new List<List<int>>();
			List<int> list_aux1 = new List<int>(), list_aux2 = new List<int>();
			int[][] vCromosomas = new int[NUM_INDIVIDUOS_TO_CRUCE][];


			// creo los nuevos individuos con los mejores 20
			for (int i = 0; i < NUM_INDIVIDUOS_TO_CRUCE; i += 2)
			{
				f1 = bests[i].getFitness();
				f2 = bests[i+1].getFitness();

				for (int j = 0; j < NUM_GENS; j++)
				{

					//do
					//{
						p1 = rnd.Next(INDEX, NUM_ALET_REPRO);
						p2 = rnd.Next(INDEX, NUM_ALET_REPRO);

						aux = (p1 > p2) ? i : (i + 1);

						num1 = bests[aux].getCromosoma()[j];
						if (aux == i)
							num2 = bests[i + 1].getCromosoma()[j];
						else
							num2 = bests[i].getCromosoma()[j];

					//} while ((list_aux1.Contains(num1) == false) && (list_aux2.Contains(num2) == false)); 

					if (list_aux1.Contains(num1))
					{
						list_aux1.Add(num2);
						list_aux2.Add(num1);
					}
					else
					{
						list_aux1.Add(num1);
						list_aux2.Add(num2);
					}
				}

				foreach (int m in list_aux1)
					Console.Write(m + " ");
				Console.WriteLine();
				foreach (int m2 in list_aux2)
					Console.Write(m2 + " ");
				listGensChilds.Add(new List<int>(list_aux1));
				listGensChilds.Add(new List<int>(list_aux2));
				list_aux1.Clear();
				list_aux2.Clear();
			}

			
			// Pasamos a vector los cromosomas para cambiarlo por los peores de la poblacion
			foreach (List<int> auxList in listGensChilds)
			{
				vCromosomas[w] = new int[NUM_GENS];
				v = 0;
				foreach (int m in auxList)
				{
					vCromosomas[w][v] = m;
					v++;
				}
				w++;
			}


			// Sustituyo los nuevos individuos por los peores de la población
			selecctionWorsts(poblation, worsts);
			for (int z = 0; z < NUM_INDIVIDUOS_TO_CRUCE; z++)
			{
				worsts[z].setFitness(-1);
				worsts[z].setCromosoma(vCromosomas[z]);

			}

			//mutacion2(worsts);
			evaluation(worsts);
		}


		/*
		 * Name: método de reproducción cruce en un punto
		 * Description: cruza todos los genes desde un punto dado
		 * Sinopsis: 
		 */
		public static void reproduction(Individuo[] poblation, Individuo[] parents, Individuo[] worsts)
		{
			List<int> gensP1 = new List<int>(), gensP2 = new List<int>();
			List<List<int>> listGensParents = new List<List<int>>(), listGensChilds = new List<List<int>>();
			List<int> list_aux = new List<int>();
			int[][] vCromosomas; 
			int num, i, j, k, aux, v, w = 0, num_aux;

			for (i = 0; i < NUM_INDIVIDUOS_TO_CRUCE; i += 2)
			{
				// Introduzco los genes del cromosoma del padre y de la madre en una lista cada uno
				for (j = 0; j < NUM_GENS; j++)
				{
					gensP1.Add(parents[i].getCromosoma()[j]);
					gensP2.Add(parents[i+1].getCromosoma()[j]);
				}

				listGensParents.Add(gensP1);
				listGensParents.Add(gensP2);

				num = rnd.Next(INDEX, NUM_GENS);

				for (k = 0; k < NUM_PARENTS; k++)
				{
					// Le añado al primer individuo la parte de genes de un padre hasta el número "num"
					list_aux.AddRange(listGensParents[k].GetRange(INDEX, num));

					num_aux = num;

					// Le añado ahora los genes del otro padre pero si que se repitan
					while (num_aux < NUM_GENS)
					{
						if (list_aux.Contains(listGensParents[(k + 1) % NUM_PARENTS][num_aux]) == false)
							list_aux.Add(listGensParents[(k + 1) % NUM_PARENTS][num_aux]);
						else
						{
							j = 0;
							while (list_aux.Contains(listGensParents[(k + 1) % NUM_PARENTS][j]) == true)
								j++;

							aux = listGensParents[(k + 1) % NUM_PARENTS][j];
							listGensParents[(k + 1) % NUM_PARENTS][j] = listGensParents[(k + 1) % NUM_PARENTS][num_aux];
							listGensParents[(k + 1) % NUM_PARENTS][num_aux] = aux;

							list_aux.Add(aux);
						}

						num_aux++;
					}

					listGensChilds.Add(new List<int>(list_aux));
					list_aux.Clear();
				}
			}

			vCromosomas = new int[listGensChilds.Count][];
			// Pasamos a vector los cromosomas para cambiarlo por los peores de la poblacion
			foreach (List<int> auxList in listGensChilds)
			{
				vCromosomas[w] = new int[NUM_GENS];
				v = 0;
				foreach (int m in auxList)
				{
					vCromosomas[w][v] = m;
					v++;
				}
				w++;
			}

			// Muto los genes de los nuevos individuos
			//mutation_standar(vCromosomas);
			mutation_baldwiniana(vCromosomas);
			//mutation_lamarckiana(vCromosomas);
			// Sustituyo los nuevos individuos por los peores de la población
			selecctionWorsts(poblation, worsts);
			for (int z = 0; z < NUM_INDIVIDUOS_TO_CRUCE; z++)
			{
				worsts[z].setFitness(-1);
				worsts[z].setCromosoma(vCromosomas[z]);
			}


			evaluation(worsts);	
				
		}


		public static void makePoblation(Individuo[] poblation, int n)
		{
			Individuo individuo;

			for (int i = 0; i < NUM_POBLATION; i++)
			{
				individuo = new Individuo(n, i, -1, rnd);
				poblation[i] = individuo;
			}
		}


		public static void saveResults(List<int> listFit)
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
			Individuo[] poblation = new Individuo[NUM_POBLATION];
			Individuo[] selectedIndivuduos = new Individuo[NUM_INDIVIDUOS_TO_CRUCE];
			Individuo[] worsts = new Individuo[NUM_POBLATION];

			List<int> listResult = new List<int>(), listBests = new List<int>();

			ParseDat p = new ParseDat(PATH2);
			NUM_GENS = p.getGens();
			VDISTANCES = p.getDistances();
			VWEIGHTS = p.getWeights();

			rnd = new Random();

			for (int z = 0; z < NUM_GENERATIONS; z++)
			{
				
				makePoblation(poblation, NUM_GENS);
				evaluation(poblation);
				selecctionRussianRoulette(poblation);
/*
				Console.WriteLine();
				Console.WriteLine("***************GENERACION "+ z + "***************");
				for (int i = 0; i < NUM_POBLATION; i++)
				{
					poblation[i].printCromosoma();
					Console.Write("------ " + poblation[i].getFitness());
					Console.WriteLine();
				
				}
*/
/*				selecction(poblation, selectedIndivuduos);
				reproduction(poblation, selectedIndivuduos, worsts);


				// Guardo el mejor de cada generacion
				for (int j = 0; j < NUM_POBLATION; j++)
					listBests.Add(poblation[j].getFitness());

				listBests.Sort();
				listResult.Add(listBests[INDEX]);
/*				Individuo pInd = poblation[INDEX];
	
				pos = 0;
				for (int j = 1; j < poblation.Length; j++)
				{
					if (poblation[j].getFitness() < pInd.getFitness())
					{
						pInd = poblation[j];
						pos = j;
					}
				}

				listResult.Add(poblation[pos].getFitness());
*/				
			}

			/*			pos = 0;
						foreach (int m in listResult)
						{
							Console.WriteLine("En la generación " + pos + " el mejor fitness es: " + m);
							pos++;
						}
						*/
			//saveResults(listResult);
		}
	}
}
