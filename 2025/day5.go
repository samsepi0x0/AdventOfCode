package main

import (
	"fmt"
	"os"
	"bufio"
	"strings"
	"strconv"
	"slices"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Enter Filename.")
		return
	}
	filename := os.Args[1]
	file, err := os.Open(filename)
	if err != nil {
		fmt.Println("Unable to load filename")
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var intervals [][]int
	
	for scanner.Scan() {
		line := scanner.Text()
		if len(line) == 0 {
			break
		}
		ranges := strings.Split(line, "-")
		start, _ := strconv.Atoi(ranges[0])
		end, _ := strconv.Atoi(ranges[1])
		
		interval := []int{start, end}
		intervals = append(intervals, interval)
	}

	var ingredients []int
	for scanner.Scan() {
		line := scanner.Text()
		ingredient, _ := strconv.Atoi(line)
		ingredients = append(ingredients, ingredient)
	}

	slices.SortFunc(intervals, func(rowA, rowB []int) int {
		if rowA[0] < rowB[0] { return -1 }
		if rowA[0] > rowB[0] { return  1 }
		return 0
	})

	var merged_intervals [][]int
	start, end := intervals[0][0], intervals[0][1]
	
	for i := 1; i < len(intervals); i++ {
		start2, end2 := intervals[i][0], intervals[i][1]
		if end >= start2 {
			end = max(end, end2)
		} else {
			newInterval := []int{start, end}
			merged_intervals = append(merged_intervals, newInterval)
			start = start2
			end = end2
		}
	}	
	newInterval := []int{start, end}
	merged_intervals = append(merged_intervals, newInterval)

	result1 := 0
	for _, ingredient := range ingredients {
		for i := 0; i < len(merged_intervals); i++ {
			if merged_intervals[i][0] <= ingredient && ingredient <= merged_intervals[i][1] {
				result1++
			}
		}
	}
	fmt.Println("Day 05 Part 01 :", result1)

}
