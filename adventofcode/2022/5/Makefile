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
$(BUILD_DIR)/argument_parser.o: src/argument_parser.cc include/argument_parser.h
	mkdir -p $(BUILD_DIR)
	$(CC) -o $@ -c $< $(CFLAGS) -I$(TCLAP_ROOT)/include

$(BUILD_DIR)/stack_file_parser.o: src/stack_file_parser.cc include/stack_file_parser.h
	mkdir -p $(BUILD_DIR)
	$(CC) -o $@ -c $< $(CFLAGS) -I$(TCLAP_ROOT)/include

$(BUILD_DIR)/supply_line_parser.o: src/supply_line_parser.cc include/supply_line_parser.h
	mkdir -p $(BUILD_DIR)
	$(CC) -o $@ -c $< $(CFLAGS)

$(BUILD_DIR)/supply_stacks.o: src/supply_stacks.cc include/supply_stacks.h
	mkdir -p $(BUILD_DIR)
	$(CC) -o $@ -c $< $(CFLAGS)

$(BUILD_DIR)/main.o: src/main.cc include/supply_stacks.h
	mkdir -p $(BUILD_DIR)
	$(CC) -o $@ -c $< $(CFLAGS)

move_stacks: $(BUILD_DIR)/main.o $(BUILD_DIR)/argument_parser.o $(BUILD_DIR)/stack_file_parser.o $(BUILD_DIR)/supply_stacks.o $(BUILD_DIR)/supply_line_parser.o
	$(CC) -o $@ $^

#---------------------
# Test
#---------------------
TEST_DIR = test
$(BUILD_DIR)/test_supply_stacks.o: $(TEST_DIR)/test_supply_stacks.cc include/supply_stacks.h
	mkdir -p $(BUILD_DIR)
	$(CC) -o $@ -c $< $(CFLAGS) -I$(CATCH_ROOT)/include -I.

$(BUILD_DIR)/test_supply_line_parser.o: $(TEST_DIR)/test_supply_line_parser.cc include/supply_line_parser.h
	mkdir -p $(BUILD_DIR)
	$(CC) -o $@ -c $< $(CFLAGS) -I$(CATCH_ROOT)/include -I.

run_unit_tests: $(BUILD_DIR)/test_supply_stacks.o $(BUILD_DIR)/test_supply_line_parser.o $(BUILD_DIR)/supply_stacks.o $(BUILD_DIR)/supply_line_parser.o
	$(CC) -o $@ $^ -I$(CATCH_ROOT)/include -L$(CATCH_ROOT)/lib -lCatch2Main -lCatch2

.PHONY: check
check: run_unit_tests move_stacks
	./$<
	bash ./test/run_system_tests


.PHONY: all
all: move_stacks

.PHONY: clean
clean:
	rm -f $(BUILD_DIR)/*.o move_stacks run_unit_tests
	rm -fd $(BUILD_DIR)
