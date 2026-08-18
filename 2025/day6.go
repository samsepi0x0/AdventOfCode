package main

import (
	"fmt"
	"os"
	"strings"
	"strconv"
	"bufio"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Enter Filename.")
		return
	}
	filename := os.Args[1]
	file, err := os.Open(filename)
	if err != nil {
		fmt.Println("Error loading the file")
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	var lines [][]int64
	var operations []string
	var grid [][]int
	
	for scanner.Scan() {
		line := scanner.Text()
		numbers := strings.Split(line, " ")

		if numbers[0] == "*" || numbers[0] == "+" {
			for i := 0; i < len(numbers); i++ {
				if numbers[i] == "+" || numbers[i] == "*" {
					operations = append(operations, numbers[i])
				}
			}
			continue
		}

		var row []int

		for i := 0; i < len(numbers); i++ {
			for j := 0; j < len(numbers[i]); j++ {
				row = append(row, int(numbers[i][j] - '0'))
			}
			row = append(row, 11)
		}

		grid = append(grid, row)

		var newline []int64
		for i := 0; i < len(numbers); i++ {
			if numbers[i] == "" {
				continue
			}
			number, _ := strconv.Atoi(numbers[i])
			number2 := 0
			numberCopy := number

			for ; numberCopy != 0; {
				r := numberCopy % 10
				numberCopy /= 10
				number2 = number2 * 10 + r
			}
			newline = append(newline, int64(number))
		}
		lines = append(lines, newline)
	}

	var result1 int64
	var result2 int64
	startCol := 0

	for i := 0; i < len(operations); i++ {
		temp, temp2 := int64(0), int64(0)
		if operations[i] == "*" {
			temp = int64(1)
			temp2 = int64(1)
		}
		// Part 1
		for j := 0; j < len(lines); j++ {
			if operations[i] == "+" {
				temp = temp + lines[j][i]
			} else {
				temp = temp * lines[j][i]
			}
		}
		result1 += temp

		// Part 2
		elevens := 0
		for ;; {
			value := int64(0)
			for k := 0; k < len(grid); k++ {
				if grid[k][startCol] == 11 {
					elevens++
					continue
				} else {
					value = value * 10 + int64(grid[k][startCol])
				}
			}

			startCol++
			if elevens == len(grid) {
				break
			}
			
			elevens = 0
			if operations[i] == "*" {
				temp2 = temp2 * value
			} else {
				temp2 = temp2 + value
			}
		}
		result2 += temp2
	}

	fmt.Println("Day 06 Part 01 :", result1)
	fmt.Println("Day 06 Part 02 :", result2)
}			}
			continue
		}

		var newline []int64
		for i := 0; i < len(numbers); i++ {
			if numbers[i] == "" {
				continue
			}
			number, _ := strconv.Atoi(numbers[i])
			number2 := 0
			numberCopy := number

			for ; numberCopy != 0; {
				r := numberCopy % 10
				numberCopy /= 10
				number2 = number2 * 10 + r
			}
			newline = append(newline, int64(number))
		}
		lines = append(lines, newline)
	}

	var result1 int64
	var result2 int64

	for i := 0; i < len(operations); i++ {
		temp := int64(0)
		if operations[i] == "*" {
			temp = int64(1)
		}
		for j := 0; j < len(lines); j++ {
			if operations[i] == "+" {
				temp = temp + lines[j][i]
			} else {
				temp = temp * lines[j][i]
			}
		}
		result1 += temp
	}



	fmt.Println("Day 06 Part 01 :", result1)
	fmt.Println("Day 06 Part 02 :", result2)
}
