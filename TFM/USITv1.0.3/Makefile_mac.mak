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

ALLTARGETS=caht wahet gfcf lg hd hdverify qsw ko koc cb cbc cr dct dctc maskcmp iffp

caht: caht.cpp
	$(CXX) $(LIBS) $(FLAGS) -o caht $(CXXFLAGS) caht.cpp

wahet: wahet.cpp
	$(CXX) $(LIBS) $(FLAGS) -o wahet $(CXXFLAGS) wahet.cpp

gfcf: gfcf.cpp
	$(CXX) $(LIBS) $(FLAGS) -o gfcf $(CXXFLAGS) gfcf.cpp

lg: lg.cpp
	$(CXX) $(LIBS) $(FLAGS) -o lg $(CXXFLAGS) lg.cpp

hd: hd.cpp
	$(CXX) $(LIBS) $(FLAGS) -o hd $(CXXFLAGS) hd.cpp

hdverify: hdverify.cpp
	$(CXX) $(LIBS) $(FLAGS) -o hdverify $(CXXFLAGS) hdverify.cpp

qsw: qsw.cpp
	$(CXX) $(LIBS) $(FLAGS) -o qsw $(CXXFLAGS) qsw.cpp

ko: ko.cpp
	$(CXX) $(LIBS) $(FLAGS) -o ko $(CXXFLAGS) ko.cpp

koc: koc.cpp
	$(CXX) $(LIBS) $(FLAGS) -o koc $(CXXFLAGS) koc.cpp

cr: cr.cpp
	$(CXX) $(LIBS) $(FLAGS) -o cr $(CXXFLAGS) cr.cpp

cb: cb.cpp
	$(CXX) $(LIBS) $(FLAGS) -o cb $(CXXFLAGS) cb.cpp

cbc: cbc.cpp
	$(CXX) $(LIBS) $(FLAGS) -o cbc $(CXXFLAGS) cbc.cpp

dct: dct.cpp
	$(CXX) $(LIBS) $(FLAGS) -o dct $(CXXFLAGS) dct.cpp

dctc: dctc.cpp
	$(CXX) $(LIBS) $(FLAGS) -o dctc $(CXXFLAGS) dctc.cpp

maskcmp: maskcmp.cpp
	$(CXX) $(LIBS) $(FLAGS) -o maskcmp $(CXXFLAGS) maskcmp.cpp

iffp: iffp.cpp
	$(CXX) $(LIBS) $(FLAGS) -o iffp $(CXXFLAGS) iffp.cpp

all: ${ALLTARGETS}
clean:
	rm ${ALLTARGETS}
	
