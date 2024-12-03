#lang racket

(require (rename-in "p1.rkt" (solve solve/part1)))
(require (rename-in "p2.rkt" (solve solve/part2)))

(define (extract-ints s)
  (map string->number (regexp-match* #px"-?\\d+" s)))

(define reports (map extract-ints (file->lines "input.txt")))
(printf "part 1: ~a\n" (solve/part1 reports))
(printf "part 2: ~a\n" (solve/part2 reports))
