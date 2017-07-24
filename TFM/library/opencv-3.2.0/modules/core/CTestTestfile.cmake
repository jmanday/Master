# CMake generated Testfile for 
# Source directory: /Users/jesusgarciamanday/Documents/Master/TFM/library/opencv-3.2.0/modules/core
# Build directory: /Users/jesusgarciamanday/Documents/Master/TFM/library/opencv-3.2.0/modules/core
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(opencv_test_core "/Users/jesusgarciamanday/Documents/Master/TFM/library/opencv-3.2.0/bin/opencv_test_core" "--gtest_output=xml:opencv_test_core.xml")
set_tests_properties(opencv_test_core PROPERTIES  LABELS "Main;opencv_core;Accuracy" WORKING_DIRECTORY "/Users/jesusgarciamanday/Documents/Master/TFM/library/opencv-3.2.0/test-reports/accuracy")
add_test(opencv_perf_core "/Users/jesusgarciamanday/Documents/Master/TFM/library/opencv-3.2.0/bin/opencv_perf_core" "--gtest_output=xml:opencv_perf_core.xml")
set_tests_properties(opencv_perf_core PROPERTIES  LABELS "Main;opencv_core;Performance" WORKING_DIRECTORY "/Users/jesusgarciamanday/Documents/Master/TFM/library/opencv-3.2.0/test-reports/performance")
add_test(opencv_sanity_core "/Users/jesusgarciamanday/Documents/Master/TFM/library/opencv-3.2.0/bin/opencv_perf_core" "--gtest_output=xml:opencv_perf_core.xml" "--perf_min_samples=1" "--perf_force_samples=1" "--perf_verify_sanity")
set_tests_properties(opencv_sanity_core PROPERTIES  LABELS "Main;opencv_core;Sanity" WORKING_DIRECTORY "/Users/jesusgarciamanday/Documents/Master/TFM/library/opencv-3.2.0/test-reports/sanity")
