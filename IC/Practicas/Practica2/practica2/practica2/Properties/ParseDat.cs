using System;
using System.IO;
using System.Collections.Generic;

namespace practica2
{
	public class ParseDat
	{
		private static int NUM_SIZE = 3;

		private int n;
		private int[][] vDistances;
		private int[][] vWeights;
		private StreamReader file;
		private String path;


		/*
 		 * Constructor por parámetro: path del fichero
 		 *
 		 */
		public ParseDat(String path)
		{
			this.path = path;
			file = File.OpenText(this.path);
			String line, aux = "";
			char[] vaux;
			List<List<int>> laux = new List<List<int>>();
			List<int> values, valuesD, valuesW;
			int i;

			// obtengo el primer valor del fichero que corresponde al número de genes un cromosoma
			//file.Read(vsize, 0, NUM_SIZE);
			line = file.ReadLine();
			this.n = int.Parse(new string(line.ToCharArray()));
			this.vDistances = new int[n][];
			this.vWeights = new int[n][];

			// leo todos los valores del fichero. La matriz de distancias y de pesos
			line = file.ReadLine();
			while (line != null)
			{
				if (line.Length > NUM_SIZE)
				{
					vaux = line.ToCharArray();
					values = new List<int>();
					for (i = 0; i < vaux.Length; i++)
					{
						if (vaux[i] == ' ')
						{
							if (aux != "")
							{
								values.Add(int.Parse(aux));
								aux = "";
							}
						}
						else
						{
							aux += vaux[i];
							if (i == vaux.Length - 1)
								values.Add(int.Parse(aux));
						}
							
					}

					//foreach (int c in values)
					//	Console.Write(c + " ");
					laux.Add(values);
					aux = "";
					//Console.WriteLine();
				}

				line = file.ReadLine();
			}

			// Almaceno los valores de las distancias y pesos en sus respectivas matrices
			for (int j = 0; j < n; j++)
			{
				vDistances[j] = new int[n];
				vWeights[j] = new int[n];

				valuesD = laux[j];
				valuesW = laux[j + n];

				for (int k = 0; k < n; k++)
				{
					vDistances[j][k] = valuesD[k];
					vWeights[j][k] = valuesW[k];
				}
			}

		}


		/*
		 * Método para devolver matriz de distancias
		 * 
		 */
		public int[][] getDistances()
		{
			return vDistances;
		}


		/*
		 * Método para devolver matriz de pesos
		 * 
		 */
		public int[][] getWeights()
		{
			return vWeights;
		}

		/*
		 * Método para devolver el número de genes de un cromosoma
		 * 
		 */
		public int getGens()
		{
			return n;
		}
	}
}
