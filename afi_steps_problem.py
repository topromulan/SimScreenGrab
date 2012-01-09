

sol3=[[1,1,1], [2,1], [1,2], [3]]

def solution(total_steps):
    assert total_steps >= 3

    current_step = 3
    working_set = sol3

    while current_step < total_steps:
        old_set = working_set
        working_set = []

        current_step += 1

        for path in old_set:
            working_set += [[1] + path]
            if path[0] == 1:
                working_set += [[2] + path[1:]]
            elif path[0] == 2:
                working_set += [[3] + path[1:]]


    print "Solution for %d steps" % total_steps
    print working_set
    print len(working_set), "answers"
    
solution(3)
solution(4)
solution(5)
solution(6)
solution(7)
solution(8)
#solution(9)
#solution(10)
    



