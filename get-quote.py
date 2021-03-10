import random

def main():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = last = len(quotes) - 1
  rnd = random.randint(0, last)
  print(quotes[rnd])
  # second quote
 # print(quotes[rnd-1])
  #Want user input to add quote to list after getting a quote
  #with open("quotes.txt", "a") as f:
#    f.append(new_quote)



if __name__== "__main__":
    main()
