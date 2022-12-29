CC = clang++
CFLAGS = -std=c++20 -Wall -Werror -Wextra -O0 -g -I./include
BUILD_DIR = build

# brew install catch2
CATCH_ROOT = /usr/local/Cellar/catch2/3.2.1

# TCLAP could be installed via: brew install tclap
# However, I installed from source to get 1.4.0:
# https://tclap.sourceforge.net
#
# tar xf tclap-1.4.0-rc1.tar.bz2
# cd tclap-1.4.0-rc1
# mkdir build
# cd build
# cmake ..
# cmake --build .
# cmake --install . [--prefix CMAKE_INSTALL_PREFIX]
TCLAP_ROOT = /Users/brianneradt/local

.DEFAULT_GOAL := all

#---------------------
# Production
#---------------------
$(BUILD_DIR)/occupant.o: src/occupant.cc include/occupant.h include/square.h
	mkdir -p $(BUILD_DIR)
	$(CC) -o $@ -c $< $(CFLAGS)

$(BUILD_DIR)/square.o: src/square.cc include/square.h include/occupant.h
	mkdir -p $(BUILD_DIR)
	$(CC) -o $@ -c $< $(CFLAGS)

$(BUILD_DIR)/valley.o: src/valley.cc include/valley.h include/square.h
	mkdir -p $(BUILD_DIR)
	$(CC) -o $@ -c $< $(CFLAGS)

$(BUILD_DIR)/main.o: src/main.cc include/valley.h include/square.h
	mkdir -p $(BUILD_DIR)
	$(CC) -o $@ -c $< $(CFLAGS) -I$(TCLAP_ROOT)/include

find_path: $(BUILD_DIR)/main.o $(BUILD_DIR)/valley.o $(BUILD_DIR)/square.o $(BUILD_DIR)/occupant.o
	$(CC) -o $@ $^

#---------------------
# Test
#---------------------
TEST_DIR = test
$(BUILD_DIR)/test_occupant.o: $(TEST_DIR)/test_occupant.cc include/occupant.h include/square.h
	mkdir -p $(BUILD_DIR)
	$(CC) -o $@ -c $< $(CFLAGS) -I$(CATCH_ROOT)/include -I.

$(BUILD_DIR)/test_square.o: $(TEST_DIR)/test_square.cc include/square.h
	mkdir -p $(BUILD_DIR)
	$(CC) -o $@ -c $< $(CFLAGS) -I$(CATCH_ROOT)/include -I.

$(BUILD_DIR)/test_valley.o: $(TEST_DIR)/test_valley.cc include/valley.h include/square.h
	mkdir -p $(BUILD_DIR)
	$(CC) -o $@ -c $< $(CFLAGS) -I$(CATCH_ROOT)/include -I.

run_unit_tests: $(BUILD_DIR)/test_valley.o $(BUILD_DIR)/valley.o $(BUILD_DIR)/test_square.o $(BUILD_DIR)/square.o $(BUILD_DIR)/test_occupant.o $(BUILD_DIR)/occupant.o
	$(CC) -o $@ $^ -I$(CATCH_ROOT)/include -L$(CATCH_ROOT)/lib -lCatch2Main -lCatch2

.PHONY: check
check: run_unit_tests find_path
	./$<
	bash ./test/run_system_tests

.PHONY: check_units
check_units: run_unit_tests
	./$<

.PHONY: all
all: find_path

.PHONY: clean
clean:
	rm -f $(BUILD_DIR)/*.o find_path run_unit_tests
	rm -fd $(BUILD_DIR)
