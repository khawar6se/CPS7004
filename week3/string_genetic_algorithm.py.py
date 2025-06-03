import random
import string

target = 'kings'
pop = ['dfasa','erngs', 'iuoiq' ,'uiqwf','iowsg']
terminate = False

while (terminate == False):
        fitness = []

        def fitness_assignment():
            for x in pop:
                score = 0 
                if x.find('k') == 0:
                    score += 1
                if x.find('i') == 1:
                    score +=1
                if x.find('n') == 2:
                    score +=1
                if x.find('g') == 3:
                    score +=1
                if x.find('s') == 4:
                    score +=1
                fitness.append(score)

        fitness_assignment()

        selection = 0
        for x in range(4):
            if fitness[x] > selection:
                selection = x


        print(selection)
        # print(selection)

        def crossover():
            new_pop = []
            for x in pop:
                y = pop[selection]
                new_pop.append(x[:-3]+y[2:])

            return new_pop

        def mutation():
            words = crossover()
            mutated_words = []
            for x in words:
                index = random.randint(0,4)
                new_text = x[:index] + random.choice(string.ascii_letters) + x[index+1:]
                mutated_words.append(new_text)

            return mutated_words




        
        new_pop =mutation()
        for x in new_pop:
            if x == target:
                terminate = True
                break
        print(pop)
        print(new_pop)
        pop = new_pop

