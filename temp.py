def breed(self):
        '''
        Creates the next generation
        '''
        def russian_roulette():
            
            
            def get_parent_index(thresholds):
                draw = np.random.random() # in [0, 1)
                for i in range(len(thresholds)):
                    if draw < thresholds[i]:
                        return i
                return len(thresholds) - 1    
            
            fitness, train_errors, valid_errors = self.get_fitness()
            normalized_fitness = (fitness - np.min(fitness)) / np.ptp(fitness) # in [0,1]
            self.avg_fitness.append(np.mean(fitness))
            self.update_best(fitness, train_errors, valid_errors)
            thresholds = []
            thresh = 0.0
            fitness_sum = np.sum(normalized_fitness)
            for val in normalized_fitness:
                thresh = thresh + (val/fitness_sum)
                thresholds.append(thresh)
            offsprings = []
            for i in range(int(self.POPULATION_SIZE/2)):
                mom = self.population[get_parent_index(thresholds)]
                dad = self.population[get_parent_index(thresholds)]
                alice, bob = self.crossover(mom, dad)
                offsprings.append(alice)
                offsprings.append(bob)
            return np.array(offsprings, dtype=np.double)
        
        
        offsprings = russian_roulette()
        self.population = self.mutate(offsprings)
    