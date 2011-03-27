# a simple makefile to demonstrate simplectest
# http://simplectest.sf.net/
# modified by lfzawacki
# this file is in the public domain :>

#choose your compiler
CC = g++

FLAGS = -Wno-write-strings#-Wall uncomment to get warnings

all: 
	@echo "Use \"make nameTest\" to compile"

#type make name-main to build the real program
%-main: main.cpp %.o
	@$(CC) -o $@ $^ $(FLAGS)

#compiles the unit file
%.o: %.cpp
	@$(CC) -c -o $@ $^ $(FLAGS)

#compiles the test executable and links it with the .o
%Test: %.o %Test.cpp
	@$(CC) -o $@ $^ $(FLAGS)

clean:
	-rm *.o *.exe

.PHONY: all clean
