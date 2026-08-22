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
	var igrid [][]int
	S_x, S_y := 0, 0

	row := 0
	for scanner.Scan() {
		line := scanner.Text()

		var temp []string
		var	itemp []int
		for i := 0; i < len(line); i++ {
			temp = append(temp, string(line[i]))
			if string(line[i]) == "S" {
				S_x = row
				S_y = i
			}
			itemp = append(itemp, -1)
		}
		row += 1

		grid = append(grid, temp)
		igrid = append(igrid, itemp)
	}

	recursive(grid, S_x + 1, S_y)
	result1 := len(complexSet)
	result2 := recursive2(grid, S_x + 1, S_y, igrid);

	fmt.Println("Day 07 Part 01 : ", result1)
	fmt.Println("Day 07 Part 02 : ", result2)
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

func recursive2(grid [][]string, x int, y int, igrid [][]int) int {
	if x == (len(grid) - 1) {
		return 1
	}

	if x < 0 || x >= len(grid) || y < 0 || y >= len(grid[0]) {
		return 0
	}

	if igrid[x][y] != -1 {
		return igrid[x][y]
	}

	if grid[x][y] == "^" {
		igrid[x][y] = (recursive2(grid, x+1, y-1, igrid) + recursive2(grid, x+1, y+1, igrid))
	} else {
		igrid[x][y] = (recursive2(grid, x+1, y, igrid))
	}
	return igrid[x][y]
}
