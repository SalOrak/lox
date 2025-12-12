# Variables
SRC_DIR := src
BUILD_DIR := build
DIST_DIR := dist
JAR_NAME := app.jar
MAIN_CLASS := com.jlox.Lox.Lox

# Find all Java source files
SOURCES := $(shell find $(SRC_DIR) -name "*.java")

# Default target
all: $(DIST_DIR)/$(JAR_NAME)

# Compile all .java files in one go
$(BUILD_DIR)/.compiled: $(SOURCES)
	@mkdir -p $(BUILD_DIR)
	javac -d $(BUILD_DIR) $(SOURCES)
	@touch $@

# Package into JAR - safer version
$(DIST_DIR)/$(JAR_NAME): $(BUILD_DIR)/.compiled
	@mkdir -p $(DIST_DIR)
	# Create manifest with Main-Class
	echo "Main-Class: $(MAIN_CLASS)" > manifest.txt
	echo "" >> manifest.txt

	cd $(BUILD_DIR) && jar cfm ../$(DIST_DIR)/$(JAR_NAME) ../manifest.txt .

	rm manifest.txt
	@echo "JAR created at $(DIST_DIR)/$(JAR_NAME)"

# Clean up
clean:
	rm -rf $(BUILD_DIR) $(DIST_DIR)

# Run
run: 
	java -jar dist/$(JAR_NAME)

.PHONY: all clean run
