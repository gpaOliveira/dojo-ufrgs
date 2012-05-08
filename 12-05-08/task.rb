class TaskScheduler

    def initialize()
        @tasks = []
    end

    def add_task(task)
        @tasks << task
    end

    def schedule()
        @tasks.sort!

        alloc = {}

        @tasks.each do |t|
            done = false
            cur = 1
            while not done
                if alloc[cur].nil?
                    alloc[cur] = []
                    alloc[cur] << t
                    done = true
                elsif not intersect(alloc[cur][-1], t)
                    alloc[cur] << t
                    done = true
                else 
                    cur += 1
                end
            end
        end

        alloc
    # if @tasks.size == 3
    #     { 1 => [@tasks[0],@tasks[2]], 2 => [@tasks[1]]}
    # else
    #     if @tasks.size > 1 && intersect(@tasks[0], @tasks[1])
    #             { 1 => [@tasks[0]], 2 => [@tasks[1]] }
    #     else
    #         { 1 => @tasks }
    #     end
    # end
end

    def intersect(task1,task2)
        if(task1[0] < task2[0])
            if (task1[1] > task2[0])
                true
            else
                false
            end
        else
            if (task2[1] > task2[0])
                true
            else
                false
            end
        end
    end

end
