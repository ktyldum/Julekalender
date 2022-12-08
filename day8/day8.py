
import numpy as np

useTestData = False

####################################
# Reading data

file = "test.txt" if useTestData else "input.txt"

forest=np.genfromtxt(file,dtype=int,delimiter=1)

print(forest)

def visible(a):
    result = [1]*len(a)
    highest = -1
    for x in range(len(a)):
        if a[x]>highest:
            highest=a[x]
            result[x] = 1
        else:
            result[x] = 0

    return result

def lookout(a):
    result = list(range(len(a)))[::-1]
    for x in range(len(result)):
        for i in range(1,result[x]):
            if a[x+i]>=a[x]:
                result[x]=i
                break

    return result

north=np.apply_along_axis(visible,0,forest)
print("From north")
print(north)

west=np.apply_along_axis(visible,1,forest)
print("From west")
print(west)

south=np.flipud(np.apply_along_axis(visible,0,np.flipud(forest)))
print("From south")
print(south)

east=np.fliplr(np.apply_along_axis(visible,1,np.fliplr(forest)))
print("From east")
print(east)

result = north + south + east + west
print("Total")
print(result)

visible = result >= 1
print(visible)

answer = np.count_nonzero(visible)
print("\n\nAnswer part1  {}\n\n".format(answer))


lookoutToSouth=(np.apply_along_axis(lookout,0,forest))
print("Look to South")
print(lookoutToSouth)

lookoutToEast=np.apply_along_axis(lookout,1,forest)
print("Look to East")
print(lookoutToEast)

lookoutToNorth=np.flipud(np.apply_along_axis(lookout,0,np.flipud(forest)))
print("Look to North")
print(lookoutToNorth)

lookoutToWest=np.fliplr(np.apply_along_axis(lookout,1,np.fliplr(forest)))
print("Look to West")
print(lookoutToWest)

scenic=lookoutToEast*lookoutToWest*lookoutToSouth*lookoutToNorth
print("Scenic value")
print(scenic)

answer2=np.amax(scenic)
print("\n\nAnswer part2:  {}\n\n".format(answer2))