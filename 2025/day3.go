package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Enter Filename.")
		return 
	}

	filename := os.Args[1]
	file, err := os.Open(filename)
	if err != nil {
		fmt.Println("Error Loading the file.")
		return
	}
	scanner := bufio.NewScanner(file)
	result := 0
	var result2 int64 = 0
	for scanner.Scan() {
		bank := scanner.Text()
		//bruteforce
		maxBankDigits := 0
		for i := 0; i < len(bank); i++ {
			for j := i + 1; j < len(bank); j++ {
				digit, _ := strconv.Atoi(bank[i:i+1] + bank[j:j+1])
				if digit > maxBankDigits {
					maxBankDigits = digit
				}
			}
		}
		result += maxBankDigits
		result2 += part2(bank)
	}
	fmt.Println("Day 03 Part 01:", result)
	fmt.Println("Day 03 Part 02:", result2)
}

func part2(bank string) int64 {
	rows, cols := len(bank), 13

	matrix := make([][]int64, rows)

	for i := range matrix {
		matrix[i] = make([]int64, cols)
		for j := range matrix[i] {
			matrix[i][j] = -2
		}
	}

	return backtrack(bank, 0, 0, matrix);
}

func backtrack(bank string, index int, count int, dp [][]int64) int64 {
	if count == 12 {
		return 0
	}
	if index == len(bank) {
		return -1
	}
	if dp[index][count] != -2 {
		return dp[index][count]
	}

	notTaken := backtrack(bank, index + 1, count, dp)
	var taken int64 = -1
	res := backtrack(bank, index + 1, count + 1, dp)

	if res != -1 {
		digit := int64(bank[index] - '0')

		pow := int64(1)
		for p := 0; p < 11-count; p++ {
			pow *= 10
		}
		taken = (digit * pow) + res
	}

	maxval := notTaken
	if taken > maxval {
		maxval = taken
	}
	dp[index][count] = maxval
	return maxval
}
