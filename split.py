
def moreItems():
    more = input("Keep Going?(y/n): ")
    return False if more == 'n' else True

def getItem():
    buyer = input("For who: ").replace(" ", "").split(',')
    cost = float(input("How much: "))
    cost /= len(buyer)

    return (buyer, round(cost, 2))

def main():
    # takes in people involved in purchase, regularized strings
    people = input("Who bought things: ").replace(" ", "").split(',')

    # final receipt for cost split between people
    costSplit = {}
    for person in people:
        costSplit[person] = 0

    print("-------------------")
    print("Start adding items:")
    print("-------------------")
    addmore = True
    while(addmore):
        item = getItem()

        for person in item[0]:
            costSplit[person] += item[1]
        
        addmore = moreItems()
    
    print("-------------------")
    tax = float(input("How much is tax?: "))
    tax /= len(people)

    for person in costSplit:
        costSplit[person] += tax 

    print(costSplit)

if __name__ == "__main__":
    main()


