import time
import random

sentences=[
    "the quick brown fox jumps over the lazy dog",
    "A journey of a thousand miles begins with a single step",
    "this is a way for use to referance the objects of the class",

]

def measure_accuracy(test_sentence,user_input):
    correct_chars=sum(1 for a,b in zip(user_input,test_sentence)if a==b)
    accuracy=(correct_chars/len(test_sentence))*100 if test_sentence else 0
    return accuracy 

def typing_test():
    test_sentence=random.choice(sentences)
    print("type the following sentence as fast as you can")
    print(f"**{test_sentence}**")
    input("press enter to start typing...")
    start_time=time.time()
    user_input=input("\nstart typing:\n")
    end_time=time.time()
    time_taken=end_time-start_time
    # time_taken_mininutes=time_takken/60
    words_count=len(test_sentence.split())
    
    print("results:")
    print(f"time taken:{time_taken :.2f}second")
    print(f"words_typed:{words_count}")
    print(f"typing_speed:{words_count/time_taken:.2f}words per seconds")
    accuracy=measure_accuracy(user_input,test_sentence)
    print(f"accuracy:{accuracy:.2f}%")
    # print(correct_chars)


typing_test()
