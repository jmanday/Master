# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.6

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Applications/CLion.app/Contents/bin/cmake/bin/cmake

# The command to remove a file.
RM = /Applications/CLion.app/Contents/bin/cmake/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/jesusgarciamanday/Desktop/Master/IC/Practicas/Practica2/p2

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/jesusgarciamanday/Desktop/Master/IC/Practicas/Practica2/p2/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/p2.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/p2.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/p2.dir/flags.make

CMakeFiles/p2.dir/main.cpp.o: CMakeFiles/p2.dir/flags.make
CMakeFiles/p2.dir/main.cpp.o: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/jesusgarciamanday/Desktop/Master/IC/Practicas/Practica2/p2/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/p2.dir/main.cpp.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/p2.dir/main.cpp.o -c /Users/jesusgarciamanday/Desktop/Master/IC/Practicas/Practica2/p2/main.cpp

CMakeFiles/p2.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/p2.dir/main.cpp.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/jesusgarciamanday/Desktop/Master/IC/Practicas/Practica2/p2/main.cpp > CMakeFiles/p2.dir/main.cpp.i

CMakeFiles/p2.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/p2.dir/main.cpp.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/jesusgarciamanday/Desktop/Master/IC/Practicas/Practica2/p2/main.cpp -o CMakeFiles/p2.dir/main.cpp.s

CMakeFiles/p2.dir/main.cpp.o.requires:

.PHONY : CMakeFiles/p2.dir/main.cpp.o.requires

CMakeFiles/p2.dir/main.cpp.o.provides: CMakeFiles/p2.dir/main.cpp.o.requires
	$(MAKE) -f CMakeFiles/p2.dir/build.make CMakeFiles/p2.dir/main.cpp.o.provides.build
.PHONY : CMakeFiles/p2.dir/main.cpp.o.provides

CMakeFiles/p2.dir/main.cpp.o.provides.build: CMakeFiles/p2.dir/main.cpp.o


CMakeFiles/p2.dir/Datas.cpp.o: CMakeFiles/p2.dir/flags.make
CMakeFiles/p2.dir/Datas.cpp.o: ../Datas.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/jesusgarciamanday/Desktop/Master/IC/Practicas/Practica2/p2/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/p2.dir/Datas.cpp.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/p2.dir/Datas.cpp.o -c /Users/jesusgarciamanday/Desktop/Master/IC/Practicas/Practica2/p2/Datas.cpp

CMakeFiles/p2.dir/Datas.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/p2.dir/Datas.cpp.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/jesusgarciamanday/Desktop/Master/IC/Practicas/Practica2/p2/Datas.cpp > CMakeFiles/p2.dir/Datas.cpp.i

CMakeFiles/p2.dir/Datas.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/p2.dir/Datas.cpp.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/jesusgarciamanday/Desktop/Master/IC/Practicas/Practica2/p2/Datas.cpp -o CMakeFiles/p2.dir/Datas.cpp.s

CMakeFiles/p2.dir/Datas.cpp.o.requires:

.PHONY : CMakeFiles/p2.dir/Datas.cpp.o.requires

CMakeFiles/p2.dir/Datas.cpp.o.provides: CMakeFiles/p2.dir/Datas.cpp.o.requires
	$(MAKE) -f CMakeFiles/p2.dir/build.make CMakeFiles/p2.dir/Datas.cpp.o.provides.build
.PHONY : CMakeFiles/p2.dir/Datas.cpp.o.provides

CMakeFiles/p2.dir/Datas.cpp.o.provides.build: CMakeFiles/p2.dir/Datas.cpp.o


CMakeFiles/p2.dir/Individuo.cpp.o: CMakeFiles/p2.dir/flags.make
CMakeFiles/p2.dir/Individuo.cpp.o: ../Individuo.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/jesusgarciamanday/Desktop/Master/IC/Practicas/Practica2/p2/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object CMakeFiles/p2.dir/Individuo.cpp.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/p2.dir/Individuo.cpp.o -c /Users/jesusgarciamanday/Desktop/Master/IC/Practicas/Practica2/p2/Individuo.cpp

CMakeFiles/p2.dir/Individuo.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/p2.dir/Individuo.cpp.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/jesusgarciamanday/Desktop/Master/IC/Practicas/Practica2/p2/Individuo.cpp > CMakeFiles/p2.dir/Individuo.cpp.i

CMakeFiles/p2.dir/Individuo.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/p2.dir/Individuo.cpp.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/jesusgarciamanday/Desktop/Master/IC/Practicas/Practica2/p2/Individuo.cpp -o CMakeFiles/p2.dir/Individuo.cpp.s

CMakeFiles/p2.dir/Individuo.cpp.o.requires:

.PHONY : CMakeFiles/p2.dir/Individuo.cpp.o.requires

CMakeFiles/p2.dir/Individuo.cpp.o.provides: CMakeFiles/p2.dir/Individuo.cpp.o.requires
	$(MAKE) -f CMakeFiles/p2.dir/build.make CMakeFiles/p2.dir/Individuo.cpp.o.provides.build
.PHONY : CMakeFiles/p2.dir/Individuo.cpp.o.provides

CMakeFiles/p2.dir/Individuo.cpp.o.provides.build: CMakeFiles/p2.dir/Individuo.cpp.o


# Object files for target p2
p2_OBJECTS = \
"CMakeFiles/p2.dir/main.cpp.o" \
"CMakeFiles/p2.dir/Datas.cpp.o" \
"CMakeFiles/p2.dir/Individuo.cpp.o"

# External object files for target p2
p2_EXTERNAL_OBJECTS =

p2: CMakeFiles/p2.dir/main.cpp.o
p2: CMakeFiles/p2.dir/Datas.cpp.o
p2: CMakeFiles/p2.dir/Individuo.cpp.o
p2: CMakeFiles/p2.dir/build.make
p2: CMakeFiles/p2.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/jesusgarciamanday/Desktop/Master/IC/Practicas/Practica2/p2/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking CXX executable p2"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/p2.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/p2.dir/build: p2

.PHONY : CMakeFiles/p2.dir/build

CMakeFiles/p2.dir/requires: CMakeFiles/p2.dir/main.cpp.o.requires
CMakeFiles/p2.dir/requires: CMakeFiles/p2.dir/Datas.cpp.o.requires
CMakeFiles/p2.dir/requires: CMakeFiles/p2.dir/Individuo.cpp.o.requires

.PHONY : CMakeFiles/p2.dir/requires

CMakeFiles/p2.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/p2.dir/cmake_clean.cmake
.PHONY : CMakeFiles/p2.dir/clean

CMakeFiles/p2.dir/depend:
	cd /Users/jesusgarciamanday/Desktop/Master/IC/Practicas/Practica2/p2/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/jesusgarciamanday/Desktop/Master/IC/Practicas/Practica2/p2 /Users/jesusgarciamanday/Desktop/Master/IC/Practicas/Practica2/p2 /Users/jesusgarciamanday/Desktop/Master/IC/Practicas/Practica2/p2/cmake-build-debug /Users/jesusgarciamanday/Desktop/Master/IC/Practicas/Practica2/p2/cmake-build-debug /Users/jesusgarciamanday/Desktop/Master/IC/Practicas/Practica2/p2/cmake-build-debug/CMakeFiles/p2.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/p2.dir/depend

