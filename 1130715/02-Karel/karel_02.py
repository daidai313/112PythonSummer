from stanfordkarel import *
import os

def main():
    """ Karel code goes here! """
    move()
    turn_left()#向右轉
    turn_left()
    turn_left()
    move()
    put_beeper()
    turn_left()#向後轉
    turn_left()
    move()
    turn_left()#向右轉
    turn_left()
    turn_left()
    move()

    #pass


if __name__ == "__main__":
    run_karel_program(os.path.join(os.getcwd(), 'worlds/karel_02'))