# CMake generated Testfile for 
# Source directory: /Users/jesusgarciamanday/Documents/Master/TFM/library/opencv-3.2.0/modules/ml
# Build directory: /Users/jesusgarciamanday/Documents/Master/TFM/library/opencv-3.2.0/modules/ml
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(opencv_test_ml "/Users/jesusgarciamanday/Documents/Master/TFM/library/opencv-3.2.0/bin/opencv_test_ml" "--gtest_output=xml:opencv_test_ml.xml")
set_tests_properties(opencv_test_ml PROPERTIES  LABELS "Main;opencv_ml;Accuracy" WORKING_DIRECTORY "/Users/jesusgarciamanday/Documents/Master/TFM/library/opencv-3.2.0/test-reports/accuracy")
