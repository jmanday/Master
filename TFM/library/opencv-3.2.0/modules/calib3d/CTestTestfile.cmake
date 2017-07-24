# CMake generated Testfile for 
# Source directory: /Users/jesusgarciamanday/Documents/Master/TFM/library/opencv-3.2.0/modules/calib3d
# Build directory: /Users/jesusgarciamanday/Documents/Master/TFM/library/opencv-3.2.0/modules/calib3d
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(opencv_test_calib3d "/Users/jesusgarciamanday/Documents/Master/TFM/library/opencv-3.2.0/bin/opencv_test_calib3d" "--gtest_output=xml:opencv_test_calib3d.xml")
set_tests_properties(opencv_test_calib3d PROPERTIES  LABELS "Main;opencv_calib3d;Accuracy" WORKING_DIRECTORY "/Users/jesusgarciamanday/Documents/Master/TFM/library/opencv-3.2.0/test-reports/accuracy")
add_test(opencv_perf_calib3d "/Users/jesusgarciamanday/Documents/Master/TFM/library/opencv-3.2.0/bin/opencv_perf_calib3d" "--gtest_output=xml:opencv_perf_calib3d.xml")
set_tests_properties(opencv_perf_calib3d PROPERTIES  LABELS "Main;opencv_calib3d;Performance" WORKING_DIRECTORY "/Users/jesusgarciamanday/Documents/Master/TFM/library/opencv-3.2.0/test-reports/performance")
add_test(opencv_sanity_calib3d "/Users/jesusgarciamanday/Documents/Master/TFM/library/opencv-3.2.0/bin/opencv_perf_calib3d" "--gtest_output=xml:opencv_perf_calib3d.xml" "--perf_min_samples=1" "--perf_force_samples=1" "--perf_verify_sanity")
set_tests_properties(opencv_sanity_calib3d PROPERTIES  LABELS "Main;opencv_calib3d;Sanity" WORKING_DIRECTORY "/Users/jesusgarciamanday/Documents/Master/TFM/library/opencv-3.2.0/test-reports/sanity")
