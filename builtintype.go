package main

import (
	"fmt"
)

type Player struct {
	name        string
	health      int
	attackPower float64
}

func (player Player) getHealth() int {
	return player.health

}

func main() {
	// Using structure
	player := Player{
		name:        "harsha",
		health:      101,
		attackPower: 45.1,
	}

	// Using Map
	//users := map[string]int{}
	users := make(map[string]int)

	users["foo"] = 100
	users["bar"] = 101

	// How to handle Errors

	age, OK := users["aar"]
	if !OK {
		fmt.Println("Bar not exists in the map")
	} else {
		fmt.Println("bar value exists in the map", age)
	}

	fmt.Printf("health: %d+\n", player.getHealth())

	fmt.Printf("health: %+v\n", users)

	// Printing Map
	for k, v := range users {
		fmt.Printf("The Key %s and the value %d \n", k, v)
	}

	numbers := []int{}
	// othernumbers := make( []int, 0 )

	numbers = append(numbers, 1)
	numbers = append(numbers, 10)
	fmt.Println(numbers)
}
