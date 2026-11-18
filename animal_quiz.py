print("Hello Buddy! Let's evaluate your prep..")

print("QUIZ TIME")

score = 0 

print("Ques1 = I am a Big, strong animal. Having a long trunk, and a small tail. Guess who am I ? ")
print("a. Elephant", "b. Tiger", "c. Cat")
Ans1 = input()


if Ans1 == "Elephant" or Ans1 == "elephant" or Ans1 == "ELEPHANT" or Ans1 == "a" or Ans1 == "A" :
    print("Yayy, right one!")
    score += 1
else :
    print("Oops, Wrong one!")

print("Ques2 = I've white and black stripes all over my body, and a little tail. Guess who am I? ")
print("a. Tiger", "b. Dog", "c. Zebra")
Ans2 = input()

if Ans2 == "Zebra" or Ans2 == "zebra" or Ans2 == "ZEBRA" or Ans2 == "c" or Ans2 == "C" :
    print("Yayy, right one!")
    score += 1
else :
    print("Oops, Wrong one!")

print("Ques3 = I've black patches around my eyes, ears and hands. Guess who am I? ")
print("a. Eagle", "b. Panda", "c. Cat")
Ans3 = input()

if Ans3 == "Panda" or Ans3 == "panda" or Ans3 == "PANDA" or Ans3 == "c" or Ans3 == "B":
    print("Yayy, right one!")
    score += 1
else :
    print("Oops, Wrong one!")

print("Ques4 = I am the king of the Jungle. I've brown hairs and I am an carnivore. Guess who am I? ")
print("a. Elephant", "b. Lion", "c. Cat")
Ans4 = input()

if Ans4 == "Lion" or Ans4 == "lion" or Ans4 == "LION" or Ans4 == "b" or Ans4 == "B":
    print("Yayy, right one!")
    score += 1
else :
    print("Oops, Wrong one!")

print("Ques5 = I am the fastest land animal and I've yellow and black spots over my body. Guess who am I? ")
print("a. Ostrich", "b. Tiger", "c. Cheetah")
Ans5 = input()

if Ans5 == "Cheetah" or Ans5 == "cheetah" or Ans5 == "CHEETAH" or Ans5 == "c" or Ans5 == "C":
    print("Yayy, right one!")
    score += 1
else :
    print("Oops, Wrong one!")


print("Your Total Score is :", score)

percentage = (score / 5) * 100
print("Your percentage is:", percentage, "%")
