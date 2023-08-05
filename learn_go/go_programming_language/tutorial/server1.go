package main

import (
	"fmt"
	"image"
	"image/color"
	"image/gif"
	"io"
	"log"
	"math"
	"math/rand"
	"net/http"
	"strconv"
	"sync"
)

var mu sync.Mutex
var num_requests int

var palette = []color.Color{color.White, color.Black}

type lissaParams struct {
	cycles  int
	res     float64
	size    int
	nframes int
	delay   int
}

func lissajous(out io.Writer, params lissaParams) {
	freq := rand.Float64() * 3.0 // relative frequency of y oscillator
	anim := gif.GIF{LoopCount: params.nframes}
	phase := 0.0 // phase difference
	for i := 0; i < params.nframes; i++ {
		rect := image.Rect(0, 0, 2*params.size+1, 2*params.size+1)
		img := image.NewPaletted(rect, palette)
		for t := 0.0; t < float64(params.cycles*2)*math.Pi; t += params.res {
			x := math.Sin(t)
			y := math.Sin(t*freq + phase)
			img.SetColorIndex(params.size+int(x*float64(params.size)+0.5), params.size+int(y*float64(params.size)+.5), blackIndex)
		}
		phase += .1
		anim.Delay = append(anim.Delay, params.delay)
		anim.Image = append(anim.Image, img)
	}
	gif.EncodeAll(out, &anim)
}

const (
	whiteIndex = 0 // first color in palette
	blackIndex = 1 // next color in palette
)

func handler(w http.ResponseWriter, r *http.Request) {
	mu.Lock()
	num_requests++
	mu.Unlock()
	fmt.Fprintf(w, "Url.Path = %q\n", r.URL.Path)
}

func counter(w http.ResponseWriter, r *http.Request) {
	mu.Lock()
	fmt.Fprintf(w, "Count: %d\n", num_requests)
	mu.Unlock()
}

func echoHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "%s %s %s\n", r.Method, r.URL, r.Proto)

	for k, v := range r.Header {
		fmt.Fprintf(w, "%s: %s\n", k, v)
	}

	fmt.Fprintf(w, "Host = %q\n", r.Host)
	fmt.Fprintf(w, "RemoveAddr = %q\n", r.RemoteAddr)

	if err := r.ParseForm(); err != nil {
		log.Println(err)
	}
	for k, v := range r.Form {
		fmt.Fprintf(w, "Form[%q] = %q", k, v)
	}
}

func signwaveHandler(w http.ResponseWriter, r *http.Request) {
	var params lissaParams
	const (
		cycles  = 5     // number of compelte x oscillator revolutions
		res     = 0.001 // angular resolution
		size    = 100   // image canvas covers [-size..+size]
		nframes = 64    // number of animation frames
		delay   = 8     // delay between frames in 10ms units
	)
	if err := r.ParseForm(); err != nil {
		log.Println(err)
	}
	for k, v := range r.Form {
		var err error
		switch k {
		case "cycles":
			params.cycles, err = strconv.Atoi(v[0])
		case "res":
			var res int
			res, err = strconv.Atoi(v[0])
			params.res = float64(res)
		case "size":
			params.size, err = strconv.Atoi(v[0])
		case "nframes":
			params.nframes, err = strconv.Atoi(v[0])
		case "delay":
			params.delay, err = strconv.Atoi(v[0])
		default:
			log.Printf("Unrecognized query: %q=%q", k, v)
		}
		if err != nil {
			log.Println("Invalid, non-int %s value %s: %s", k, v, err)
		}
	}
	if params.cycles == 0 {
		params.cycles = cycles
	}
	if params.res == 0 {
		params.res = res
	}
	if params.size == 0 {
		params.size = size
	}
	if params.nframes == 0 {
		params.nframes = nframes
	}
	if params.delay == 0 {
		params.delay = delay
	}

	lissajous(w, params)
}

func main() {
	http.HandleFunc("/", handler)
	http.HandleFunc("/count", counter)
	http.HandleFunc("/echo", echoHandler)
	http.HandleFunc("/signwave", signwaveHandler)
	log.Fatal(http.ListenAndServe("localhost:8000", nil))
}
