TARGET=pushm
SRC=src
SRC_FILES=$(wildcard $(SRC)/*.cpp)
OBJ_FILES=$(patsubst $(SRC)/%.cpp,%.o,$(SRC_FILES))

CXX=g++
# OpenBSD (uncomment)
#CXX=eg++

CXXFLAGS=-std=c++17 -O3 -Wall -Wextra -Wpedantic
CXXLIBS=-lstdc++fs

$(TARGET): $(OBJ_FILES)
	$(CXX) $(CXXFLAGS) $(OBJ_FILES) $(CXXLIBS) -o $(TARGET)

%.o: $(SRC)/%.cpp
	$(CXX) $(CXXFLAGS) -c -o $@ $<

clean:
	rm -f *.o $(TARGET)

install: $(TARGET)
	cp $(TARGET) /usr/local/bin

uninstall:
	rm -f /usr/local/bin/$(TARGET)
