def next_peg(position, num_of_pegs = 3):
    return (position + 1) % num_of_pegs


def non_min_position(pegs, min_position):
    position1 = next_peg(min_position) if pegs[

        next_peg(min_position)] else None
    position2 = next_peg(next_peg(min_position)) if pegs[
        next_peg(next_peg(min_position))] else None

    if (position1 != None) and (position2 != None):
        if pegs[position1][-1] > pegs[position2][-1]:
            return position2
        else:
            return position1

    elif position1 is not None:
        return position1

    else:
        return position2


def move_disk(pegs, start, target):
	pegs[target].append(pegs[start].pop())


def iteration_solution(pegs, min_position,num_of_pegs):
    while True:
        print(pegs)
        move_disk(pegs, min_position, next_peg(min_position,num_of_pegs))
        min_position = next_peg(min_position,num_of_pegs)
        print(pegs)
        try:
                middle = non_min_position(pegs, min_position)
                move_disk(pegs, middle, num_of_pegs - middle - min_position)
        except:
        	break

if __name__ == '__main__':
    # peg is a stack
    pegs = [[],[6, 5, 4, 3, 2, 1], []]
    for position, peg in enumerate(pegs):
    	if peg:
    		min_position = position

    iteration_solution(pegs, min_position, len(pegs))
