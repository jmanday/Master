CXX=g++

# INCLUDE LIBS FOR OPENCV
OPENCV = `pkg-config opencv --cflags --libs`
LIBS = $(OPENCV)

# INCLUDE BASE DIRECTORY AND BOOST DIRECTORY FOR HEADERS
LDFLAGS = -I/usr/local/Cellar/boost/1.64.0_1/include

# INCLUDE OPENCV DIRECTORY AND BOOST DIRECTORY FOR LIB FILES
LLIBFLAGS = -L/usr/local/Cellar/boost/1.64.0_1/lib -L/usr/local/opt/opencv/lib

# SPECIFIY LINK OPTIONS
LINKFLAGS = -lopencv_core -lopencv_highgui -lopencv_imgproc -lopencv_objdetect -lopencv_contrib -lboost_filesystem -lboost_system -lboost_regex -lopencv_photo

# FINAL FLAGS -- TO BE USED THROUGHOUT
FLAGS = $(LDFLAGS) $(LLIBFLAGS) $(LINKFLAGS)

CXXFLAGS=-g -Wall

ALLTARGETS=harris-laplace

harris-laplace: harris-laplace.cpp
	$(CXX) $(LIBS) $(FLAGS) -o harris-laplace $(CXXFLAGS) harris-laplace.cpp

all: ${ALLTARGETS}
clean:
	rm -f ${ALLTARGETS}
