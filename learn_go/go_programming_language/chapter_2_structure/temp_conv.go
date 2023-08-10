package main

const Usage = `A tool for converting between Celsius and Fahrenheit.

Usage:
	temp_conv [-c] <temperature>
`

import (
	"flag"
	"fmt"
	"log"
	"strconv"
)

type Celsius float64

func (c Celsius) String() string {
	return fmt.Sprintf("%.1fC", c)
}

type Fahrenheit float64

func (f Fahrenheit) String() string {
	return fmt.Sprintf("%.1fF", f)
}

// Use an interface to convert to string.
type TempStringer interface {
	String() string
}

func Ttos(s TempStringer) string {
	return s.String()
}

const (
	AbsoluteZero Celsius = -273.15
	FreezingC    Celsius = 0
	BoilingC     Celsius = 100
)

func CToF(c Celsius) Fahrenheit {
	return Fahrenheit((c*9)/5) + 32
}

func FToC(f Fahrenheit) Celsius {
	return Celsius(((f - 32) * 5) / 9)
}

func main() {
	isC := flag.Bool("c", false, "Input is in Celsius.")
	flag.Parse()
	input, err := strconv.ParseFloat(flag.Arg(0), 64)
	if err != nil {
		log.Fatalf("%s is not a valid floating point number.\n\n%s", flag.Arg(0), Usage)
	}

	// Functions are first class types.
	var convert func(input float64) string
	if *isC {
		convert = func(input float64) string {
			return Ttos(CToF(Celsius(input)))
		}
	} else {
		convert = func(input float64) string {
			return Ttos(FToC(Fahrenheit(input)))
		}
	}
	output := convert(input)
	fmt.Println(output)
}
