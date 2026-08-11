package main

import (
	"fmt"
	"bufio"
	"os"
)

func main() {
	if len(os.Args) < 2 {	
		fmt.Println("Enter Filename.")
		return
	}

	filename := os.Args[1]
	file, err := os.Open(filename)
	if err != nil {	
		fmt.Println("Error opening file")
		return
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	var grid [][]rune
	for scanner.Scan() {
		line := scanner.Text()
		row := []rune(line)
		grid = append(grid, row)
	}

	rows := len(grid)
	cols := len(grid[0])

	result1 := 0

	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if grid[i][j] == '@' && check(grid, i, j) {
				result1++
			}
		}
	}
	
	result2 := 0	
	flag := true
	for ; flag == true; {
		flag = false
		for i:= 0; i < rows; i++ {
			for j := 0; j < cols; j++ {
				if grid[i][j] == '@' && check(grid, i,j) {
					result2++
					grid[i][j] = '.'
					flag = true
				}
			}
		}
	}


	fmt.Println("Day 04 Part 01 :", result1)
	fmt.Println("Day 04 Part 02 :", result2)
}


func check(grid [][]rune, i int, j int) bool {
	directions := [8][2]int{
		{-1,-1},
		{-1, 0},
		{-1, 1},
		{0, -1},
		{0, 1},
		{1, -1},
		{1, 0},
		{1, 1}, 
	}

	count := 0
	for _, direction := range directions {
		ni := i + direction[0]
		nj := j + direction[1]

		if ni < 0 || ni >= len(grid) || nj < 0 || nj >= len(grid[0]) {
			continue
		}

		if grid[ni][nj] == '@' {
			count++
		}
	}
	return count < 4
}
