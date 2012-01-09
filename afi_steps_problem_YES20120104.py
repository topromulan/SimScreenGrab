

sol2=[[1,1], [2]]

def solution(total_steps):
    assert total_steps >= 2

    current_step = 2
    working_set = sol2

    while current_step < total_steps:
        old_set = working_set
        working_set = []

        current_step += 1

        for path in old_set:
            working_set += [[1] + path]
            if path[0] == 1:
                working_set += [[2] + path[1:]]


    print "Solution for %d steps" % total_steps
    print working_set
    print len(working_set), "answers"
    
solution(2)
solution(3)
solution(4)
solution(5)
#solution(6)
#solution(7)
#solution(8)
#solution(9)
#solution(10)
    



