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
	var linesRev [][]int64
	var operations []string
	
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

		var newline []int64
		var newlineRev []int64
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
			newlineRev = append(newlineRev, int64(number2))
		}
		lines = append(lines, newline)
		linesRev = append(linesRev, newlineRev)
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

	for i := 0; i < len(operations); i++ {
		temp := int64(0)
		if operations[i] == "*" {
			temp = int64(1)
		}

		flag := false
		for {
			flag = false
			num := int64(0)
			for j := 0; j < len(linesRev); j++ {
				num = num * 10 + (linesRev[j][i] % 10)
				linesRev[j][i] /= 10
				if linesRev[j][i] > 0 {
					flag = true
				}
			}

			if !flag {
				break
			}
			fmt.Print(num, "\t")
			if operations[i] == "*" {
				temp = temp * num
			} else {
				temp = temp + num
			}
		}
		fmt.Println()
		result2 += temp
		
	}

	fmt.Println("Day 06 Part 01 :", result1)
	fmt.Println("Day 06 Part 02 :", result2)
}