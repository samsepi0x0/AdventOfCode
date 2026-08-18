package main

import (
	"fmt"
	"os"
	"bufio"
)

var complexSet = make(map[complex64]struct{})

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Enter Filename.")
		return
	}
	filename := os.Args[1]
	file, err := os.Open(filename)
	if err != nil {
		fmt.Println("Error loading the file.")
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var grid [][]string
	S_x, S_y := 0, 0

	row := 0
	for scanner.Scan() {
		line := scanner.Text()

		var temp []string
		for i := 0; i < len(line); i++ {
			temp = append(temp, string(line[i]))
			if string(line[i]) == "S" {
				S_x = row
				S_y = i
			}
		}
		row += 1

		grid = append(grid, temp)
	}
	recursive(grid, S_x + 1, S_y)
	result1 := len(complexSet)

	fmt.Println("Day 07 Part 01 : ", result1)
}

func recursive(grid [][]string, x int, y int) {
	if x < 0 || x >= len(grid) || y < 0 || y >= len(grid[0]) {
		return
	}
	if grid[x][y] == "|" {
		return
	}
	if grid[x][y] == "^" {
		c64 := complex(float32(x), float32(y))
		complexSet[c64] = struct{}{}

		recursive(grid, x, y - 1)
		recursive(grid, x, y + 1)

		if y - 1 >= 0 {
			grid[x][y-1] = "|"
		}
		if (y + 1) < len(grid[0]) {
			grid[x][y+1] = "|"
		}

	} else {
		grid[x][y] = "|"
		recursive(grid, x+1, y)
	}
}
