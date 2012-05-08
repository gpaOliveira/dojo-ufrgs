require 'task'

describe TaskScheduler, "Scheduler of Tasks" do

	it "should schedule one task" do
		scheduler = TaskScheduler.new
		scheduler.add_task [0, 2]
		scheduler.schedule.should == { 1 => [ [0,2] ] }
	end

	it "should schedule two tasks" do
		scheduler = TaskScheduler.new
		[[0, 2], [2, 4]].each { |task|
			scheduler.add_task task
		}
		scheduler.schedule.should == { 1 => [ [0,2] , [2,4] ] }
	end

	it "should schedule two rooms with one task each" do
		scheduler = TaskScheduler.new
		[[0, 2], [1, 3]].each { |task|
			scheduler.add_task task
		}
		scheduler.schedule.should == { 1 => [[0,2]], 2 => [[1,3]]}
	end

	it "should schedule two rooms with one task each2" do
		scheduler = TaskScheduler.new
		[[1, 3], [0, 2]].each { |task|
			scheduler.add_task task
		}
		scheduler.schedule.should == { 1 => [[0,2]], 2 => [[1,3]]}
	end

	it "should intersect" do
		scheduler = TaskScheduler.new
		scheduler.intersect([0, 1], [0, 1]).should == true
		scheduler.intersect([0, 4], [2, 3]).should == true
		scheduler.intersect([0, 3], [2, 4]).should == true
		scheduler.intersect([2, 4], [0, 3]).should == true
		scheduler.intersect([0, 1], [2, 3]).should == false
		scheduler.intersect([0, 1], [1, 2]).should == false
		scheduler.intersect([2, 3], [0, 4]).should == true
		scheduler.intersect([0, 2], [2, 4]).should == false
	end

	it "should schedule 3 tasks, but only 2 works" do
		scheduler = TaskScheduler.new
		[[1, 3], [0, 2], [3, 4]].each { |task|
			scheduler.add_task task
		}
		scheduler.schedule.should == { 1 => [[0,2],[3,4]], 2 => [[1,3]]}
	end


end

