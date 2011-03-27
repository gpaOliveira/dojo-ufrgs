# a simple makefile to demonstrate simplectest
# http://simplectest.sf.net/
# modified by lfzawacki
# this file is in the public domain :>

#choose your compiler
CC = g++

OBJ = romanos
OBJ_TESTS = $(OBJ:=Test)

FLAGS = -Wno-write-strings#-Wall uncomment to get warnings

#making fizzBuzzTest and consequently fizzBuzz.o
all: $(OBJ_TEST)

#type make main to build the real program
main: main.cpp $(OBJ:=.o)
	$(CC) -o $@ $^ $(FLAGS)

#compiles the unit file, in this case fizzBuzz.o
%.o: %.cpp
	$(CC) -c -o $@ $^ $(FLAGS)

#compiles the test executable and links it with the .o
#in this case its fizzBuzzTest linked with fizzBuzz.o
%Test: %.o %Test.cpp
	$(CC) -o $@ $^ $(FLAGS)

clean:
	-rm *.o *.exe

.PHONY: all clean
