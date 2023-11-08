import time
from multiprocessing import cpu_count, Pool

def factorize(*args):   

    number_of_values = len(args)
    list_assert = []
    if number_of_values:
        for i in range(number_of_values):
            temp_number_of_values = args[i] 
            result_list = []          
            while temp_number_of_values > 0:
                result = args[i] / temp_number_of_values                
                if result % 1 == 0:                    
                    result_list.append(int(result))
                temp_number_of_values -= 1
            list_assert.append(result_list)    
            
    for el in list_assert:
        return el
    


if __name__ == "__main__":

    numbers = [128, 255, 99999, 10651060]

    start_time = time.time()
    with Pool(cpu_count()) as p:
        result = p.map(factorize, numbers)
        for el in result:
            print(el)
    end_time = time.time()

    time_difference = end_time - start_time
    print(time_difference)



