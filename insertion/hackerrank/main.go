package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
    "strconv"
    "strings"
)

func swap(arr []int32, i, j int) {
	arr[i] = arr[j]
}

func print(arr []int32) {
    fmt.Println(strings.Trim(fmt.Sprint(arr), "[]"))
}

/*
 * Complete the 'insertionSort1' function below.
 *
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER_ARRAY arr
 */
func insertionSort1(n int32, arr []int32) {
	rightmost := len(arr) - 1
	pointer := arr[rightmost] // fixed pointer
	previous := rightmost - 1

	for {
        if previous >= 0 && pointer < arr[previous] {
            swap(arr, previous + 1, previous)
    
            previous = previous - 1
        } else {
            arr[previous+1] = pointer
            print(arr)
            break
        }

        print(arr)
	}
}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

    nTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
    checkError(err)
    n := int32(nTemp)

    arrTemp := strings.Split(strings.TrimSpace(readLine(reader)), " ")

    var arr []int32

    for i := 0; i < int(n); i++ {
        arrItemTemp, err := strconv.ParseInt(arrTemp[i], 10, 64)
        checkError(err)
        arrItem := int32(arrItemTemp)
        arr = append(arr, arrItem)
    }

    insertionSort1(n, arr)
}

func readLine(reader *bufio.Reader) string {
    str, _, err := reader.ReadLine()
    if err == io.EOF {
        return ""
    }

    return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
    if err != nil {
        panic(err)
    }
}
