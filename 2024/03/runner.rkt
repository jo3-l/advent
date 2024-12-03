#lang racket

(require (rename-in "p1.rkt" (solve solve/part1)))
(require (rename-in "p2.rkt" (solve solve/part2)))

(define prog (file->string "input.txt"))
(printf "part 1: ~a\n" (solve/part1 prog))
(printf "part 2: ~a\n" (solve/part2 prog))
