import time
import random
def randoms(name):
    r = random.randint(0,10)
    time.sleep(r)
    print(f"{name} married aft {r} years")
    
def main():
    for child in ['mona',"mohmmad",'ali']:
        randoms(child)

if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    total_time= start_time - end_time
    print(f"executed in {total_time}")