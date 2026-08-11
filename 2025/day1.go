package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
)

func main() {
	
	if len(os.Args) < 2 {
		fmt.Println("Enter filename")
		return
	}	
	filename := os.Args[1]

	file, err := os.Open(filename)

	if err != nil {
		fmt.Println("The file could not be loaded")
	}

	scanner := bufio.NewScanner(file)
	password := 0
	password2 := 0
	number := 50
	MOD := 100
	
	for scanner.Scan() {
		line := scanner.Text()

		direction := line[0:1]
		delta, err := strconv.Atoi(line[1:])

		if err != nil {
			fmt.Println(line, " could not be parsed.")
			continue
		}

		if direction == "R" {
			password2 += (number + delta) / MOD
			number = (number + delta) % MOD
		} else {
			if number == 0 {
				password2 += delta / MOD
			} else if delta >= number {
				password2 += (delta + 100 - number) / MOD
			}
			number = (number - delta%MOD + MOD) % MOD
		}
		
		if number == 0 {
			password = password + 1	
		}
	}
	fmt.Println("Day 01 Part 01 : ", password)
	fmt.Println("Day 01 Part 02 : ", password2)
}
