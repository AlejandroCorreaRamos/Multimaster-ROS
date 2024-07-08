# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

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
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/user/catkin_ws/src/geographiclib

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/user/catkin_ws/src/geographiclib/build

# Include any dependencies generated for this target.
include examples/CMakeFiles/example-MGRS.dir/depend.make

# Include the progress variables for this target.
include examples/CMakeFiles/example-MGRS.dir/progress.make

# Include the compile flags for this target's objects.
include examples/CMakeFiles/example-MGRS.dir/flags.make

examples/CMakeFiles/example-MGRS.dir/example-MGRS.cpp.o: examples/CMakeFiles/example-MGRS.dir/flags.make
examples/CMakeFiles/example-MGRS.dir/example-MGRS.cpp.o: ../examples/example-MGRS.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/user/catkin_ws/src/geographiclib/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object examples/CMakeFiles/example-MGRS.dir/example-MGRS.cpp.o"
	cd /home/user/catkin_ws/src/geographiclib/build/examples && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/example-MGRS.dir/example-MGRS.cpp.o -c /home/user/catkin_ws/src/geographiclib/examples/example-MGRS.cpp

examples/CMakeFiles/example-MGRS.dir/example-MGRS.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/example-MGRS.dir/example-MGRS.cpp.i"
	cd /home/user/catkin_ws/src/geographiclib/build/examples && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/user/catkin_ws/src/geographiclib/examples/example-MGRS.cpp > CMakeFiles/example-MGRS.dir/example-MGRS.cpp.i

examples/CMakeFiles/example-MGRS.dir/example-MGRS.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/example-MGRS.dir/example-MGRS.cpp.s"
	cd /home/user/catkin_ws/src/geographiclib/build/examples && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/user/catkin_ws/src/geographiclib/examples/example-MGRS.cpp -o CMakeFiles/example-MGRS.dir/example-MGRS.cpp.s

examples/CMakeFiles/example-MGRS.dir/example-MGRS.cpp.o.requires:

.PHONY : examples/CMakeFiles/example-MGRS.dir/example-MGRS.cpp.o.requires

examples/CMakeFiles/example-MGRS.dir/example-MGRS.cpp.o.provides: examples/CMakeFiles/example-MGRS.dir/example-MGRS.cpp.o.requires
	$(MAKE) -f examples/CMakeFiles/example-MGRS.dir/build.make examples/CMakeFiles/example-MGRS.dir/example-MGRS.cpp.o.provides.build
.PHONY : examples/CMakeFiles/example-MGRS.dir/example-MGRS.cpp.o.provides

examples/CMakeFiles/example-MGRS.dir/example-MGRS.cpp.o.provides.build: examples/CMakeFiles/example-MGRS.dir/example-MGRS.cpp.o


# Object files for target example-MGRS
example__MGRS_OBJECTS = \
"CMakeFiles/example-MGRS.dir/example-MGRS.cpp.o"

# External object files for target example-MGRS
example__MGRS_EXTERNAL_OBJECTS =

examples/example-MGRS: examples/CMakeFiles/example-MGRS.dir/example-MGRS.cpp.o
examples/example-MGRS: examples/CMakeFiles/example-MGRS.dir/build.make
examples/example-MGRS: src/libGeographic.so.19.2.0
examples/example-MGRS: examples/CMakeFiles/example-MGRS.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/user/catkin_ws/src/geographiclib/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable example-MGRS"
	cd /home/user/catkin_ws/src/geographiclib/build/examples && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/example-MGRS.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
examples/CMakeFiles/example-MGRS.dir/build: examples/example-MGRS

.PHONY : examples/CMakeFiles/example-MGRS.dir/build

examples/CMakeFiles/example-MGRS.dir/requires: examples/CMakeFiles/example-MGRS.dir/example-MGRS.cpp.o.requires

.PHONY : examples/CMakeFiles/example-MGRS.dir/requires

examples/CMakeFiles/example-MGRS.dir/clean:
	cd /home/user/catkin_ws/src/geographiclib/build/examples && $(CMAKE_COMMAND) -P CMakeFiles/example-MGRS.dir/cmake_clean.cmake
.PHONY : examples/CMakeFiles/example-MGRS.dir/clean

examples/CMakeFiles/example-MGRS.dir/depend:
	cd /home/user/catkin_ws/src/geographiclib/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/user/catkin_ws/src/geographiclib /home/user/catkin_ws/src/geographiclib/examples /home/user/catkin_ws/src/geographiclib/build /home/user/catkin_ws/src/geographiclib/build/examples /home/user/catkin_ws/src/geographiclib/build/examples/CMakeFiles/example-MGRS.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : examples/CMakeFiles/example-MGRS.dir/depend

