# Makefile for Week 2 project

# Target: run the data preparation script
prep:
	./prep_data.sh

# Target: clean up generated files
clean:
	rm -rf data

# Target: run both clean and prep
all: clean prep

# Target: show help
help:
	@echo "Available targets:"
	@echo "  make prep   - Run prep_data.sh to prepare data"
	@echo "  make clean  - Remove the data folder"
	@echo "  make all    - Clean and then prep"
	@echo "  make help   - Show this help message"

