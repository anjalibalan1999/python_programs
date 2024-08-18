import random
sentence_starter=["About 100 years ago", "IN the 20 BC", "Once upon a tiime"]
character = ["there lived a king", "there was a man named jack", "there lived a farmar"]
time = ["One day", "One full-monn night"]
story_plot=["he was passing by", "he was going for a picnic to"]
place=["the mountains", "the garden"]
second_character = ["he saw a man", "he saw a young lady"]
age=["who seemed to be in late 20s", "who seemed very old and feeble"]
work=["searching something", "digging a well on roadside"]

print(random.choice(sentence_starter)+random.choice(character)+
      random.choice(time)+random.choice(story_plot)+
      random.choice(place)+random.choice(second_character)+
      random.choice(age)+random.choice(work))