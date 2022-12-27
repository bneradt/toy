CC = clang++
CFLAGS = -std=c++20 -Wall -Werror -Wextra -O3 -g -I./include
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
$(BUILD_DIR)/snafu.o: src/snafu.cc include/snafu.h include/snafu_internals.h
	mkdir -p $(BUILD_DIR)
	$(CC) -o $@ -c $< $(CFLAGS)

$(BUILD_DIR)/snafu_internals.o: src/snafu_internals.cc include/snafu_internals.h
	mkdir -p $(BUILD_DIR)
	$(CC) -o $@ -c $< $(CFLAGS)

$(BUILD_DIR)/main.o: src/main.cc include/snafu.h include/snafu_internals.h
	mkdir -p $(BUILD_DIR)
	$(CC) -o $@ -c $< $(CFLAGS)

compute_snafu: $(BUILD_DIR)/main.o $(BUILD_DIR)/snafu.o $(BUILD_DIR)/snafu_internals.o
	$(CC) -o $@ $^

#---------------------
# Test
#---------------------
TEST_DIR = test
$(BUILD_DIR)/test_snafu.o: $(TEST_DIR)/test_snafu.cc include/snafu.h include/snafu_internals.h
	mkdir -p $(BUILD_DIR)
	$(CC) -o $@ -c $< $(CFLAGS) -I$(CATCH_ROOT)/include -I.

$(BUILD_DIR)/test_snafu_internals.o: $(TEST_DIR)/test_snafu_internals.cc include/snafu_internals.h
	mkdir -p $(BUILD_DIR)
	$(CC) -o $@ -c $< $(CFLAGS) -I$(CATCH_ROOT)/include -I.

run_unit_tests: $(BUILD_DIR)/test_snafu.o $(BUILD_DIR)/snafu.o $(BUILD_DIR)/test_snafu_internals.o $(BUILD_DIR)/snafu_internals.o
	$(CC) -o $@ $^ -I$(CATCH_ROOT)/include -L$(CATCH_ROOT)/lib -lCatch2Main -lCatch2

.PHONY: check
check: run_unit_tests compute_snafu
	./$<
	bash ./test/run_system_tests


.PHONY: all
all: compute_snafu

.PHONY: clean
clean:
	rm -f $(BUILD_DIR)/*.o compute_snafu run_unit_tests
	rm -fd $(BUILD_DIR)
