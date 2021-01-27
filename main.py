from playsound import playsound
import os
import random
from time import sleep


def get_num_file_dict():
    d = {}
    sound_files = os.listdir("./Sounds_0to1000")
    for file in sound_files:
        # print(file)
        # print(file.split(".")[0])
        d[file.split(".")[0]] = file
    return d


if __name__ == "__main__":
    num_file_dict = get_num_file_dict()
    total = 0
    correct = 0
    
    if int(input("Print 1 to Start: ")) == 1:
        while True:
            num = random.randint(0,1000)
            total = total + 1
            playsound("./Sounds_0to1000/"+str(num)+".mp3")
            your_ans = input("Input your answer: (r to replay)")
            
            while your_ans == "r":
                playsound("./Sounds_0to1000/" + str(num) + ".mp3")
                your_ans = input("Input your answer: (r to replay)")
                
            if int(your_ans) == num:
                correct = correct + 1
                print(f"Correct! Correct {correct} / Total {total} = {correct/total * 100:.1f}%")
        
            elif int(your_ans) is not num:
                print(f"Wrong, Correct Ans:{num}")
                while int(your_ans) != num:
                    playsound("./Sounds_0to1000/" + str(num) + ".mp3")
                    your_ans = input("Input your answer: ")
                sleep(1)
