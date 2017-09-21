using System;
using System.Collections.Generic;


namespace practica2
{
	public class Individuo
	{
		private int numGens;
		private int rFitness;
		private int posInPoblation;
		private int[] cromosoma;
        private double probability;


		/*
 		 * Constructor por defecto
 		 *
 		*/
		public Individuo()
		{
		}


		/*
 		 * Constructor por parámetros: el cromosoma que va a tener el individuo
 		 *
 		*/
		public Individuo(List<int> nCromosoma)
		{
			this.posInPoblation = -1;
			this.rFitness = -1;
			this.numGens = nCromosoma.Count;
			this.cromosoma = new int[this.numGens];
            this.probability = -1.0;

			int i = 0;
			foreach (int m in nCromosoma)
			{
				this.cromosoma[i] = m;
				i++;
			}
		}


		/*
 		 * Constructor por parámetros: el cromosoma que va a tener el individuo
 		 *
 		*/
		public Individuo(int[] nCromosoma)
		{
			this.posInPoblation = -1;
			this.rFitness = -1;
			this.numGens = nCromosoma.Length;
            this.probability = -1.0;
			this.cromosoma = new int[this.numGens];
			for (int i = 0; i < nCromosoma.Length; i++)
				this.cromosoma[i] = nCromosoma[i];
		}


		/*
 		 * Constructor por parámetros: el número de genes que tendrá el cromosoma del individuo
 		 *
 		*/
		public Individuo(int numGens)
		{
			this.posInPoblation = -1;
			this.rFitness = -1;
			this.numGens = numGens;
            this.probability = -1.0;
			this.cromosoma = new int[numGens];
		}


		/*
 		 * Constructor por parámetros: el número de genes que tendrá el cromosoma del individuo, la posición en la población y el valor de la función fitness
 		 *
 		*/
		public Individuo(int numGens, int posPobl, int vFitness, Random rnd)
		{
			int num = 0, j = 0;
			bool find = false;

			this.numGens = numGens;
			this.posInPoblation = posPobl;
			this.rFitness = vFitness;
			this.cromosoma = new int[numGens];
            this.probability = -1.0;

			for (int i = 0; i < this.numGens; i++)
			{
				num = rnd.Next(0, numGens);

				if (i > 0)
				{
					j = 0;
					while (j < i)
					{
						if (this.cromosoma[j] == num)
							find = true;
						
						j++;
					}

				}

				if (find == true)
				{
					i--;
					find = false;
				}
				else
					this.cromosoma[i] = num;
			}
		}


		/*
 		 * Método para devolver el conjunto de genes de un cromosoma
		 *
 		*/
		public int[] getCromosoma()
		{
			return this.cromosoma;
		}


		/*
 		 * Método para modificar un cromosoma
 		 *
 		*/
		public void setCromosoma(int[] newCromosoma)
		{
			for (int i = 0; i < this.numGens; i++)
				this.cromosoma[i] = newCromosoma[i];
		}


		/*
 		 * Método para devolver el número de genes de un cromosoma
 		 *
 		*/
		public int getNumGens()
		{
			return numGens;
		}


		/*
 		 * Método para mutar un gen de un cromosoma
 		 *
 		*/
		public void muteGen(int gen, int pos)
		{
			this.cromosoma[pos] = gen;
		}


		/*
 		 * Método para imprimir los genes de un cromosoma
 		 *
 		*/
		public void printCromosoma()
		{
			for (int i = 0; i < this.numGens; i++)
				Console.Write(this.cromosoma[i] + " ");
		}


		/*
 		 * Método para borrar los genes de un cromosoma
 		 *
 		*/
		public void eraseCromosoma()
		{
			for (int i = 0; i < this.numGens; i++)
				this.cromosoma[i] = -1;
		}


		/*
 		 * Método para devolver el valor de la función fitness sobre el individuo
 		 *
 		*/
		public int getFitness()
		{
			return this.rFitness;
		}


		/*
 		 * Método para establecer el valor de la función fitness sobre el individuo
 		 *
 		*/
		public void setFitness(int nFitness)
		{
			this.rFitness = nFitness;
		}


		/*
 		 * Método para devolver la posición del individuo en la población
 		 *
 		*/
		public int getPosInPoblation()
		{
			return this.posInPoblation;
		}


		/*
 		 * Método para establecer la posición de un individuo en la población
 		 *
 		*/
		public void setPosInPoblation(int pos)
		{
			this.posInPoblation = pos;
		}

		/*
         * Método para devolver la probabilidad del individuo en función del fitness
         *
        */
        public double getProbability()
		{
            return this.probability;
		}


		/*
         * Método para establecer la probabilidad del individuo en función del fitness
         *
        */
		public void setProbability(double prob)
		{
			this.probability = prob;
		}
	}
}
