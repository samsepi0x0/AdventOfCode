package main

import (
	"fmt"
	"os"
	"bufio"
	"strings"
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
		fmt.Println("Error Loading file.")
		return
	}

	scanner := bufio.NewScanner(file)

	count := 0
	count2 := 0

	for scanner.Scan() {
		line := scanner.Text()
		result := strings.Split(line, ",")
		for _, value := range result {
			ranges := strings.Split(value, "-")
			startIndex, _ := strconv.Atoi(ranges[0])
			endIndex, _ := strconv.Atoi(ranges[1])

			for i := startIndex; i <= endIndex; i++ {
				str := strconv.Itoa(i)
				length := len(str) / 2
				if str[0:length] == str[length:] {
					count += i
					// fmt.Println(i)
				}
				for s := 1; s < len(str); s++ {
					prefix := str[0:s]
					newstr := strings.Repeat(prefix, len(str)/s)
					if newstr == str {
						count2 += i
						break
					}
				}
			}
		}
	}
	fmt.Println("Day 02 Part 01 :", count)
	fmt.Println("Day 02 Part 02 :", count2)
}
