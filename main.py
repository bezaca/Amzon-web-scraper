from time import sleep
from module.scraper import check_price


# Execute main program
# For default , the program will execute every 2 hours

def time_wait(time_in_hours):
    # modify this function if you need to change timing of execution
    return sleep(60 * 60 * time_in_hours)


if __name__ == '__main__':
    while True:
        check_price()
        time_wait(2)
